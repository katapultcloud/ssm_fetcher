# Usage

## Requirements

```
python3
boto3
```

## Installation

Add line to `~/.bashrc` or `~/.bash_profile` etc.

```
alias f-ssm='<path>/fetch-ssm.py'
```

## Examples

### Fetching one parameter

```
$ f-ssm secret-url
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

## Future Enhancments
* Currently fetches secrets from `us-east-1` region only. This needs to be parameterized.
* Add option to output JSON.
