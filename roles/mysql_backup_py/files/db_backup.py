import os
import time
import sys
import argparse
import datetime
import subprocess
import logging
import boto3

from dotenv import dotenv_values
from botocore.exceptions import ClientError
from botocore.config import Config

LOG_PATH = '/var/log/db_backup.log'
SMALL_FILE_SIZE_THRESHOLD = 20

logging.basicConfig(
    filename=LOG_PATH,
    filemode='a',
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d,%H:%M:%S',
    level=logging.INFO
)

env = dotenv_values("/etc/zabbix/scripts/db_backup.env")
AWS_SECRET = env['AWS_SECRET']
AWS_BUCKET = env['AWS_BUCKET']
AWS_REGION = env['AWS_REGION']
AWS_SECKEY = env['AWS_SECKEY']
MYSQL_PASS = env['MYSQL_PASS']
MYSQL_USER = env['MYSQL_USER']
S3_FOLDER  = env['S3_FOLDER']


class ReturnCode(Exception):
    pass


class ParamsBuilder:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def parse(self):
        self.parser.add_argument('--databases', help='DB list', required=True)
        self.parser.add_argument('--retention', help='Days for store', required=True, type=int)
        self.parser.add_argument('--path', help='Folder for local backups', required=True)
        args = self.parser.parse_args()

        return {
            'databases': args.databases.split(','),
            'retention': args.retention,
            'path': args.path
        }


class FileCompressor:
    def __init__(self, parser):
        self.parser = parser
        self.dest = parser['path']

    def prepare(self):
        target = os.path.join(self.dest, "")
        exist = all(
            os.path.exists(os.path.join(self.dest, f"{date_str}-{db}.sql.gz")) and
            os.path.getsize(os.path.join(self.dest, f"{date_str}-{db}.sql.gz")) > SMALL_FILE_SIZE_THRESHOLD
            for db in self.parser['databases']
        )
        logging.info("Archives exist: %s", exist, "proceeding with backup")

        if not os.path.exists(self.dest):
            os.makedirs(self.dest)

        return {'exist': exist, 'target': target}

    def compress(self, check):
        prefix_name = check['target'] + date_str + '-'

        if not check['exist']:
            for db in self.parser['databases']:
                dump_command = f'mysqldump -h localhost -u {MYSQL_USER} -p{MYSQL_PASS} {db} --single-transaction --no-tablespaces --log-error=/dev/null | gzip > {prefix_name}{db}.sql.gz'
                logging.info("Dumping DB: %s", db)

                with subprocess.Popen(dump_command, shell=True) as proc:
                    proc.communicate()
                    if proc.returncode != 0:
                        logging.error("Backup failed for database: %s", db)
                        raise ReturnCode(f"Backup failed for database: {db}")

                logging.info("Backup done for DB: %s", db)

        return prefix_name


class Backup:
    def __init__(self):
        self.aws_bucket = AWS_BUCKET
        self.s3_client = boto3.client(
            service_name='s3',
            aws_access_key_id=AWS_SECKEY,
            aws_secret_access_key=AWS_SECRET,
            config=Config(
                connect_timeout=5,
                retries={'max_attempts': 2},
                s3={'addressing_style': 'path'},
                use_dualstack_endpoint=False
            )
        )

    def upload_file_to_s3(self, file_prefix):
        for db in parser['databases']:
            archive_path = f"{file_prefix}{db}.sql.gz"
            archive_full_name = f"{date_str}-{db}.sql.gz"
            object_name = f"{S3_FOLDER}/{archive_full_name}"

            try:
                file_size = os.path.getsize(archive_path)
                if file_size <= SMALL_FILE_SIZE_THRESHOLD:
                    logging.warning("Archive %s is too small (%d bytes) or empty, skipping upload", archive_full_name, file_size)
                else:
                    self.s3_client.upload_file(archive_path, self.aws_bucket, object_name)
                    logging.info("Uploading %s to %s/%s", archive_path, self.aws_bucket, object_name)
            except ClientError as e:
                logging.error("Error while uploading %s to S3: %s", archive_full_name, e)
                sys.exit(e)


class Cleanup:
    def __init__(self, parser):
        self.parser = parser

    def cleaner(self):
        try:
            for filename in os.listdir(self.parser['path']):
                filepath = os.path.join(self.parser['path'], filename)
                if os.path.isfile(filepath) and os.path.getmtime(filepath) < time.time() - float(self.parser['retention']) * 86400:
                    logging.info("Delete old backup file: %s", filename)
                    os.remove(filepath)
        except Exception as e:
            logging.error("Error while deleting files: %s", e)
            sys.exit("Error while deleting files %s", e)
        else:
            logging.info("Cleanup done successfully", filepath)
            sys.exit(0)


def main():
    file_compressor = FileCompressor(parser)
    backup = Backup()
    cleanup = Cleanup(parser)

    check = file_compressor.prepare()
    archive_prefix = file_compressor.compress(check)

    try:
        backup.upload_file_to_s3(archive_prefix)
    except Exception as e:
        logging.error("Error while uploading files to S3: %s", e)
        sys.exit(e)
    else:
        logging.info("Operation completed successfully for %s", archive_prefix)
        cleanup.cleaner()


if __name__ == "__main__":
    date_now = datetime.datetime.now()
    date_str = date_now.strftime('%Y-%m-%d')
    parser = ParamsBuilder().parse()
    main()
