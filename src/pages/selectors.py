from enum import Enum


class MainPageSelectors(Enum):
    ENTER_BUTTON_CLASS = ".zen-ui-button-text__text"


class LoginPageSelectors(Enum):
    SIGNIN_BUTTON_LOG = "passp:sign-in"
    LOGIN_FIELD = "passp-field-login"
    PSWD_FIELD = "passp-field-passwd"


class DiskPageSelectors(Enum):
    COPY_ITEM = ".listing__items :nth-child(2)"
    COPY_BUTTON = ".groupable-buttons :nth-child(4) :nth-child(1)"
    NEW_FOLDER = "//div[@title = 'NewFolder']"
    COPY_BUTTON_WINDOW = ".confirmation-dialog__button_submit"
    DRAG_ITEM = ".listing__items :nth-child(2)"
    DROP_ITEM = ".listing__items :nth-child(3)"
    FOLDER = ".listing__items :nth-child(1)"
    DELETE_ITEM = ".listing__items :nth-child(1)"
    DELETE_BUTTON = ".groupable-buttons :nth-child(3) :nth-child(1)"
    USER_ICON = ".PSHeader-User"
    USER_EXIT = ".legouser__menu-item_action_exit"
    CREATE = ".create-resource-popup-with-anchor"
    ADD_FOLDER = ".create-resource-popup-with-anchor__create-items :nth-child(1)"
    NAME_FIELD = ".Textinput.Textinput_view_default :nth-child(1)"
    UPLOAD_FIELD = ".upload-button__attach"
    TEXT_IN_FILE = " //p[text()='This is file for upload on Yandex Drive.'] "
