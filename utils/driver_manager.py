import os
import platform

from selenium import webdriver


# Класс для хранения драйвера
class Driver:

    instance = None

    chrome_driver_by_os = {
        'Darwin': 'drivers/chromedriver_mac64',
        'Linux': 'drivers/chromedriver_linux64.exe',
        'Windows': 'drivers/chromedriver_win32.exe'
    }

    firefox_driver_by_os = {
        'Darwin': 'drivers/geckodriver_mac64',
        'Linux': 'drivers/geckodriver_linux64',
        'Windows': 'drivers/geckodriver_win32.exe'
    }

    @classmethod
    def get_instance(cls):
        return cls.instance

    @classmethod
    def new_instance(cls, browser_name):
        path = os.path.dirname(os.path.abspath(__file__)).split('utils')[0]
        os_name = platform.system()

        if browser_name == 'chrome':
            cls.instance = webdriver.Chrome(executable_path=path + cls.chrome_driver_by_os[os_name])
        elif browser_name == 'firefox':
            cls.instance = webdriver.Firefox(executable_path=path + cls.firefox_driver_by_os[os_name])
        else:
            AssertionError('Неизвестный браузер!')
        return cls.instance



