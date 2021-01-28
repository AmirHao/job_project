#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11
from rest_framework import routers

from job.views.company import CompanyViewSet
from job.views.company2user import Company2UserViewSet
from job.views.history import HistoriesViewSet
from job.views.jianli import JianLiViewSet
from job.views.job import JobViewSet
from job.views.job2jianli import Job2JianliViewSet
from job.views.role import RoleViewSet
from job.views.test_view import TestViewSet, TestGenericViewSet, TestModelViewSet
from job.views.user import UserView

router = routers.DefaultRouter()
router.trailing_slash = '/?'
router.routes[2].mapping.pop('delete')
router.routes[2].mapping['put'] = router.routes[2].mapping['patch']
router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'company2users', Company2UserViewSet, basename='company2users')
router.register(r'jianlis', JianLiViewSet, basename='jianlis')
router.register(r'jobs', JobViewSet, basename='jobs')
router.register(r'job2jianlis', Job2JianliViewSet, basename='job2jianlis')
router.register(r'users', UserView, basename='users')
# router.register(r'testviewset', TestViewSet, basename='testviewset')
# router.register(r'testgenericviewset', TestGenericViewSet, basename='testgenericviewset')
# router.register(r'testmodelviewset', TestModelViewSet, basename='testmodelviewset')
router.register(r'histories', HistoriesViewSet, basename='histories')
