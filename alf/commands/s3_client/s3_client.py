#!/usr/bin/env python
import logging
import os
import boto3

logger = logging.getLogger(__name__)


class S3Client:
    client = None
    resource = None
    bucket = None

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, bucket=''):
        if aws_access_key_id is not None and aws_secret_access_key is not None:
            self.client = boto3.client('s3',
                                       aws_access_key_id=aws_access_key_id,
                                       aws_secret_access_key=aws_secret_access_key
                                       )
            self.resource = boto3.resource('s3',
                                           aws_access_key_id=aws_access_key_id,
                                           aws_secret_access_key=aws_secret_access_key
                                           )
            self.bucket = bucket

    @staticmethod
    def _tree(files, show_file=False, show_full_dir=False):
        """
        Display tree folder of model
        :param input_dir:
        :param padding:
        :param print_files:
        :return:
        """
        padding = '│   '
        prefix = '├──'
        for dir, files in files.items():
            len_dir = len(dir.split('/')) - 2
            padding_dir = ''
            for i in range(0, len_dir):
                padding_dir += padding
            if not show_full_dir:
                dir = dir.split('/')[-2]
            print(padding_dir + prefix, dir)
            if show_file:
                for file in files:
                    print(padding_dir + padding + prefix, file)

    def get_files(self, s3_source='', structure_files={}):
        paginator = self.client.get_paginator('list_objects')
        for result in paginator.paginate(Bucket=self.bucket, Delimiter='/', Prefix=s3_source):
            if result.get('CommonPrefixes') is not None:
                for subdir in result.get('CommonPrefixes'):
                    if subdir.get('Prefix').endswith('/'):
                        folder_name = subdir.get('Prefix')
                        structure_files[folder_name] = []
                        self.get_files(subdir.get('Prefix'), structure_files)
            for file in result.get('Contents', []):
                if not file.get('Key').endswith('/'):
                    folder_name = os.path.dirname(file.get('Key')) + '/'
                    file_name = os.path.basename(file.get('Key'))

                    if structure_files.get(folder_name) is None:
                        structure_files[folder_name] = [file_name]
                    else:
                        structure_files[folder_name].append(file_name)
        return structure_files

    def show_structure(self, s3_source='', show_file=True, show_full_dir=True):
        """
        :param visualize: path of folder in the bucket
        :param destination: path of folder in the project
        :param show_file: Display path of file
        :param show_full_dir: Display path of dir
        :return:
        """
        structure_files = self.get_files(s3_source, {})
        print("SHOW STRUCTURE S3", s3_source)
        self._tree(structure_files, show_file, show_full_dir)

    def download(self, source='', destination='/'):
        if destination is None or destination == '/':
            logger.error("Destination is invalided")
        else:
            paginator = self.client.get_paginator('list_objects')
            for result in paginator.paginate(Bucket=self.bucket, Delimiter='/', Prefix=source):
                if result.get('CommonPrefixes') is not None:
                    for subdir in result.get('CommonPrefixes'):
                        self.download(subdir.get('Prefix'), destination)
                for file in result.get('Contents', []):
                    if not file.get('Key').endswith('/'):
                        dest_pathname = os.path.join(destination, file.get('Key'))
                        if os.path.exists(dest_pathname) and \
                                file.get('Size') == os.path.getsize(dest_pathname):
                            continue
                        logger.info("DOWNLOAD FILE: {}".format(file.get('Key')))
                        if not os.path.exists(os.path.dirname(dest_pathname)):
                            os.makedirs(os.path.dirname(dest_pathname))
                        self.client.download_file(self.bucket, file.get('Key'), dest_pathname)

    def upload(self, source, destination):
        return self.client.upload_file(source, self.bucket, destination)

    def list_bucket(self):
        response = self.client.list_buckets()

        # Output the bucket names
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')

    def delete(self, key):
        obj = self.resource.Object(self.bucket, key)
        return obj.delete()
