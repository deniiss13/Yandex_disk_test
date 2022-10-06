from selenium.webdriver.common.by import By


class MainPageSelectors:
    ENTER_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".zen-ui-button-text__text")


class LoginPageSelectors:
    SIGNIN_BUTTON_LOG = (By.ID, "passp:sign-in")
    LOGIN_FIELD = (By.ID, "passp-field-login")
    PSWD_FIELD = (By.ID, "passp-field-passwd")


class DiskPageSelectors:
    COPY_ITEM = (By.CSS_SELECTOR, ".listing__items :nth-child(2)")
    COPY_BUTTON = (By.CSS_SELECTOR, ".groupable-buttons :nth-child(4) :nth-child(1)")
    NEW_FOLDER = (By.XPATH, "//div[@title = 'NewFolder']")
    COPY_BUTTON_WINDOW = (By.CSS_SELECTOR, ".confirmation-dialog__button_submit")
    DRAG_ITEM = (By.CSS_SELECTOR, ".listing__items :nth-child(2)")
    DROP_ITEM = (By.CSS_SELECTOR, ".listing__items :nth-child(3)")
    FOLDER = (By.CSS_SELECTOR, ".listing__items :nth-child(1)")
    DELETE_ITEM = (By.CSS_SELECTOR, ".listing__items :nth-child(1)")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".groupable-buttons :nth-child(3) :nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".PSHeader-User")
    USER_EXIT = (By.CSS_SELECTOR, ".legouser__menu-item_action_exit")
    CREATE = (By.CSS_SELECTOR, ".create-resource-popup-with-anchor")
    ADD_FOLDER = (By.CSS_SELECTOR, ".create-resource-popup-with-anchor__create-items :nth-child(1)")
    NAME_FIELD = (By.CSS_SELECTOR, ".Textinput.Textinput_view_default :nth-child(1)")
    UPLOAD_FIELD = (By.CSS_SELECTOR, ".upload-button__attach")
    TEXT_IN_FILE = (By.XPATH, " //p[text()='This is file for upload on Yandex Drive.'] ")

