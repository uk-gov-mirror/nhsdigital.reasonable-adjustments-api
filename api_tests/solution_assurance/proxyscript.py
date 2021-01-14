from mitmproxy import http

def mitmproxy(func):
    def wrapper():
        print("first")
        func()
        print("second")

    return wrapper

@mitmproxy
def test_first():
    print("test body first")

@mitmproxy
def test_second():
    print("test body second")

class MitmproxyTestHelper:
    def request(self, flow):
        if flow.request.headers.get('TestScenario') == 'GetHelloWorld408':
            print("[+] Test GetHelloWorld408 scenario")
            # flow.kill() # This will kill the TCP socket. it's not suitable for timeout scenario
            flow.response = http.HTTPResponse.make(
                status_code=408,
                headers={"Connection": "closed"}
            )

