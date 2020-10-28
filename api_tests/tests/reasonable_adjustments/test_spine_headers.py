import pytest
from api_tests.config_files import config
from api_tests.scripts.apigee_api import ApigeeDebugApi


@pytest.mark.usefixtures("setup")
class TestSpineHeadersSuite:
    """ A test suite to verify the spine headers are sent as part of the target backend request """

    @pytest.mark.spine_headers
    @pytest.mark.usefixtures('get_token')
    def test_fromASID_header_is_set(self):
        # Given
        debug_session = ApigeeDebugApi(config.REASONABLE_ADJUSTMENTS_PROXY)
        expected_header_value = '200000001115'

        # When
        self.send_a_get_consent_request()

        # Then
        actual_header_value = debug_session.get_apigee_header('FromASID')
        assert actual_header_value == expected_header_value

    @pytest.mark.spine_headers
    @pytest.mark.usefixtures('get_token')
    def test_ToASID_header_is_set(self):
        # Given
        debug_session = ApigeeDebugApi(config.REASONABLE_ADJUSTMENTS_PROXY)
        expected_header_value = '200000006422'

        # When
        self.send_a_get_consent_request()

        # Then
        actual_header_value = debug_session.get_apigee_header('ToASID')
        assert actual_header_value == expected_header_value

    def send_a_get_consent_request(self):
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
