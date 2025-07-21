#!/usr/bin/env python3

import os
import shutil
import tarfile
import argparse
import sys
import logging
from datetime import datetime, timedelta

logging.basicConfig(filename='/var/log/folder_backup.log',
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S',
                    level=logging.INFO)

class ParamsBuilder:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--source', help='Source folder with files to backup', required=True)
        self.parser.add_argument('--destination', help='Destination folder for backup store', required=True)
        self.parser.add_argument('--cleanup', action='store_true', help='Remove source folder after backup if specified', required=False)

    def parse(self):
        args = self.parser.parse_args()
        return {
            'source': args.source,
            'dest': args.destination,
            'cleanup': args.cleanup
        }


class FileCompressor:
    def __init__(self, params):
        self.path = params['source']
        self.dest = params['dest']

    def prepare(self):
        dt = datetime.now() - timedelta(days=1)
        mon = dt.strftime("%m")
        year = dt.strftime("%Y")

        src = os.path.join(self.path, year, mon, "")
        target = os.path.join(self.dest, year, "")
        archive = target + dt.strftime('%Y-%m') + '.tgz'

        if not os.path.exists(target):
            os.makedirs(target)

        if not os.path.exists(src):
            logging.error(f"Error: source {src} isn't found")
            sys.exit(f"Error: source {src} isn't found")

        if os.path.exists(archive):
            logging.info(f"Archive {archive} already exists")
            sys.exit(f"Error: {archive} already exists")

        self.src = src
        self.target = target
        self.archive = archive

        return {
            'target': target,
            'src': src,
            'archive': archive
        }

    def compress(self):
        try:
            with tarfile.open(self.archive, 'w:gz') as tar:
                tar.add(self.src, recursive=True)
        except tarfile.TarError as e:
            logging.error(f"Error while compressing: {e}")
            sys.exit(f"Error while archiving: {e}")
        logging.info("Successfully saved backup into: %s", self.archive)


class Cleanup:
    def cleaner(self, src):
        try:
            shutil.rmtree(src)
        except OSError as e:
            logging.error(f"Error {e} while deleting the source folder from: {src}")
            sys.exit(f"Error {e} while deleting the source folder from: {src}")
        logging.info("Successfully deleted old data from: %s", src)


if __name__ == '__main__':
    params_builder = ParamsBuilder()
    params = params_builder.parse()

    file = FileCompressor(params)
    dirs = file.prepare()
    file.compress()

    if params['cleanup']:
        cleaner = Cleanup()
        cleaner.cleaner(dirs['src'])
