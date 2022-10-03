from enum import Enum


class Names(Enum):
    NEW_FOLDER = "New_Folder2"


class Path(Enum):
    UPLOAD_FILE = "/Users/denis/Desktop/upload.txt"
    CORRECT_TEXT = "This is file for upload on Yandex Drive."


class Links(Enum):
    MAIN_LINK = "http://yandex.ru"
    DISK_LINK = "https://disk.yandex.ru/client/disk"


class AuthData(Enum):
    login = "testtaskqa@yandex.ru"
    password = "Ytrewq00"
