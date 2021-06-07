import yaml
from credmanager.credential_manager import CredentialManager

LOCAL_SECRETS_FILE = "config/secrets.yaml"
ROLE_ARN = 'arn:aws:iam::127579856528:role/data-secrets-ro'

def generate_creds_from_path(**secrets):
    if not secrets:
       log.info("AWS secrets missing from file secrets.yaml file")
    return CredentialManager(role_arn=ROLE_ARN).lookup_credential(**secrets)

def get_secret(secret_key):
    return get_value_from_key(LOCAL_SECRETS_FILE, secret_key)
