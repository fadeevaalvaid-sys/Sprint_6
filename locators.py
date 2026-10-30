
from selenium.webdriver.common.by import By


class MainPageLocators:
    # FAQ
    FAQ_QUESTION = (
        By.CSS_SELECTOR,
        "div[id='accordion__heading-{}']"
    )

    FAQ_ANSWER = (
        By.CSS_SELECTOR,
        "div[id='accordion__panel-{}']"
    )

    # Кнопки заказа на главной странице
    ORDER_BUTTON_TOP = (
        By.CSS_SELECTOR,
        "button.Button_Button__ra12g:not(.Button_Middle__1CSJM)"
    )

    ORDER_BUTTON_BOTTOM = (
        By.CSS_SELECTOR,
        "button.Button_Button__ra12g.Button_Middle__1CSJM"
    )

    # Логотипы
    SCOOTER_LOGO = (
        By.CSS_SELECTOR,
        "a.Header_LogoScooter__3lsAR"
    )

    YANDEX_LOGO = (
        By.CSS_SELECTOR,
        "a.Header_LogoYandex__3TSOI"
    )


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

    # Вариант станции в выпадающем списке
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

    RENTAL_PERIOD = (
        By.CSS_SELECTOR,
        "div.Dropdown-control"
    )

    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        "//div[@role='option' and text()='{}']"
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
