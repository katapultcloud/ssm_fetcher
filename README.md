# Usage

## Requirements

```
python3
boto3
```

## Installation

Add line to `~/.bashrc` or `~/.bash_profile` etc.

```
alias f-ssm='<path>/ssm_fetcher.py'
```

## Help

```
$ f-ssm --help
usage: ssm_fetcher.py [-h] [--json] [--profile PROFILE] [--region REGION]
                      ssm_params [ssm_params ...]

SSM Parameter Fetcher

positional arguments:
  ssm_params            list of ssm parameters

optional arguments:
  -h, --help            show this help message and exit
  --json, -j            enables json output
  --profile PROFILE, -p PROFILE
                        aws profile to use, default "default"
  --region REGION, -r REGION
                        aws region to use, default "us-east-1"

```

## Examples

### Fetching one parameter

```
$ f-ssm secret-url
secret-url:
secret.example.com
```

### Fetching one parameter with json format

```json
$ f-ssm secret-url --json
{"secret-url": "secret.example.com"}
```

### Fetching one parameter with different aws profile

```
$ f-ssm secret-url -p boto_profile
secret-url:
secret.example.com
```

### Fetching one parameter with non-default aws profile from non-default aws region

```
$ f-ssm secret-url -p boto_profile -r us-west-1
secret-url:
secret.example.com
```

### Fetching multiple parameters
```
$ f-ssm private-key.pem i-dont-exist website-password
private-key.pem:
<private_key>

i-dont-exist:

website-password:
Password1234!
```
