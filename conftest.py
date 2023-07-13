#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import time

import pytest
import requests
from common.excel_util import write_excel, save_excel
from req.default_headers import default_headers
from req.session_establish import session_establish
tableName1 = "../data/1.xlsx"
sheetName1 = "core_case"
sheetName2 = "login_data"


@pytest.fixture(scope="session",params=["test"],autouse=True)
def login():
  rep = session_establish(method=write_excel(table_name=tableName1,sheet_name=sheetName1,coordinate_name='B2'),url=write_excel(table_name=tableName1,sheet_name=sheetName1,coordinate_name='C2'),headers=default_headers(),data=write_excel(table_name=tableName1,sheet_name=sheetName1,coordinate_name='D2'))
  if 'token' in rep.text:
    token = json.loads(rep.text)['data']['token']
    save_excel(table_name=tableName1,sheet_name=sheetName2,coordinate_name='A1',data=token)
  else:
    pass
  yield
  data = {
    "msg_type": "interactive",
    "card": {
      "config": {
        "wide_screen_mode": True,
        "enable_forward": True
      },
      "elements": [{
        "tag": "div",
        "text": {
          "content": "allure报告地址：",
          "tag": "lark_md"
        }
      }, ],
      "header": {
        "title": {
          "content": "自动化测试报告-allure：" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
          "tag": "plain_text"
        }
      }
    }
  }
  response = requests.post("https://open.feishu.cn/open-apis/bot/v2/hook/9a03d9e4-089e-4dc1-9a1d-7e85fcba7e46",
                           data=json.dumps(data))
  print("\nsession会话结束！")
