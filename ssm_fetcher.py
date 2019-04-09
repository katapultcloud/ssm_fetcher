import boto3
import argparse
import json


def arguments():
    parser = argparse.ArgumentParser(description='SSM Parameter Fetcher')
    parser.add_argument(
        '--json', '-j', action='store_true', help='enables json output')
    parser.add_argument(
        '--profile',
        '-p',
        type=str,
        default='default',
        help='aws profile to use, default "default"')
    parser.add_argument(
        'ssm_parameters',
        metavar='ssm_params',
        type=str,
        nargs='+',
        help='list of ssm parameters')
    parser.add_argument(
        '--region',
        '-r',
        type=str,
        default='us-east-1',
        help='aws region to use, default "us-east-1"')
    args = parser.parse_args()
    return args


def ssm_client(region_name, profile_name):
    session = boto3.Session(region_name=region_name, profile_name=profile_name)
    ssm = session.client('ssm')
    return ssm


def fetch_ssm(ssm, path):
    try:
        response = ssm.get_parameter(Name=path, WithDecryption=True)
        return response['Parameter']['Value']
    except ssm.exceptions.ParameterNotFound:
        return ''


def main():
    args = arguments()
    ssm_auth = ssm_client(args.region, args.profile)
    if args.json:
        output = {}
    else:
        output = ''

    for ssm_parameter in args.ssm_parameters:
        if args.json:
            output[ssm_parameter] = fetch_ssm(ssm_auth, ssm_parameter)
        else:
            output += ssm_parameter + ':\n' + fetch_ssm(ssm_auth, ssm_parameter) + '\n'

    if args.json:
        return json.dumps(output)
    else:
        return output


if __name__ == '__main__':
    print(main())
