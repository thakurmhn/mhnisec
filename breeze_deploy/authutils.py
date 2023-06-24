import yaml
from yaml.loader import BaseLoader


def get_api_creds():
    _secret_file = '/home/mohan/icicidirect-api-keys/app_secrets.yaml'
    app_secrets_dict = ''
    with open(_secret_file, 'r') as stream:

        try:
            # Converts yaml document to python object
            app_secrets_dict = yaml.load(stream, Loader=BaseLoader)
            for key, val in app_secrets_dict.items():
                print(key, " : ", val, "\n")
        except yaml.YAMLError as e:
            LOG.info(e)

    return app_secrets_dict

