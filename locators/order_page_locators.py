
from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая форма — данные клиента
    FIRST_NAME = (
        By.CSS_SELECTOR,
        "input[placeholder='* Имя']"
    )

    LAST_NAME = (
        By.CSS_SELECTOR,
        "input[placeholder='* Фамилия']"
    )

    ADDRESS = (
        By.CSS_SELECTOR,
        "input[placeholder='* Адрес: куда привезти заказ']"
    )

    METRO = (
        By.CSS_SELECTOR,
        "input[placeholder='* Станция метро']"
    )

    METRO_OPTION = (
        By.XPATH,
        "//*[contains(@class, 'select-search__option') and normalize-space()='{}']"
    )

    PHONE = (
        By.CSS_SELECTOR,
        "input[placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    # Вторая форма — параметры аренды
    DELIVERY_DATE = (
        By.CSS_SELECTOR,
        "input[placeholder='* Когда привезти самокат']"
    )

    CALENDAR = (
        By.CSS_SELECTOR,
        ".react-datepicker"
    )

    RENTAL_PERIOD = (
        By.CSS_SELECTOR,
        "div.Dropdown-control"
    )

    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        "//div[@role='option' and normalize-space()='{}']"
    )

    BLACK_SCOOTER = (
        By.ID,
        "black"
    )

    GREY_SCOOTER = (
        By.ID,
        "grey"
    )

    COMMENT = (
        By.CSS_SELECTOR,
        "input[placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать']"
    )

    # Окно подтверждения заказа
    CONFIRMATION_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Хотите оформить заказ?')]"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]//button[text()='Да']"
    )

    # Окно успешного оформления
    SUCCESS_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'Order_Text')]"
    )
