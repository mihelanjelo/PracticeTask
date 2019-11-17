import pytest

from allure_commons._allure import story, feature
from page_objects.login_page import LoginPage
from utils.driver_manager import Driver


@feature('Тестирование авторизации')
class TestLogin:

    @classmethod
    def teardown_class(cls):
        Driver.get_instance().quit()

    @story('Проверка невозможности входа для незарегистрированного пользователя')
    @pytest.mark.parametrize('browser', ['chrome'])
    def test_try_login1(self, browser):
        driver = Driver().new_instance(browser)
        driver.get('https://www.kickico.com/ru/signin')
        page = LoginPage()
        page.is_page_opened()
        page.is_visible("поле ввода емейла")
        page.is_visible("поле ввода пароля")
        page.send_text_to("поле ввода емейла", 'test@gmail.com')
        page.send_text_to("поле ввода пароля", 'test')
        page.click_at('кнопка "Вход"')
        page.is_visible('сообщение о неверном емейле или пароле')

    @story('Проверка невозможности входа при пустом поле ввода пароля')
    @pytest.mark.parametrize('browser', ['chrome', 'firefox'])
    def test_try_login_empty_password(self, browser):
        driver = Driver().new_instance(browser)
        driver.get('https://www.kickico.com/ru/signin')
        page = LoginPage()
        page.is_page_opened()
        page.is_visible("поле ввода емейла")
        page.is_visible("поле ввода пароля")
        page.send_text_to("поле ввода емейла", 'test@gmail.com')
        page.click_at('кнопка "Вход"')
        page.is_visible('сообщение о необходимости ввести пароль')

    @story('Проверка невозможности входа при пустом поле ввода email')
    @pytest.mark.parametrize('browser', ['chrome', 'firefox'])
    def test_try_login_empty_email(self, browser):
        driver = Driver().new_instance(browser)
        driver.get('https://www.kickico.com/ru/signin')
        page = LoginPage()
        page.is_page_opened()
        page.is_visible("поле ввода емейла")
        page.is_visible("поле ввода пароля")
        page.send_text_to("поле ввода пароля", 'test')
        page.click_at('кнопка "Вход"')
        page.is_visible('сообщение о необходимости ввести email')