
from datetime import datetime, timedelta

import pytest
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


# Дата доставки — завтра
DELIVERY_DATE = (
    datetime.now() + timedelta(days=1)
).strftime("%d.%m.%Y")


@allure.feature("Оформление заказа")
class TestOrder:

    @pytest.mark.parametrize(
        "entry_point, first_name, last_name, address, metro, phone, rental_period, scooter_color, comment",
        [
            (
                "top",
                "Анна",
                "Иванова",
                "Москва, улица Стромынка, 1",
                "Бульвар Рокоссовского",
                "89991234567",
                "двое суток",
                "black",
                "Позвонить перед доставкой"
            ),
            (
                "bottom",
                "Пётр",
                "Петров",
                "Москва, улица Ленина, 10",
                "Бульвар Рокоссовского",
                "89997654321",
                "трое суток",
                "grey",
                "Доставить после обеда"
            )
        ]
    )
    @allure.story("Позитивный сценарий оформления заказа")
    def test_order_flow(
        self,
        driver,
        entry_point,
        first_name,
        last_name,
        address,
        metro,
        phone,
        rental_period,
        scooter_color,
        comment
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу Самоката"):
            main_page.open()

        with allure.step("Перейти к форме заказа"):
            if entry_point == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()

        with allure.step("Заполнить форму с данными клиента"):
            order_page.fill_customer_info(
                first_name,
                last_name,
                address,
                metro,
                phone
            )

        with allure.step("Заполнить параметры аренды"):
            order_page.fill_rental_details(
                DELIVERY_DATE,
                rental_period,
                scooter_color,
                comment
            )

        with allure.step("Нажать кнопку Заказать"):
            order_page.click_order_button()

        with allure.step("Проверить окно подтверждения заказа"):
            confirmation = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    OrderPageLocators.CONFIRMATION_TITLE
                )
            )

            assert "Хотите оформить заказ?" in confirmation.text

        with allure.step("Подтвердить оформление заказа"):
            order_page.confirm_order()

        with allure.step("Проверить успешное оформление заказа"):
            success_message = order_page.get_success_message()

            assert "Заказ оформлен" in success_message
            assert "Номер заказа" in success_message


@allure.feature("Навигация")
class TestNavigation:

    @allure.story("Переход на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):

        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу Самоката"):
            main_page.open()

        with allure.step("Нажать на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить переход на главную страницу"):
            WebDriverWait(driver, 10).until(
                EC.url_to_be(
                    "https://qa-scooter.praktikum-services.ru/"
                )
            )

            assert driver.current_url == (
                "https://qa-scooter.praktikum-services.ru/"
            )

    @allure.story("Переход на главную страницу Дзена по логотипу Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):

        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу Самоката"):
            main_page.open()

        with allure.step("Нажать на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Проверить переход на страницу Дзена"):
            assert "dzen.ru" in driver.current_url
