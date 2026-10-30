
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открывает главную страницу Самоката."""
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def get_faq_answer(self, question_id):
        """Открывает вопрос FAQ и возвращает текст ответа."""

        question_locator = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(question_id)
        )

        answer_locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(question_id)
        )

        question = self.wait.until(
            EC.visibility_of_element_located(question_locator)
        )

        # Прокручиваем страницу к нужному вопросу
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            question
        )

        question = self.wait.until(
            EC.element_to_be_clickable(question_locator)
        )

        # Если вопрос уже открыт, закрываем его
        if question.get_attribute("aria-expanded") == "true":
            question.click()

            self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    question_locator,
                    "aria-expanded",
                    "false"
                )
            )

        # Открываем вопрос
        question = self.wait.until(
            EC.element_to_be_clickable(question_locator)
        )
        question.click()

        self.wait.until(
            EC.text_to_be_present_in_element_attribute(
                question_locator,
                "aria-expanded",
                "true"
            )
        )

        answer = self.wait.until(
            EC.visibility_of_element_located(answer_locator)
        )

        return answer.text

    def click_order_button_top(self):
        """Нажимает верхнюю кнопку Заказать."""
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.ORDER_BUTTON_TOP
            )
        ).click()

    def click_order_button_bottom(self):
        """Прокручивает страницу вниз и нажимает нижнюю кнопку Заказать."""

        button = self.wait.until(
            EC.presence_of_element_located(
                MainPageLocators.ORDER_BUTTON_BOTTOM
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.ORDER_BUTTON_BOTTOM
            )
        ).click()

    def click_scooter_logo(self):
        """Нажимает на логотип Самоката."""
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.SCOOTER_LOGO
            )
        ).click()

    def click_yandex_logo(self):
        """Нажимает на логотип Яндекса и переключается на новую вкладку."""

        old_windows = self.driver.window_handles

        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.YANDEX_LOGO
            )
        ).click()

        self.wait.until(
            EC.number_of_windows_to_be(len(old_windows) + 1)
        )

        new_window = [
            window
            for window in self.driver.window_handles
            if window not in old_windows
        ][0]

        self.driver.switch_to.window(new_window)

        self.wait.until(
            EC.url_contains("dzen.ru")
        )
