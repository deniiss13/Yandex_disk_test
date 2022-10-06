from .constants import AUTH
import requests
import json


class Client:

    @staticmethod
    def get_files(limit: int = 20, file_type: str = "text", offset=0):
        response = requests.get(f"https://cloud-api.yandex.net/v1/disk/resources/files?limit={limit}", headers=AUTH)
        assert response.ok, f"{response.status_code}"
        return response

    @staticmethod
    def create_folder(name):
        response = requests.put(rf"https://cloud-api.yandex.net/v1/disk/resources?path=%2F{name}", headers=AUTH)

        assert response.ok, f"{response.status_code}"
        return response

    @staticmethod
    def copy_file(name, location):
        response = requests.post(
            rf"https://cloud-api.yandex.net/v1/disk/resources/copy?from=%2F{name}&path=%2F{location}%2F{name}",
            headers=AUTH)
        assert response.ok, f"{response.status_code}"
        return response

    @staticmethod
    def rename_file(name, new_name, location):
        return requests.post(
         rf"https://cloud-api.yandex.net/v1/disk/resources/copy?from=%2F{location}%2F{name}&path=%2F{location}%2F{new_name}&overwrite=true",
         headers=AUTH
        )

    @staticmethod
    def delete_file(path):
        return requests.delete(rf"https://cloud-api.yandex.net/v1/disk/resources?path=%2F{path}&permanently=false",
                               headers=AUTH)
