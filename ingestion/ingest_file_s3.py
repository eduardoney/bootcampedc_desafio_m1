import logging
import boto3
from os import listdir
from os.path import isfile, join, basename
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If name not specified, use file name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        logging.info(f"Upload: file {object_name}")
        response = s3_client.upload_file(file_name,
                                         bucket,
                                         object_name,
                                         ExtraArgs={'ACL': 'private'})
    except ClientError as e:
        logging.error(e)
        return False
    return True


def list_files(directory, extesion=None, with_path=True):
    """Return a list of files in directory
    :param directory: Directory to list the elements
    :return list: Return a list of files in directory"""
    try:
        if extesion:
            file_list = [join(directory, file) if with_path else file for file in listdir(path=directory)
                         if isfile(join(directory, file)) and file.lower().endswith(extesion.lower())]
        else:
            file_list = [join(directory, file) if with_path else file for file in listdir(path=directory)
                         if isfile(join(directory, file))]

    except Exception as e:
        logging.error(e)
        return None
    return file_list


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s|%(levelname)s|%(message)s')

    bucket = "datalake-eduardoney-707008544288"
    directory = ".\\data\\microdados_educacao_basica_2020\\DADOS"

    logging.info("Start process")

    file_list = list_files(directory=directory,
                           extesion="csv",
                           with_path=True)

    logging.info(f'Files to process: {file_list}')

    for file in file_list:
        object_name = f"raw-data/microdados_educacao_basica_2020/{basename(file)}"
        result = upload_file(file_name=file,
                             bucket=bucket,
                             object_name=object_name)
        logging.info(f"Upload result: {result}")

    logging.info("Ended process")