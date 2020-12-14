import json
import uuid

import pytest
import requests
from assertpy import assert_that

from api_tests.config_files import config
from api_tests.tests.utils import Utils


@pytest.mark.usefixtures("setup")
class TestHappyCasesSuite:
    """ A test suite to verify all the happy path oauth endpoints """

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_consent_get(self):
        # Given
        expected_status_code = 200

        # When
        response = requests.get(
            url=config.REASONABLE_ADJUSTMENTS_CONSENT,
            params={
                'patient': '9999999998',
                'category': 'test',
                'status': 'test'
            },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_consent_post(self):
        # Given
        expected_status_code = 201

        # When
        response = requests.post(
            url=config.REASONABLE_ADJUSTMENTS_CONSENT,
            json=json.dumps({'message': 'test'}),
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json'
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_consent_put(self):
        # Given
        expected_status_code = 200
        etag = Utils.get_etag(self,
                              config.REASONABLE_ADJUSTMENTS_CONSENT,
                              params={
                                  'patient': '9999999998',
                                  'category': 'test',
                                  'status': 'test'
                              })

        # When
        response = requests.put(
            url=config.REASONABLE_ADJUSTMENTS_CONSENT + '/test',
            data=json.dumps({'message': 'test'}),
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json',
                'If-Match': etag
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_flag_get(self):

        # Given
        expected_status_code = 200

        # When
        response = requests.get(
            url=config.REASONABLE_ADJUSTMENTS_FLAG,
            params={
                'patient': '9999999998',
                'category': 'test',
                'status': 'test'
            },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_flag_post(self):
        # Given
        expected_status_code = 201

        # When
        response = requests.post(
            url=config.REASONABLE_ADJUSTMENTS_FLAG,
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json'
            },
            json=json.dumps({'message': 'test'})
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_flag_put(self):
        # Given
        expected_status_code = 200
        etag = Utils.get_etag(self,
                              config.REASONABLE_ADJUSTMENTS_CONSENT,
                              params={
                                  'patient': '9999999998',
                                  'category': 'test',
                                  'status': 'test',
                              })

        # When
        response = requests.put(
            url=config.REASONABLE_ADJUSTMENTS_FLAG + '/1',
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json',
                'if-match': etag,
            },
            data=json.dumps({'message': 'test'})
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_list_get(self):
        # Given
        expected_status_code = 200

        # When
        response = requests.get(
            url=config.REASONABLE_ADJUSTMENTS_LIST,
            params={
                'patient': '9999999998',
                'status': 'test',
                'code': 'test'
            },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_list_post(self):
        # Given
        expected_status_code = 201

        # When
        response = requests.post(
            url=config.REASONABLE_ADJUSTMENTS_LIST,
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json'
            },
            json=json.dumps({'message': 'test'})
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_list_put(self):
        # Given
        expected_status_code = 200
        etag = Utils.get_etag(self,
                              config.REASONABLE_ADJUSTMENTS_CONSENT,
                              params={
                                  'patient': '9999999998',
                                  'category': 'test',
                                  'status': 'test',
                              })

        # When
        response = requests.put(
            url=config.REASONABLE_ADJUSTMENTS_LIST + '/1',
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json',
                'if-match': etag,
            },
            data=json.dumps({'message': 'test'})
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_remove_ra_record_post(self):
        # Given
        expected_status_code = 200

        # When
        response = requests.post(
            url=config.REASONABLE_ADJUSTMENTS_REMOVE_RA_RECORD,
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json',
                'If-Match': 'abc123'
            },
            json=json.dumps({'message': 'test'})
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

