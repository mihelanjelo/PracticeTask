from selenium.webdriver.common.by import By
from .base_page import BasePage


# Класс с элементами страницы авторизации
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

    PAGE_TITLE = "KICKICO - Вход"

    LOCATORS = {
        "поле ввода емейла": (By.ID, "UserLogin_username"),
        "поле ввода пароля": (By.ID, "UserLogin_password"),
        'кнопка "Вход"': (By.XPATH, "//input[@type='submit']"),
        'сообщение о неверном емейле или пароле': (By.XPATH, "//*[text()='Password or email is incorrect.']"),
    }
