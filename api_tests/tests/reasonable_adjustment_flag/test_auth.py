import pytest
import requests
import uuid
from assertpy import assert_that

from api_tests.config_files import config
from api_tests.tests.utils import Utils
from api_tests.tests.reasonable_adjustment_flag.request_bodies import *


@pytest.mark.usefixtures("setup")
class TestAuthCasesSuite:
    """ A test suite to verify all the happy path oauth endpoints """

    existing_patient = '5900008142'
    nhsd_session_urid = '093895563513'

    @pytest.mark.auth
    @pytest.mark.integration
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_auth_consent_post(self):
        # Given
        expected_status_code = 200

        # When
        response = requests.post(
            url=config.REASONABLE_ADJUSTMENTS_CONSENT,
            json=POST_Consent,
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': self.nhsd_session_urid,
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/json',
                'accept': 'application/fhir+json',
            }
        )
        print(response.text)

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.auth
    @pytest.mark.integration
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_consent_put(self):
        # Given
        expected_status_code = 200
        etag = Utils.get_etag(self,
                              config.REASONABLE_ADJUSTMENTS_CONSENT,
                              params={
                                  'patient': self.existing_patient,
                                  'category': 'https://fhir.nhs.uk/STU3/CodeSystem/RARecord-FlagCategory-1|NRAF',
                                  'status': 'active'
                              })

        # When
        print(etag)
        response = requests.put(
            url=config.REASONABLE_ADJUSTMENTS_CONSENT + '/ccc2f403-ba16-4ca7-9f79-8bd4aaaf1c9b',
            # params={
            #     'patient': '9999999998',
            #     'category': 'test',
            #     'status': 'test'
            # },
            data=json.dumps(PUT_Consent),
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': self.nhsd_session_urid,
                'x-request-id': str(uuid.uuid4()),
                'If-Match': '533acf5104b93ddfb372c56cce2968feb16fb85a',
                # 'If-Match': '*',
                'content-type': 'application/json',
                'accept': 'application/fhir+json',
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_flag_post(self):
        # Given
        expected_status_code = 201

        # When
        response = requests.post(
            url=config.REASONABLE_ADJUSTMENTS_FLAG,
            # params={
            #     'patient': '9999999998',
            #     'code': 'test',
            #     'status': 'test'
            # },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': self.nhsd_session_urid,
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/json',
                'accept': 'application/fhir+json',
            },
            json=POST_Flag,
        )

        print(response.text)
        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.happy_path
    @pytest.mark.integration
    @pytest.mark.sandbox
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_remove_ra_record_post(self):
        # Given
        expected_status_code = 200

        # When
        response = requests.post(
            url=config.REASONABLE_ADJUSTMENTS_REMOVE_RA_RECORD,
            # params={
            #     'patient': '9999999998',
            #     'removalReason': 'test',
            #     'supportingComment': 'test',
            # },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': 'test',
                'x-request-id': str(uuid.uuid4()),
                'content-type': 'application/fhir+json',
            },
            json=POST_raremoverecord,
        )
        print(response.text)

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)
