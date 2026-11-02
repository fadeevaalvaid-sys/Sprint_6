
import allure

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Перейти по адресу {url}")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить список открытых вкладок")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Найти видимый элемент")
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти кликабельный элемент")
    def find_clickable_element(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        self.find_clickable_element(locator).click()

    @allure.step("Ввести текст в поле")
    def send_keys(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step("Нажать Escape в поле")
    def press_escape(self, locator):
        self.find_element(locator).send_keys(Keys.ESCAPE)

    @allure.step("Получить значение атрибута элемента")
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    @allure.step("Дождаться нужного значения атрибута")
    def wait_for_attribute_value(self, locator, attribute, value):
        return self.wait.until(
            lambda driver: driver.find_element(
                *locator
            ).get_attribute(attribute) == value
        )

    @allure.step("Дождаться изменения атрибута элемента")
    def wait_for_attribute(self, locator, attribute, value):
        return self.wait.until(
            EC.text_to_be_present_in_element_attribute(
                locator,
                attribute,
                value
            )
        )

    @allure.step("Дождаться исчезновения элемента")
    def wait_until_invisible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Проверить, выбран ли элемент")
    def is_selected(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        return element.is_selected()

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    @allure.step("Нажать на последний доступный элемент")
    def click_last_available(self, locator):
        elements = self.wait.until(
            lambda driver: [
                element
                for element in driver.find_elements(*locator)
                if element.is_displayed() and element.is_enabled()
            ]
        )
        elements[-1].click()

    @allure.step("Дождаться открытия новой вкладки")
    def wait_for_new_window(self, old_windows):
        self.wait.until(
            EC.number_of_windows_to_be(len(old_windows) + 1)
        )

        new_window = [
            window
            for window in self.get_window_handles()
            if window not in old_windows
        ][0]

        self.driver.switch_to.window(new_window)

    @allure.step("Дождаться перехода на страницу {url}")
    def wait_for_url(self, url):
        self.wait.until(
            EC.url_contains(url)
        )
