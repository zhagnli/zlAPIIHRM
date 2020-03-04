import unittest

import requests



class TestEmployee(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    # 登录成功
    def test01_loginSuccess(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile": "13800000002",
                                       "password": "123456"},
                                 headers={"Content-Type": "application/json"})
        print("获取的json数据为", response.json())
        jsonData = response.json()  # type:dict
        print("登录成功返回的响应数据", jsonData)
        # 断言状态响应码
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, jsonData.get("success"))
        self.assertEqual(10000, jsonData.get("code"))
        self.assertIn("操作成功", jsonData.get("message"))

    # 添加员工
    def test02_addEmployee(self):
        # 先登录
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile": "13800000002",
                                       "password": "123456"},
                                 headers={"Content-Type": "application/json"})
        jsonData = response.json()  # type:dict
        print("登录成功返回的响应数据", jsonData)
        token = "Bearer " + jsonData.get("data")
        print("token为：",token)
        response = requests.post("http://182.92.81.159/api/sys/user",
                                 json={"username":"Nancy001",
                                       "mobile":"13245678901",
                                       "timeOfEntry":"2019-07-01",
                                       "formOfEmployment": 1,
                                       "workNumber": "1322131",
                                       "departmentName": "开发部",
                                       "departmentId": "1066240656856453120",
                                       "correctionTime": "2019-11-30"
                                       },
                                 headers={"Content-Type":"application/json",
                                          "Authorization":token})
        jsonData = response.json()
        print("获取的响应数据为：",jsonData)
        # assert断言
        self.assertEqual()