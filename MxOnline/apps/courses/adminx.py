# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__date__ = '12/17/2018 4:15 PM'

import xadmin
from .models import Course, Lesson, Video, CourseResource


# Course的admin管理器
class CourseAdmin(object):
    list_display = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']


xadmin.site.register(Course, CourseAdmin)