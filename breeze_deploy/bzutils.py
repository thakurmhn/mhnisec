import yaml
from yaml.loader import BaseLoader
import os
from pprint import pprint
from breeze_connect import BreezeConnect

class BzUtils:

    def __init__(self):

        self.secret_file = f"{os.getcwd()}/secret_token.yaml"

    def get_api_creds(self):
        _secret_dict = ''
        with open(self.secret_file, 'r') as file:
            isec_secret = yaml.load(file, Loader=yaml.FullLoader)

            _secret_dict = isec_secret
        return _secret_dict

    @property
    def api_key(self):
        _secrets = self.get_api_creds()
        _api_key = _secrets['api_key']
        return _api_key

    @property
    def app_secret(self):
        _secrets = self.get_api_creds()
        _app_secret = _secrets['app_secret']
        return _app_secret

    @property
    def session_token(self):
        _secret = self.get_api_creds()
        _session_token = _secret['session_token']
        return _session_token

    @property
    def customer_details(self):
        breeze = BreezeConnect(api_key=self.api_key)
        bz_session = breeze.generate_session(api_secret=self.app_secret, session_token=self.session_token)
        customer_details = breeze.get_customer_details(api_session=self.session_token)
        return customer_details

    @property
    def get_funds(self):
        breeze = BreezeConnect(api_key=self.api_key)
        bz_session = breeze.generate_session(api_secret=self.app_secret, session_token=self.session_token)
        funds = breeze.get_funds()
        return funds

    @property
    def demat_holdings(self):
        breeze = BreezeConnect(api_key=self.api_key)
        bz_session = breeze.generate_session(api_secret=self.app_secret, session_token=self.session_token)
        holdings = breeze.get_demat_holdings()
        return holdings


