import os
import time
import sys
import argparse
import datetime
import subprocess
import boto3
import logging
from dotenv import dotenv_values
from botocore.exceptions import ClientError

env = dotenv_values("/opt/pg_backup_env")
AWS_ACCESS_KEY = env['AWS_ACCESS_KEY']
AWS_SECRET_KEY = env['AWS_SECRET_KEY']
AWS_BUCKET_NAME = env['AWS_BUCKET_NAME']
AWS_REGION = env['AWS_REGION']
S3_FOLDER = env['S3_FOLDER']

logging.basicConfig(filename='/var/log/pg_backup.log',
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S',
                    level=logging.INFO)


class ReturnCode(Exception):
    pass


class ParamsBuilder:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def parse(self):
        self.parser.add_argument('--databases', help='List of databases', required=True)
        self.parser.add_argument('--pg_user', help='PostgreSQL user', required=True)
        self.parser.add_argument('--retention', help='Days to store local backups', required=True)
        self.parser.add_argument('--path', help='Folder for local backups', required=True)

        args = self.parser.parse_args()

        return {
            'pg_user': args.pg_user,
            'databases': args.databases,
            'retention': args.retention,
            'path': args.path
        }


class FileCompressor:
    def __init__(self):
        self.dest = parser['path']

    def prepare(self):
        DB=parser['databases'].split(',')
        target = os.path.join(self.dest, "")
        for x in DB:
            archive_check = target + date_str + '-' + x + '.sql.gz'
            if os.path.exists(archive_check):
                logging.info("Archive %s is already exist", archive_check)
                exist = True
            else:
                exist = False
        if not os.path.exists(self.dest):
            os.makedirs(self.dest)

        return {
            'exist' : exist,
            'target' : target
        }

    def compress(self, CH):
        DB=parser['databases'].split(',')
        PG_USER = parser['pg_user']
        prefix_name = CH['target'] + date_str + '-'

        if not CH['exist']:
            try:
                for x in DB:
                    p = subprocess.Popen(
                        'sudo -u ' + PG_USER + ' pg_dump -U ' + PG_USER + ' --no-password -d ' + x + ' --schema=public | gzip' + ' > ' + prefix_name + x + '.sql.gz', shell=True)
                    p.communicate()
                    if p.returncode != 0:
                        raise ReturnCode
                    logging.info('Backup done for DB: %s', x)
            except ReturnCode as e:
                sys.exit('Archives creating failed', e)

        return prefix_name


class Backup:
    def __init__(self):
        self.aws_bucket = AWS_BUCKET_NAME

    def upload_file_to_s3(self, FC):
        DB=parser['databases'].split(',')

        try:
            s3_client = boto3.client(
                service_name='s3',
                aws_access_key_id = AWS_ACCESS_KEY,
                aws_secret_access_key = AWS_SECRET_KEY)
            if current_day == 1:
                retention_days = "KeepAlways"
            else:
                retention_days = "Keep32"
            for x in DB:
                archive_path = FC + x + '.sql.gz'
                archive_full_name = date_str + '-' + x + ".sql.gz"
                object_name = f"{S3_FOLDER}/{archive_full_name}"
                s3_client.upload_file(archive_path, self.aws_bucket, object_name, ExtraArgs={'Tagging': f'RetentionPolicy={retention_days}'})
                logging.info("Archive %s has been uploaded to S3", archive_full_name)
        except ClientError as e:
            logging.error(f"Error while uploading {archive_full_name} to S3: {e}")
            sys.exit(e)


class Cleanup:
    def __init__(self):
        pass

    def local_cleaner (self):
        try:
            for filename in os.listdir(parser['path']):
                if os.path.getmtime(os.path.join(parser['path'], filename)) < time.time() - float(parser['retention']) * 86400:
                    if os.path.isfile(os.path.join(parser['path'], filename)):
                        logging.info('Deleted %s', filename)
                        os.remove(os.path.join(parser['path'], filename))
        except Exception as e:
            logging.error("Error %s while deleting files", e)
            sys.exit(e)
        else:
            logging.info("Cleaner task has been finished successfully")
            sys.exit(0)


if __name__ == '__main__':
    logging.info("Starting backup process")
    date_r = datetime.datetime.now()
    date_str = date_r.strftime('%Y-%m-%d')
    current_day = date_r.day

    parser = ParamsBuilder().parse()

    file = FileCompressor()
    check = file.prepare()
    arch = file.compress(check)

    backup = Backup()
    backup.upload_file_to_s3(arch)

    clean = Cleanup()
    clean.local_cleaner()
    logging.info("Finishing backup process")
