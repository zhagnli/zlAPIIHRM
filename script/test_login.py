import unittest

import requests


class TestLogin(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    # 登录成功
    def test01_loginSuccess(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile":"13800000002",
                                       "password":"123456"},
                                 headers={"Content-Type": "application/json"})
        print("获取的json数据为",response.json())
        jsonData = response.json()  # type:dict
        print("登录成功返回的响应数据",jsonData)
        # 断言状态响应码
        self.assertEqual(200,response.status_code)
        self.assertEqual(True,jsonData.get("success"))
        self.assertEqual(10000,jsonData.get("code"))
        self.assertIn("操作成功",jsonData.get("message"))

    # 用户名不存在
    def test02_loginNoUser(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile":"13900000002",
                                       "password":"123456"},
                                 headers={"Content-Type":"application/json"})
        javaData = response.json()
        print("获取的json数据为：",javaData)
        # 断言代码
        self.assertEqual(200,response.status_code)
        self.assertEqual(False,javaData.get("success"))
        self.assertEqual(20001,javaData.get("code"))
        self.assertIn("用户名或密码错误",javaData.get("message"))

    # 密码错误
    def test03_loginErrorPassword(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile":"13800000002",
                                       "password":"error"},
                                 headers={"Content-Type":"application/json"})
        javaData = response.json()
        print("获取到的响应数据为：",javaData)
        # 断言判断
        self.assertEqual(200,response.status_code)
        self.assertEqual(False,javaData.get("success"))
        self.assertEqual(20001,javaData.get("code"))
        self.assertIn("用户名或密码错误",javaData.get("message"))

    # 请求参数为空
    def test04_loginNullParam(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 headers={"Content-Type":"application/json"})
        javaData = response.json()
        print("获取到的响应数据：",javaData)
        # 断言判断
        self.assertEqual(200,response.status_code)
        self.assertEqual(False,javaData.get("success"))
        self.assertEqual(99999,javaData.get("code"))
        self.assertIn("抱歉，系统繁忙，请稍后重试",javaData.get("message"))

    # 用户名为空
    def test05_loginNullUser(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile":"",
                                       "password":"123456"},
                                 headers={"Content-Type":"application/json"})
        javaData = response.json()
        print("获取到的响应数据为：",javaData)
        # 断言判断
        self.assertEqual(200,response.status_code)
        self.assertEqual(False,javaData.get("success"))
        self.assertEqual(20001,javaData.get("code"))
        self.assertIn("用户名或密码错误",javaData.get("message"))

    # 密码为空
    def test06_loginNullPassword(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile":"13800000002",
                                       "password":""},
                                 headers={"Content-Type":"application/json"})
        javaData = response.json()
        print("获取到的响应数据为：",javaData)
        # 断言响应
        self.assertEqual(200,response.status_code)
        self.assertEqual(False,javaData.get("success"))
        self.assertEqual(20001,javaData.get("code"))
        self.assertEqual("用户名或密码错误",javaData.get("message"))

