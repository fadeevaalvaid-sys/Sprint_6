from datetime import datetime, timedelta

import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage


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
    @allure.step("Оформить заказ через кнопку {entry_point}")
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
            main_page.click_order_button(entry_point)

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
            confirmation = order_page.get_confirmation_title()

            assert "Хотите оформить заказ?" in confirmation

        with allure.step("Подтвердить оформление заказа"):
            order_page.confirm_order()

        with allure.step("Проверить успешное оформление заказа"):
            success_message = order_page.get_success_message()

            assert "Заказ оформлен" in success_message
            assert "Номер заказа" in success_message


@allure.feature("Навигация")
class TestNavigation:

    @allure.story("Переход на главную страницу по логотипу Самоката")
    @allure.step("Проверить переход на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу Самоката"):
            main_page.open()

        with allure.step("Нажать на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить переход на главную страницу"):
            assert main_page.is_main_page_opened()

    @allure.story("Переход на главную страницу Дзена по логотипу Яндекса")
    @allure.step("Проверить переход на Дзен по логотипу Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу Самоката"):
            main_page.open()

        with allure.step("Нажать на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Проверить переход на страницу Дзена"):
            assert main_page.is_dzen_opened()