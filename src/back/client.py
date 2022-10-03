from .constants import Token
import requests


class Client:
    @staticmethod
    def create_folder(name):
        response = requests.put(rf"https://cloud-api.yandex.net/v1/disk/resources?path=%2F{name}",
                            headers={
                                "Authorization": Token.TOKEN.value})
        return response

    @staticmethod
    def copy_file(name, location):
        return requests.post(
            rf"https://cloud-api.yandex.net/v1/disk/resources/copy?from=%2F{name}&path=%2F{location}%2F{name}",
            headers={"Authorization": Token.TOKEN.value})

    @staticmethod
    def rename_file(name, new_name, location):
        return requests.post(
        rf"https://cloud-api.yandex.net/v1/disk/resources/copy?from=%2F{location}%2F{name}&path=%2F{location}%2F{new_name}&overwrite=true",
        headers={"Authorization": Token.TOKEN.value})

    @staticmethod
    def delete_file(path):
        return requests.delete(rf"https://cloud-api.yandex.net/v1/disk/resources?path=%2F{path}&permanently=false",
                               headers={
                                   "Authorization": Token.TOKEN.value})
