import boto3
import sys


def ssm_client():
    session = boto3.Session(region_name='us-east-1')
    ssm = session.client('ssm')
    return ssm


def fetch_ssm(path):
    ssm = ssm_client()
    try:
        response = ssm.get_parameter(Name=path, WithDecryption=True)
        return response['Parameter']['Value']
    except ssm.exceptions.ParameterNotFound:
        return ''


def main():
    for ssm_path in sys.argv[1:]:
        print(ssm_path + ':\n' + fetch_ssm(ssm_path))
    return None


if __name__ == '__main__':
    main()
