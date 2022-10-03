from src.back.constants import Files


def test(client):
    response = client.create_folder(Files.NEW_FOLDER_1.value)
    assert response.ok, f"error status code - {response.status_code}"

    response = client.copy_file(Files.FILE_FOR_COPY.value, Files.NEW_FOLDER_1.value)
    assert response.ok, f"error status code - {response.status_code}"

    response = client.rename_file(Files.FILE_FOR_COPY.value, Files.NAME_COPY_FILE.value, Files.NEW_FOLDER_1.value)
    assert response.ok, f"error status code - {response.status_code}"

    response = client.delete_file(Files.DELETE_FILE.value)
    assert response.ok, f"error status code - {response.status_code}"
