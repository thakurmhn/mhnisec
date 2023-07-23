import yaml
from yaml.loader import BaseLoader
import os
from pprint import pprint
from breeze_connect import BreezeConnect
from datetime import datetime

class BzUtils:

    def __init__(self):

        self.secret_file = f"{os.getcwd()}/secret_token.yaml"
        # self.breeze = BreezeConnect(api_key=self.api_key)
        # self.bz_session = self.breeze.generate_session(api_secret=self.app_secret, session_token=self.session_token)

    def get_api_creds(self):
        _secret_dict = ''
        with open(self.secret_file, 'r') as file:
            isec_secret = yaml.load(file, Loader=yaml.FullLoader)

            _secret_dict = isec_secret
        return _secret_dict

    @property
    def breeze(self):
        breeze = BreezeConnect(api_key=self.api_key)
        return breeze

    @property
    def bz_session(self):
        bz_session = self.breeze.generate_session(api_secret=self.app_secret, session_token=self.session_token)
        return bz_session

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
        breeze = self.breeze
        bz_session = self.bz_session
        customer_details = breeze.get_customer_details(api_session=self.session_token)
        print(self.session_token)
        return customer_details

    @property
    def get_funds(self):
        breeze = BreezeConnect(api_key=self.api_key)
        bz_session = breeze.generate_session(api_secret=self.app_secret, session_token=self.session_token)
        funds = breeze.get_funds()
        return funds

    @property
    def demat_holdings(self):
        breeze = self.breeze
        bz_session = self.bz_session
        holdings = breeze.get_demat_holdings()
        return holdings

    @staticmethod
    def get_datetime_iso(month, day, date, time, year=2023):
        try:
            # Construct the datetime string
            datetime_str = f"{year}-{month:02d}-{date:02d}T{time}"

            # Parse the datetime string
            parsed_datetime = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")

            # Convert the parsed datetime to the desired format
            iso_format = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S.000Z")

            # Return the datetime in the desired format
            return iso_format
        except ValueError:
            return "Invalid datetime parameters. Please provide valid month, date, and time."

if __name__ == '__main__':
    bz = BzUtils()
    pprint(bz.bz_session)







