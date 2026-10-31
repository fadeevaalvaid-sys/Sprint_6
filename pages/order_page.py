
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_customer_info(
        self, first_name, last_name, address, metro, phone
    ):
        """Заполняет первую форму данными клиента."""

        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.FIRST_NAME
            )
        ).send_keys(first_name)

        self.driver.find_element(
            *OrderPageLocators.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *OrderPageLocators.ADDRESS
        ).send_keys(address)

        # Открываем список станций метро
        metro_field = self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.METRO
            )
        )
        metro_field.click()

        # Находим нужную станцию в выпадающем списке
        metro_option = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(metro)
        )

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(metro_option)
        ).click()

        # Проверяем, что станция выбрана
        self.wait.until(
            lambda driver: driver.find_element(
                *OrderPageLocators.METRO
            ).get_attribute("value") == metro
        )

        self.driver.find_element(
            *OrderPageLocators.PHONE
        ).send_keys(phone)

        self.driver.find_element(
            *OrderPageLocators.NEXT_BUTTON
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.DELIVERY_DATE
            )
        )

    def fill_rental_details(
        self, delivery_date, rental_period, scooter_color, comment
    ):
        """Заполняет форму с параметрами аренды."""

        # Указываем дату доставки
        date_field = self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.DELIVERY_DATE
            )
        )

        date_field.send_keys(delivery_date)
        date_field.send_keys(Keys.ESCAPE)

        # Закрываем календарь кликом по комментарию
        comment_field = self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.COMMENT
            )
        )
        comment_field.click()

        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, ".react-datepicker")
            )
        )

        # Выбираем срок аренды
        rental_dropdown = self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.RENTAL_PERIOD
            )
        )
        rental_dropdown.click()

        rental_option = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(
                rental_period
            )
        )

        self.wait.until(
            EC.element_to_be_clickable(rental_option)
        ).click()

        # Выбираем цвет самоката
        if scooter_color == "black":
            color_locator = OrderPageLocators.BLACK_SCOOTER
        else:
            color_locator = OrderPageLocators.GREY_SCOOTER

        color_checkbox = self.driver.find_element(
            *color_locator
        )

        if not color_checkbox.is_selected():
            color_checkbox.click()

        # Заполняем комментарий
        comment_field.send_keys(comment)

    def click_order_button(self):
        """Нажимает кнопку Заказать во второй форме."""

        buttons = self.wait.until(
            lambda driver: [
                button
                for button in driver.find_elements(
                    *OrderPageLocators.ORDER_BUTTON
                )
                if button.is_displayed() and button.is_enabled()
            ]
        )

        buttons[-1].click()

    def confirm_order(self):
        """Подтверждает оформление заказа."""

        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.CONFIRMATION_TITLE
            )
        )

        self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.CONFIRM_BUTTON
            )
        ).click()

    def get_success_message(self):
        """Возвращает сообщение об успешном оформлении заказа."""

        success_title = self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.SUCCESS_TITLE
            )
        )

        success_message = self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.SUCCESS_MESSAGE
            )
        )

        return success_title.text + " " + success_message.text
