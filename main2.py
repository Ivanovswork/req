import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url_to_upload = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = {'Content-type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        porams = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url_to_upload, headers=headers, params=porams)
        href = response.json()['href']
        r = requests.put(href, data=open(file_path, 'rb'))



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'tets_file.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)