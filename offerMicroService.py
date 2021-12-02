import os
from flask_sqlalchemy import SQLAlchemy
from flask import current_app, abort
from models import Product, OffersMS
from schemas import product_schema_relation
import requests
from functools import cached_property


DEFAULT_OFFERSMS_URL = 'https://applifting-python-excercise-ms.herokuapp.com/api/v1'
OFFERS_MS_URL = 'localhost:5000'
'''
once deployed to heroku it should get the url from there with this line
os.environ.get(
    'OFFERS_MS_URL', DEFAULT_OFFERSMS_URL).rstrip('/')'''

OFFERS_URL = {
    'auth': f'{OFFERS_MS_URL}/auth',
    'register_product': f'{OFFERS_MS_URL}/products/register',
    'get_offers': lambda product: f'{OFFERS_MS_URL}/products/{product.uuid}/offers'
}


def abort_503():
    abort(503, {'message': 'Call failed'})


class OffersMsClient:

    def register_product(self, product: Product):
        url = OFFERS_URL['register_product']
        data = product_schema_relation.dump(product)

        current_app.logger.info(
            f'Registering product with uuid={data["id"]} and headers {self._headers}')
        r = requests.post(url=url, headers=self._headers, data=data)
        if r.status_code:
            return True

        else:
            current_app.logger.error(
                f'register_product({product}) failed', response=r)
            abort_503()

    def extract_offers(self, product: Product):
        url = OFFERS_URL['get_offers'](product)
        r = requests.get(url, headers=self._headers)
        if not r.ok:
            current_app.logger.error(
                f'extract_offers({product}) failed', response=r)
            return []

        return r.json()

    @staticmethod
    def _extract_access_token():
        url = OFFERS_URL['auth']
        current_app.logger.info('Calling auth.')
        r = requests.post(url=url)
        return r.json()['access_token']

    @cached_property
    def get_access_token(self) -> str:
        return OffersMS.get_access_token(self._extract_access_token)

    @property
    def _headers(self):
        return {'Bearer': self.get_access_token}
