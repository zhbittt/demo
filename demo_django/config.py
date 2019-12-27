# -*- coding: utf-8 -*-
import os

# 依赖的mysql数据库
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_PORT = os.environ.get('MYSQL_PORT', 3306)
MYSQL_USER = os.environ.get('MYSQL_USER', 'demo')
MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME', 'demo')
MYSQL_PWD = os.environ.get('MYSQL_PWD', 'demo')
