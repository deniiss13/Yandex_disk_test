import json

from src.back.constants import Files


def test_files_operations(client):
    response = client.create_folder(Files.NEW_FOLDER_1.value)
    assert response.reason == "CREATED", f"error reason - {response.reason}"
    assert response.status_code == 201,  f"error status code {response.status_code}"

    response = client.copy_file(Files.FILE_FOR_COPY.value, Files.NEW_FOLDER_1.value)
    assert response.reason == "CREATED", f"error reason - {response.reason}"
    assert response.status_code == 201, f"error status code {response.status_code}"

    response = client.rename_file(Files.FILE_FOR_COPY.value, Files.NAME_COPY_FILE.value, Files.NEW_FOLDER_1.value)
    assert response.reason == "CREATED", f"error reason - {response.reason}"
    assert response.status_code == 201, f"error status code {response.status_code}"
    files = client.get_files()
    file_names = [i["name"] for i in json.loads(files.text)["items"]]
    assert Files.NAME_COPY_FILE.value in file_names, ""

    response = client.delete_file(Files.DELETE_FILE.value)
    assert response.reason == "NO CONTENT", f"error reason - {response.reason}"
    assert response.status_code == 204, f"error status code {response.status_code}"
