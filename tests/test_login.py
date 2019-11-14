import pytest

from page_objects.login_page import LoginPage
from utils.driver_manager import Driver


class TestLogin:

    @classmethod
    def teardown_class(cls):
        Driver.get_instance().quit()

    @pytest.mark.parametrize('browser', ['chrome', 'firefox'])
    def test_login_success(self, browser):
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
