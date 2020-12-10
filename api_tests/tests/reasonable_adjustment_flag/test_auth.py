import pytest
import requests
import uuid
from assertpy import assert_that

from api_tests.config_files import config


@pytest.mark.usefixtures("setup")
class TestAuthCasesSuite:
    """ A test suite to verify all the happy path oauth endpoints """

    existing_patient = '5900008142'
    nhsd_session_urid = '093895563513'

    @pytest.mark.integration
    @pytest.mark.smoke
    @pytest.mark.usefixtures('get_token_internal_dev')
    def test_asid_auth(self):
        # Given
        expected_status_code = 200

        # When
        response = requests.get(
            url=config.REASONABLE_ADJUSTMENTS_CONSENT,
            params={
                'patient': self.existing_patient,
                'category': 'https://fhir.nhs.uk/STU3/CodeSystem/RARecord-FlagCategory-1|NRAF',
                'status': 'active'
            },
            headers={
                'Authorization': f'Bearer {self.token}',
                'nhsd-session-urid': self.nhsd_session_urid,
                'x-request-id': str(uuid.uuid4()),
                'accept': 'application/json'
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

