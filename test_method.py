from unittest import TestCase

import requests


# class TestTornadoRequest(TestCase):
#     base_url = 'http://10.36.174.13:8000'
#
#     def test_index_post(self):
#         url = self.base_url + '/'
#         # 发起post请求，表单参数
#         resp = requests.delete(url, data={
#             'name': 'leon',
#             'city': 'xian'
#         })
#         print(resp.text)

class TestUserRequest(TestCase):
    url = 'http://10.36.174.13:8000/user'

    def test_login(self):
        resp = requests.get(self.url,
                            json={
                                'name': 'Ryon',
                                'pwd':'123'
                            })