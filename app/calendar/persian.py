#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Persian(Calendar):

    calendar = convertdate.persian
    debug = False


if __name__ == '__main__':
    b=Persian()
    b.insert()
