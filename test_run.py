#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import pytest
import sys
if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')

