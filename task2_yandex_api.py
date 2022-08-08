import api
import requests
folder_name = 'photos_from_vk'


def create_folder(folder_name: str, token: str):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    dict_header = {'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    dict_params = {"path": folder_name}
    resp = requests.put(url, headers=dict_header, params=dict_params)
    return resp.status_code


if __name__ == '__main__':
    yadisk_token = api.yadisk_token
    result = create_folder(folder_name, yadisk_token)
    print(result)

