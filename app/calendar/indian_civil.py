#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Indian_civil(Calendar):

    calendar = convertdate.indian_civil
    debug = False


if __name__ == '__main__':
    b=Indian_civil()
    b.insert()
