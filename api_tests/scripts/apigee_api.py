from api_tests.scripts.generic_request import GenericRequest
from api_tests.config_files.config import APIGEE_API_URL, APIGEE_AUTHENTICATION, APIGEE_ENVIRONMENT, APIGEE_USERNAME, \
    APIGEE_PASSWORD
import json
import uuid
import base64


class ApigeeDebugApi(GenericRequest):
    def __init__(self, proxy: str):
        super(ApigeeDebugApi, self).__init__()
        self.session_name = self._generate_uuid()
        self.proxy = proxy

        # Temporary fix until we create a way to get apigee tokens
        # https://docs.apigee.com/api-platform/system-administration/using-gettoken

        if APIGEE_USERNAME != '' and APIGEE_PASSWORD != '':
            token = base64.b64encode(f'{APIGEE_USERNAME}:{APIGEE_PASSWORD}'.encode('ascii'))
            self.headers = {'Authorization': f'Basic {token.decode("ascii")}'}
        elif APIGEE_AUTHENTICATION != '':
            self.headers = {'Authorization': f'Bearer {APIGEE_AUTHENTICATION}'}
        else:
            raise Exception("None of apigee authentication methods is provided. If you're running this remotely you \
                must provide APIGEE_AUTHENTICATION otherwise provide APIGEE_USERNAME and APIGEE_PASSWORD")

        self.revision = self._get_latest_revision()
        self.create_debug_session()

    @staticmethod
    def _generate_uuid():
        unique_id = uuid.uuid4()
        return str(unique_id)

    def _get_latest_revision(self) -> str:
        url = f"{APIGEE_API_URL}/apis/{self.proxy}/revisions"

        response = self.get(url, headers=self.headers)
        revisions = response.json()
        return revisions[-1]

    def create_debug_session(self):
        url = f"{APIGEE_API_URL}/environments/{APIGEE_ENVIRONMENT}/apis/{self.proxy}/revisions/{self.revision}/" \
              f"debugsessions?session={self.session_name}"

        response = self.post(url, headers=self.headers)

        assert self.check_status_code(response, 201), f"Unable to create apigee debug session {self.session_name}"

    def _get_transaction_id(self) -> str:
        url = f"{APIGEE_API_URL}/environments/{APIGEE_ENVIRONMENT}/apis/{self.proxy}/revisions/{self.revision}/" \
              f"debugsessions/{self.session_name}/data"

        response = self.get(url, headers=self.headers)
        assert self.check_status_code(response, 200), f"Unable to get apigee transaction id for {self.session_name}"
        return response.text.strip('[]').replace("\"", "").strip().split(', ')[0]

    def _get_transaction_data(self) -> dict:
        transaction_id = self._get_transaction_id()
        url = f"{APIGEE_API_URL}/environments/{APIGEE_ENVIRONMENT}/apis/{self.proxy}/revisions/{self.revision}/" \
              f"debugsessions/{self.session_name}/data/{transaction_id}"

        response = self.get(url, headers=self.headers)
        assert self.check_status_code(response, 200), f"Unable to get apigee transaction {transaction_id}"

        return json.loads(response.text)

    def get_apigee_variable(self, name: str) -> str:
        data = self._get_transaction_data()
        executions = [x.get('results', None) for x in data['point'] if x.get('id', "") == "Execution"]
        executions = list(filter(lambda x: x != [], executions))

        variable_accesses = []

        for execution in executions:
            for item in execution:
                if item.get('ActionResult', '') == 'VariableAccess':
                    variable_accesses.append(item)

        for result in variable_accesses:  # Configured by the application
            for item in result['accessList']:
                if item.get('Get', {}).get('name', '') == name:
                    return item.get('Get', {}).get('value', '')
