import logging
import boto3
from os import listdir
from os.path import isfile, join
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
        response = s3_client.upload_file(file_name,
                                         bucket,
                                         object_name,
                                         ExtraArgs={'ACL': 'private'})
    except ClientError as e:
        logging.error(e)
        return False
    return True


def list_files(directory, extesion=None):
    """Return a list of files in directory
    :param directory: Directory to list the elements
    :return list: Return a list of files in directory"""
    try:
        if extesion:
            file_list = [join(directory, file) for file in listdir(path=directory)
                         if isfile(join(directory, file)) and file.lower().endswith(extesion.lower())]
        else:
            file_list = [join(directory, file) for file in listdir(path=directory)
                         if isfile(join(directory, file))]

    except Exception as e:
        logging.error(e)
        return None
    return file_list


if __name__ == "__main__":
    logging.info("Start process")
    file_list = list_files(directory="data\microdados_educacao_basica_2020\DADOS",
                           extesion="csv")
    print(file_list)
