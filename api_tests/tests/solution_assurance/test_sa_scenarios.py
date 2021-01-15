import os

import pytest
import requests
from assertpy import assert_that

from api_tests.config_files import config

home_dir = os.environ.get("HOME")
cert_path = os.environ.get("CERT_PATH")
cert_path = cert_path or (home_dir + "/.mitmproxy/mitmproxy-ca-cert.pem")

mitmproxy_url = os.environ.get("MITMPROXY_URL") or "http://127.0.0.1:8080"
proxies = {
    "http": mitmproxy_url,
    "https": mitmproxy_url
}


class TestSaCasesSuite:

    @pytest.mark.solution_assurance
    def test_ra_api_cs_024(self):
        # Given
        expected_status_code = 500

        # When
        response = requests.post(
            proxies=proxies,
            verify=cert_path,
            url=config.REASONABLE_ADJUSTMENTS_FLAG,
            headers={
                'Test-Scenario-Id': 'RA-API-CS-024',
            }
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.solution_assurance
    def test_ra_api_cs_025(self):
        # Given
        expected_status_code = 500

        # When
        response = requests.post(
            proxies=proxies,
            verify=cert_path,
            url=config.REASONABLE_ADJUSTMENTS_FLAG,
            headers={
                'Test-Scenario-Id': 'RA-API-CS-025',
            },
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.solution_assurance
    def test_ra_api_cs_033(self):
        # Given
        expected_status_code = 500

        # When
        response = requests.put(
            proxies=proxies,
            verify=cert_path,
            url=config.REASONABLE_ADJUSTMENTS_FLAG,
            headers={
                'Test-Scenario-Id': 'RA-API-CS-033',
            },
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)


    @pytest.mark.solution_assurance
    def test_ra_api_cs_034(self):
        # Given
        expected_status_code = 500

        # When
        response = requests.put(
            proxies=proxies,
            verify=cert_path,
            url=config.REASONABLE_ADJUSTMENTS_FLAG,
            headers={
                'Test-Scenario-Id': 'RA-API-CS-034',
            },
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.solution_assurance
    def test_ra_api_cs_040(self):
        # Given
        expected_status_code = 500

        # When
        response = requests.put(
            proxies=proxies,
            verify=cert_path,
            url=config.REASONABLE_ADJUSTMENTS_REMOVE_RA_RECORD,
            headers={
                'Test-Scenario-Id': 'RA-API-CS-040',
            },
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.solution_assurance
    def test_ra_api_cs_041(self):
        # Given
        expected_status_code = 500

        # When
        response = requests.put(
            proxies=proxies,
            verify=cert_path,
            url=config.REASONABLE_ADJUSTMENTS_REMOVE_RA_RECORD,
            headers={
                'Test-Scenario-Id': 'RA-API-CS-041',
            },
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)

    @pytest.mark.solution_assurance
    def test_ra_api_cs_043(self):
        # Given
        expected_status_code = 500

        # When
        response = requests.put(
            proxies=proxies,
            verify=cert_path,
            url=config.REASONABLE_ADJUSTMENTS_REMOVE_RA_RECORD,
            headers={
                'Test-Scenario-Id': 'RA-API-CS-043',
            },
        )

        # Then
        assert_that(expected_status_code).is_equal_to(response.status_code)
