import base64
import json
import uuid

import pytest
import requests
from assertpy import assert_that

from api_tests.config_files import config
from api_tests.config_files.config import REASONABLE_ADJUSTMENTS_PROXY_NAME, REASONABLE_ADJUSTMENTS_PROXY_PATH
from api_tests.scripts.apigee_api import ApigeeDebugApi
from api_tests.tests.utils import Utils


@pytest.mark.usefixtures("setup")
class TestProxyCasesSuite:
    """ A test suite to verify all the happy path oauth endpoints """

    @pytest.mark.spine_headers
    @pytest.mark.integration
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_ASID_fetch(self):
        # Given
        debug_session = ApigeeDebugApi(config.REASONABLE_ADJUSTMENTS_PROXY_NAME)
        expected_value = '200000001390'

        # When
        Utils.send_request(self)

        # Then
        actual_asid = debug_session.get_apigee_variable('verifyapikey.VerifyAPIKey.CustomAttributes.asid')
        assert_that(expected_value).is_equal_to(actual_asid)

        actual_header_value = debug_session.get_apigee_header('NHSD-ASID')
        assert_that(expected_value).is_equal_to(actual_header_value)

    @pytest.mark.spine_headers
    @pytest.mark.integration
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_x_request_id_equals_nhsd_request_id(self):
        # Given
        debug_session = ApigeeDebugApi(config.REASONABLE_ADJUSTMENTS_PROXY_NAME)

        # When
        Utils.send_request(self)

        # Then
        trace_id = debug_session.get_apigee_header('NHSD-Request-ID')
        x_request_id = debug_session.get_apigee_header('x-request-id')

        assert_that(trace_id).is_equal_to(x_request_id)

    @pytest.mark.ods
    @pytest.mark.integration
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_valid_ods(self):
        # Given
        debug_session = ApigeeDebugApi(REASONABLE_ADJUSTMENTS_PROXY_NAME)
        expected_ods = 'D82106'

        # When
        Utils.send_request(self)

        # Then
        actual_ods = debug_session.get_apigee_variable('verifyapikey.VerifyAPIKey.CustomAttributes.ods')

        assert_that(expected_ods).is_equal_to(actual_ods)

    @pytest.mark.jwt
    @pytest.mark.integration
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_jwt(self):
        # Given
        debug_session = ApigeeDebugApi(REASONABLE_ADJUSTMENTS_PROXY_NAME)
        expected_jwt_claims = {
            'reason_for_request': 'directcare',
            'scope': 'user/Consent.read',
            'requesting_organization': 'https://fhir.nhs.uk/Id/ods-organization-code|D82106',
            'requesting_system': 'https://fhir.nhs.uk/Id/accredited-system|200000001390',
            'requesting_user': 'https://fhir.nhs.uk/Id/sds-role-profile-id|test',
            'sub': 'https://fhir.nhs.uk/Id/sds-role-profile-id|test',
            'iss': 'http://api.service.nhs.uk',
            'aud': f'/{REASONABLE_ADJUSTMENTS_PROXY_PATH}/Consent'
        }

        # When
        Utils.send_request(self)

        # Then
        # We should pull Authorization header instead but Apigee mask that value so we get spineJwt variable instead
        actual_jwt = debug_session.get_apigee_variable('spineJwt')

        # We manually decode jwt because, jwt library requires all three segments but we only have two (no signature).
        jwt_segments = actual_jwt.split('.')
        actual_jwt_claims = json.loads(base64.b64decode(jwt_segments[1]))

        assert_that(expected_jwt_claims['reason_for_request']).is_equal_to_ignoring_case(actual_jwt_claims['reason_for_request'])
        assert_that(expected_jwt_claims['scope']).is_equal_to_ignoring_case(actual_jwt_claims['scope'])
        assert_that(expected_jwt_claims['requesting_organization']).is_equal_to_ignoring_case(actual_jwt_claims['requesting_organization'])
        assert_that(expected_jwt_claims['requesting_system']).is_equal_to_ignoring_case(actual_jwt_claims['requesting_system'])
        assert_that(expected_jwt_claims['requesting_user']).is_equal_to_ignoring_case(actual_jwt_claims['requesting_user'])
        assert_that(expected_jwt_claims['sub']).is_equal_to_ignoring_case(actual_jwt_claims['sub'])
        assert_that(expected_jwt_claims['iss']).is_equal_to_ignoring_case(actual_jwt_claims['iss'])
        assert_that(expected_jwt_claims['aud']).is_equal_to_ignoring_case(actual_jwt_claims['aud'])

    @pytest.mark.happy_path
    @pytest.mark.integration
    @pytest.mark.smoke
    def test_status_get(self):
        # Given
        expected_status_code = 200
        # When
        response = requests.get(
            url=config.REASONABLE_ADJUSTMENTS_STATUS,
            headers={
                'apikey': config.STATUS_APIKEY
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.integration
    def test_ping(self):
        # Given
        expected_status_code = 200
        expected_content_type = 'application/json'

        # When
        response = requests.get(url=config.REASONABLE_ADJUSTMENTS_PING)

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)
        assert_that(expected_content_type).is_equal_to(response.headers['content-type'])
