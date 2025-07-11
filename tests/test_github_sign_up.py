import pytest
from selene import browser
from tests import conftest


# Задание 1. Скипаем тесты по возвращаему фикстурой значению

def test_desktop_sing_up_skip(setup_browser):
    if setup_browser == 'Mobile':
        pytest.skip(reason='Запуск теста возможен только с десктопным разрешением.')

    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_mobile_sign_up_skip(setup_browser):
    if setup_browser == 'Desktop':
        pytest.skip(reason='Запуск теста возможен только с мобильным разрешением.')

    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()


# Задание 2. Переопределяем набор параметризованных значений

@pytest.mark.parametrize('desktop_browser', [(1920, 1080)], indirect=True, ids=['FullHD'])
def test_desktop_sing_up_reparam(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').click()


@pytest.mark.parametrize('mobile_browser', [(360, 800)], indirect=True, ids=['IphoneProMaxUltra'])
def test_mobile_sing_up_reparam(mobile_browser):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()

# Задание 3. Разные фикстуры, без переопределения.

def test_desktop_sing_up_own_fixture(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_mobile_sing_up_own_fixture(mobile_browser):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()