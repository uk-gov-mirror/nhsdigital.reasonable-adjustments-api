from mitmproxy import http


class ScenarioManager:
    current_scenario = ''

    base_cmd_url = "http://mitm.it/cmd"
    cmd_prefix = "scenario."

    def get_scenario_from_url(self, flow: http.HTTPFlow) -> str:
        if self.is_cmd_url(flow):
            url = flow.request.pretty_url
            seg = url.split('/')

            return seg[-1][len(self.cmd_prefix):]
        else:
            return ''

    def is_cmd_url(self, flow: http.HTTPFlow) -> bool:
        return flow.request.pretty_url.startswith(self.base_cmd_url)


scenario_manager = ScenarioManager()


class ScenarioMangerAddon:
    def request(self, flow: http.HTTPFlow):
        scenario = scenario_manager.get_scenario_from_url(flow)
        if scenario != '':
            scenario_manager.current_scenario = scenario
            print(f'[+] Switch to Scenario: ${scenario}')

            flow.response = http.HTTPResponse.make(
                status_code=200,
                content=f'scenario ${scenario} has been selected'
            )


def intercept_ra_api_cs_024(flow: http.HTTPFlow):
    flow.response = http.HTTPResponse.make(
        status_code=500,
    )


def intercept_ra_api_cs_025(flow: http.HTTPFlow):
    flow.response = http.HTTPResponse.make(
        status_code=500,
    )


scenarios = [
    {
        'risk_id': 'RA-API-CS-024',
        'risk_group': 'Create a new Reasonable Adjustment Flag',
        'description': 'Connecting System fails to notify user a new Reasonable Adjustment Flag has NOT been successfully created.',
        'cause': 'Connecting system fails to correctly process response from RA API (System level)',
        'intercept': intercept_ra_api_cs_024
    },
    {
        'risk_id': 'RA-API-CS-025',
        'risk_group': 'Create a new Reasonable Adjustment Flag',
        'description': 'Connecting System fails to notify user a new Reasonable Adjustment Flag has NOT been successfully created.',
        'cause': 'Connecting system fails to correctly present the data returned from RA API (Presentation layer)',
        'intercept': intercept_ra_api_cs_025
    },
]


class SaTest:
    def __init__(self):
        self.scenario_manager = scenario_manager

    def request(self, flow):
        for scenario in scenarios:
            if (scenario_manager.current_scenario == scenario['risk_id']) and (not scenario_manager.is_cmd_url(flow)):
                self.log_scenario(scenario)
                scenario['intercept'](flow)

    def log_scenario(self, scenario):
        print(f'[+] Scenario ID: {scenario["risk_id"]}')
        print(f'     Risk Group: {scenario["risk_group"]}')
        print(f'    Description: {scenario["description"]}')
        print(f'          Cause: {scenario["cause"]}')


addons = [
    SaTest(),
    ScenarioMangerAddon(),
]
