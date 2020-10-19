from api_tests.config_files import config
import pytest
import json

from api_tests.config_files.config import REASONABLE_ADJUSTMENTS_PROXY
from api_tests.config_files.environments import ENV
from api_tests.scripts.apigee_api import ApigeeDebugApi
from api_tests.scripts.generic_request import GenericRequest


# @pytest.fixture()
# def switch_to_invalid_asid_application():
#     print("here")
#     config.CLIENT_ID = ENV['oauth']['invalid_asid_client_id']
#     config.CLIENT_SECRET = ENV['oauth']['invalid_asid_client_secret']
#     config.REDIRECT_URI = "https://example.com/callback"

@pytest.mark.usefixtures("setup")
class TestAsidSuite:
    """ A test suit to verify ASID is fetched from Custom Attributes associated with the App """

    @pytest.mark.asid
    def test_valid_asid(self, switch_to_app, get_token):
        # Given
        switch_to_app('with_valid_asid')

        debug_session = ApigeeDebugApi(REASONABLE_ADJUSTMENTS_PROXY)
        expected_asid = '200000001115'

        # When
        self.send_a_request()

        # Then
        actual_asid = debug_session.get_apigee_variable('verifyapikey.VerifyAPIKey.CustomAttributes.asid')
        assert actual_asid == expected_asid

    @pytest.mark.asid
    @pytest.mark.invalid_asid
    @pytest.mark.errors
    def test_invalid_asid(self, switch_to_invalid_asid, get_token):
        self.reasonable_adjustments.check_endpoint(
            verb='GET',
            endpoint='consent',
            expected_status_code=500,
            expected_response={
                'error': 'invalid/missing ASID/ODS',
                'error_description': 'An internal server error occurred. Invalid/missing ASID/ODS. Contact us for assistance diagnosing this issue: https://digital.nhs.uk/developer/help-and-support quoting Message ID',
            },
            params={
                'patient':  'test',
                'category': 'test',
                'status':   'test',
            },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': 'test'
            }
        )

    @pytest.mark.asid
    @pytest.mark.invalid_asid
    @pytest.mark.errors
    def test_missing_asid(self, switch_to_missing_asid, get_token):
        self.reasonable_adjustments.check_endpoint(
            verb='GET',
            endpoint='consent',
            expected_status_code=500,
            expected_response={
                'error': 'invalid/missing ASID/ODS',
                'error_description': 'An internal server error occurred. Invalid/missing ASID/ODS. Contact us for assistance diagnosing this issue: https://digital.nhs.uk/developer/help-and-support quoting Message ID',
            },
            params={
                'patient':  'test',
                'category': 'test',
                'status':   'test',
            },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': 'test'
            }
        )

    def send_a_request(self):
        self.reasonable_adjustments.check_endpoint(
            verb='GET',
            endpoint='consent',
            expected_status_code=200,
            expected_response=None,
            params={
                'patient':  'test',
                'category': 'test',
                'status':   'test',
            },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': 'test'
            }
        )

