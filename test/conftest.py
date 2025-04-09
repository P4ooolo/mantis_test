import pytest
from fixture.application import Application
import json
import os.path


fixture = None
target = None

def load_confiq(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    confiq = load_confiq(request.config.getoption("--target"))
    if fixture is None or not fixture.is_valid():
        fixture = Application(
            browser=browser,
            base_url=confiq["web"]['baseUrl'],
            username=confiq["webadmin"]["username"],
            password=confiq["webadmin"]["password"]
        )
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
