from api_tests.config_files import config
import pytest
import json

from api_tests.config_files.config import REASONABLE_ADJUSTMENTS_PROXY
from api_tests.config_files.environments import ENV
from api_tests.scripts.apigee_api import ApigeeDebugApi
from api_tests.scripts.generic_request import GenericRequest


@pytest.mark.usefixtures("setup")
class TestAsidSuite:
    """ A test suit to verify ASID is fetched from Custom Attributes associated with the App """

    @pytest.mark.asid
    def test_asid(self, get_token):
        # Given
        # valid_asid_id = ENV['oauth']['invalid_asic_client_id']
        # valid_asid_secret = ENV['oauth']['invalid_asic_client_secret']
        # switch_app(valid_asid_id, valid_asid_secret)

        debug_session = ApigeeDebugApi(REASONABLE_ADJUSTMENTS_PROXY)
        expected_asid = '200000001115'

        # When
        self.send_a_request()

        # Then
        actual_asid = debug_session.get_apigee_variable('verifyapikey.VerifyAPIKey.CustomAttributes.asid')
        assert actual_asid == expected_asid

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

