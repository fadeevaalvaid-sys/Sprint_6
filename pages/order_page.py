
import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить форму данными клиента")
    def fill_customer_info(
        self, first_name, last_name, address, metro, phone
    ):
        self.send_keys(
            OrderPageLocators.FIRST_NAME,
            first_name
        )

        self.send_keys(
            OrderPageLocators.LAST_NAME,
            last_name
        )

        self.send_keys(
            OrderPageLocators.ADDRESS,
            address
        )

        self.click_element(OrderPageLocators.METRO)

        self.send_keys(
            OrderPageLocators.METRO,
            metro
        )

        metro_option = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(metro)
        )

        self.click_element(metro_option)

        self.wait_for_attribute_value(
            OrderPageLocators.METRO,
            "value",
            metro
        )

        self.send_keys(
            OrderPageLocators.PHONE,
            phone
        )

        self.click_element(OrderPageLocators.NEXT_BUTTON)

        self.find_element(OrderPageLocators.DELIVERY_DATE)

    @allure.step("Заполнить параметры аренды")
    def fill_rental_details(
        self, delivery_date, rental_period, scooter_color, comment
    ):
        self.send_keys(
            OrderPageLocators.DELIVERY_DATE,
            delivery_date
        )

        self.press_escape(OrderPageLocators.DELIVERY_DATE)

        self.click_element(OrderPageLocators.COMMENT)

        self.wait_until_invisible(
            OrderPageLocators.CALENDAR
        )

        self.click_element(OrderPageLocators.RENTAL_PERIOD)

        rental_option = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(
                rental_period
            )
        )

        self.click_element(rental_option)

        if scooter_color == "black":
            color_locator = OrderPageLocators.BLACK_SCOOTER
        else:
            color_locator = OrderPageLocators.GREY_SCOOTER

        if not self.is_selected(color_locator):
            self.click_element(color_locator)

        self.send_keys(
            OrderPageLocators.COMMENT,
            comment
        )

    @allure.step("Нажать кнопку Заказать")
    def click_order_button(self):
        self.click_last_available(
            OrderPageLocators.ORDER_BUTTON
        )

    @allure.step("Получить заголовок окна подтверждения заказа")
    def get_confirmation_title(self):
        return self.find_element(
            OrderPageLocators.CONFIRMATION_TITLE
        ).text

    @allure.step("Подтвердить оформление заказа")
    def confirm_order(self):
        self.find_element(
            OrderPageLocators.CONFIRMATION_TITLE
        )

        self.click_element(
            OrderPageLocators.CONFIRM_BUTTON
        )

    @allure.step("Получить сообщение об успешном оформлении заказа")
    def get_success_message(self):
        success_title = self.find_element(
            OrderPageLocators.SUCCESS_TITLE
        )

        success_message = self.find_element(
            OrderPageLocators.SUCCESS_MESSAGE
        )

        return success_title.text + " " + success_message.text
