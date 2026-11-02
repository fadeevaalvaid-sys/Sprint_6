
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
