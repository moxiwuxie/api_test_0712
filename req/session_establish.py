#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
def session_establish(method,url,data=None,**kwargs):
  try:
    method = str(method.lower())
  except:
    print('method blank')
  rep = None
  if method == 'get':
    rep = requests.session().request(method=method,url=url,params=data,**kwargs)
  elif method == 'post':
    if data:
      pass
    else:
      print("data blank")
    rep = requests.session().request(method=method,url=url,params=data,**kwargs)
  else:
    rep = requests.session().request(method=method,url=url,**kwargs)
  return rep
