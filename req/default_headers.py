#!/usr/bin/python
# -*- coding: UTF-8 -*-
from common.excel_util import write_excel
def default_headers(content_type="application/json"):
  headers = {
    "content-type":content_type,
    "authorization":write_excel(table_name="../data/1.xlsx",sheet_name="login_data",coordinate_name='A1')
  }
  return headers
