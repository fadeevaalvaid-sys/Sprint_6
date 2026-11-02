
import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL, DZEN_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.go_to_url(MAIN_PAGE_URL)

    @allure.step("Получить ответ на вопрос FAQ")
    def get_faq_answer(self, question_id):
        question_locator = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(question_id)
        )

        answer_locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(question_id)
        )

        self.scroll_to_element(question_locator)

        if self.get_attribute(
            question_locator,
            "aria-expanded"
        ) == "true":
            self.click_element(question_locator)

            self.wait_for_attribute(
                question_locator,
                "aria-expanded",
                "false"
            )

        self.click_element(question_locator)

        self.wait_for_attribute(
            question_locator,
            "aria-expanded",
            "true"
        )

        answer = self.find_element(answer_locator)

        return answer.text

    @allure.step("Нажать кнопку Заказать")
    def click_order_button(self, entry_point):
        if entry_point == "top":
            self.click_element(
                MainPageLocators.ORDER_BUTTON_TOP
            )
        else:
            self.scroll_to_element(
                MainPageLocators.ORDER_BUTTON_BOTTOM
            )
            self.click_element(
                MainPageLocators.ORDER_BUTTON_BOTTOM
            )

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        old_windows = self.get_window_handles()

        self.click_element(MainPageLocators.YANDEX_LOGO)

        self.wait_for_new_window(old_windows)

        self.wait_for_url(DZEN_URL)

    @allure.step("Проверить, что открыта главная страница Самоката")
    def is_main_page_opened(self):
        return self.get_current_url() == MAIN_PAGE_URL

    @allure.step("Проверить, что открыта страница Дзена")
    def is_dzen_opened(self):
        return DZEN_URL in self.get_current_url()
