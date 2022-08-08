import unittest
import api
from task2_yandex_api import create_folder
from parameterized import parameterized

'''
коды ответов сервера
201 - папка успешно создана
409 - папка уже существует
401 - Unauthorized
'''
class TestFunctiuns(unittest.TestCase):

    @parameterized.expand(
        [
            ("photos_from_vk", 409),
            ("test_folder", 201)
        ]
    )
    def test_create_folder(self, folder_name, result):
        yadisk_token = api.yadisk_token
        c_result = create_folder(folder_name, yadisk_token)
        self.assertEqual(c_result, result)

    @unittest.expectedFailure
    def test_incorrect_token(self):
        yadisk_token = '56756786889768768'
        folder_name = 'test_token'
        c_result = create_folder(folder_name, yadisk_token)
        self.assertEqual(c_result, 401)
