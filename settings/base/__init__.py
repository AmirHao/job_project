import pymysql

from settings.base.django import *
from settings.base.rest_framework import *
from settings.base.jwt import *
from settings.base.log import *

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()
