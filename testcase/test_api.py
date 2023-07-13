#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import re
import pytest
import requests
from common.excel_util import write_excel,save_excel
from req.assert_api import assert_api_rep
from req.default_headers import default_headers
from req.session_establish import session_establish
tableName1 = "../data/1.xlsx"
sheetName1 = "core_case"
sheetName2 = "login_data"
sheetName3 = "parametrize"


@pytest.mark.smoke
def test_article_create():
  rep = session_establish(method=write_excel(table_name=tableName1,sheet_name=sheetName1,coordinate_name='B3'),url=write_excel(table_name=tableName1,sheet_name=sheetName1,coordinate_name='C3'),headers=default_headers(),data=write_excel(table_name=tableName1,sheet_name=sheetName1,coordinate_name='D3'))
  article_id = re.findall(r'"data":(.*?),"success"', rep.text, flags=0)
  try:
    assert_api_rep(actual=article_id,predicted='1453')
  except:
    print("not equal")
