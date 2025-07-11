import pytest
from selene import browser


def readable_resolution_param_name(res):
    width, height = res
    device = 'Desktop' if width >= 1280 else 'Mobile'
    return f'{device}: {width}x{height}'


# Задание 1.

@pytest.fixture(params=[
    (1920, 1080),
    (1366, 768),
    (1536, 864),
    (1280, 720),
    (360, 800),
    (390, 844),
    (393, 873),
    (412, 915)
], ids=readable_resolution_param_name)
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield 'Desktop' if width >= 1280 else 'Mobile'
    browser.quit()


# Задание 2.

@pytest.fixture(params=[(1920, 1080), (1366, 768), (1536, 864),(1280, 720)],
                ids=readable_resolution_param_name)
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(360, 800), (390, 844), (393, 873), (412, 915)],
                ids=readable_resolution_param_name)
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()