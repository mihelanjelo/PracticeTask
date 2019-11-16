import time
from typing import List

import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from utils.actions import BasicActions
from utils.driver_manager import Driver
from utils.logger import Logger


# Базовый класс для объектов страниц с часто используемыми методами
class BasePage:
    def __init__(self):
        self.driver = Driver.get_instance()
        self.basic_actions = BasicActions(self.driver)
        self.logger = Logger.get_instance()

    PAGE_TITLE = None

    LOCATORS = {
        "example locator": (By.XPATH, "//button[@class='green button']"),
    }

    XPATH_PATTERNS = {
        "example pattern": "//div[text()='{text}']"
    }

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            allure.attach('Скриншот', Driver.get_instance().get_screenshot_as_png(), type=AttachmentType.PNG)

    def is_page_opened(self, waiting_time=10):
        step_name = f'Открыта страница {self.PAGE_TITLE}'
        self.logger.info(step_name)
        with step(step_name):
            for i in range(0, waiting_time + 1):
                if self.driver.title == self.PAGE_TITLE:
                    return True
                elif i == waiting_time:
                    return False
                else:
                    time.sleep(1)
    
    def is_visible(self, locator_name, time_waiting_element=10, values=None) -> bool:
        step_name = f'Появится {locator_name}'
        self.logger.info(step_name)
        with step(step_name):
            if not values:
                return self.basic_actions.is_element_visible(self.LOCATORS[locator_name], time_waiting_element)
            else:
                locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
                return self.basic_actions.is_element_visible(locator, time_waiting_element)
    
    def is_not_visible(self, locator_name: object, time_waiting_element: object = 0, values: object = None) -> bool:
        step_name = f'Исчезнет {locator_name}'
        self.logger.info(step_name)
        with step(step_name):
            if not values:
                return self.basic_actions.wait_element_hiding(self.LOCATORS[locator_name], time_waiting_element)
            else:
                locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
                return self.basic_actions.wait_element_hiding(locator, time_waiting_element)

    def click_at(self, locator_name, time_waiting_element=10, values=None, offset=None):
        step_name = f'Нажать на {locator_name}'
        self.logger.info(step_name)
        with step(step_name):
            if not offset:
                if not values:
                    self.basic_actions.click_on_element(self.LOCATORS[locator_name], time_waiting_element)
                else:
                    locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
                    self.basic_actions.click_on_element(locator, time_waiting_element)
            else:
                if not values:
                    el = self.basic_actions.wait_element(self.LOCATORS[locator_name], time_waiting_element)
                    action = webdriver.common.action_chains.ActionChains(self.driver)
                    action.move_to_element_with_offset(el, offset['x'], offset['y'])
                    action.click()
                    action.perform()
                else:
                    locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
                    el = self.basic_actions.wait_element(locator, time_waiting_element)
                    action = webdriver.common.action_chains.ActionChains(self.driver)
                    action.move_to_element_with_offset(el, offset['x'], offset['y'])
                    action.click()
                    action.perform()

    def get_text_from(self, locator_name, time_waiting_element=10, values: object = None) -> str:
        step_name = f'Получить текст из {locator_name}'
        self.logger.info(step_name)
        with step(step_name):
            if not values:
                locator = self.LOCATORS[locator_name]
            else:
                locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))

            if 'input' in locator[1] or 'textarea' in locator[1]:
                return self.basic_actions.wait_element(locator, time_waiting_element). \
                    get_attribute('value')
            else:
                return self.basic_actions.get_text_from_element(locator, time_waiting_element)

    def get_text_from_every(self, locator_name, time_waiting_element=10) -> List[str]:
        step_name = f'Получить текст из каждого {locator_name}'
        self.logger.info(step_name)
        with step(step_name):
            return self.basic_actions.get_text_from_elements(self.LOCATORS[locator_name], time_waiting_element)

    def send_text_to(self, locator_name, text, time_waiting_element=10, values=None):
        step_name = f'Ввести текст "{text}" в {locator_name}'
        self.logger.info(step_name)
        with step(step_name):
            if not values:
                self.basic_actions.send_text_to_element(text, self.LOCATORS[locator_name], time_waiting_element)
            else:
                locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
                self.basic_actions.send_text_to_element(text, locator, time_waiting_element)

    def clear(self, locator_name, time_waiting_element=10):
        self.basic_actions.wait_element(self.LOCATORS[locator_name], time_waiting_element).clear()
    
    def select_item(self, locator_name, value, time_waiting_element=10):
        self.basic_actions.select_item_by_text(value, self.LOCATORS[locator_name], time_waiting_element)

    def get_elements(self, locator_name, time_waiting_element=10, values=None) -> List[WebElement]:
        if not values:
            return self.basic_actions.wait_elements(self.LOCATORS[locator_name], time_waiting_element)
        else:
            locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
            return self.basic_actions.wait_elements(locator, time_waiting_element)
    
    def get_element(self, locator_name, time_waiting_element=10, values=None) -> WebElement:
        if not values:
            return self.basic_actions.wait_element(self.LOCATORS[locator_name], time_waiting_element)
        else:
            locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
            return self.basic_actions.wait_element(locator, time_waiting_element)
