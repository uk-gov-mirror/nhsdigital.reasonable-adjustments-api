import requests
import time
import json

from api_tests.config_files.config import REASONABLE_ADJUSTMENTS_CONSENT
from assertpy import assert_that
import uuid

from api_tests.tests import request_bank
from api_tests.tests.request_bank import Request


def get_consent_details(response):
    result_dict = json.loads(response.text)
    consent_exists = False
    consent_id = None
    version_id = None

    if 'total' in result_dict:
        if result_dict['total'] > 0:
            consent_exists = True
            consent_id = result_dict['entry'][0]['resource']['id'];
            version_id = 'W/"' + result_dict['entry'][0]['resource']['meta']['versionId'] + '"'

    return {'consent_exists': consent_exists, 'consent_id': consent_id, 'version_id': version_id}


class Utils:
    """ A Utils class to be used for shared functionality between tests  """

    @staticmethod
    def send_request(self) -> requests.Response:
        response = requests.get(
            url=REASONABLE_ADJUSTMENTS_CONSENT,
            params={'patient': 'test', 'category': 'test', 'status': 'test'},
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
            }
        )

        return response

    @staticmethod
    def get_etag(self, resource_url: str, params):
        response = requests.get(
            url=resource_url,
            params=params,
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': '093895563513',
                'x-request-id': str(uuid.uuid4()),
            }
        )
        time.sleep(1)
        return response.headers['etag']

    @staticmethod
    def send_consent_post(auth_token:str):
        expected_status_code = 201

        response = requests.post(
            url=REASONABLE_ADJUSTMENTS_CONSENT,
            json=request_bank.get_body(Request.CONSENT_POST),
            headers={
                'Authorization': f'Bearer {auth_token}',
                'nhsd-session-urid': '093895563513',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json'
            })

        time.sleep(1)
        assert_that(expected_status_code).is_equal_to(response.status_code)
        return response

    @staticmethod
    def send_consent_put(token:str, consent_id:str, version_id:str):
        expected_status_code = 200

        response = requests.put(
            url=REASONABLE_ADJUSTMENTS_CONSENT + '/' + consent_id,
            json=request_bank.get_body(Request.CONSENT_PUT),
            headers={
                'Authorization': f'Bearer {token}',
                'nhsd-session-urid': '093895563513',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json',
                'If-Match': version_id
            }
        )

        time.sleep(1)
        assert_that(expected_status_code).is_equal_to(response.status_code)
        return response

    @staticmethod
    def send_get_consent(auth_token:str):
        response = requests.get(
            url=REASONABLE_ADJUSTMENTS_CONSENT,
            params={
                'patient': '9692247317',
                'category': 'https://fhir.nhs.uk/STU3/CodeSystem/RARecord-FlagCategory-1|NRAF',
                'status': 'active'
            },
            headers={
                'Authorization': f'Bearer {auth_token}',
                'nhsd-session-urid': '093895563513',
                'x-request-id': str(uuid.uuid4()),
                'Accept': 'application/fhir+json'
            }
        )

        time.sleep(1)
        return get_consent_details(response)
