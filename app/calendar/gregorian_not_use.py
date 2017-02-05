#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Gregorian(Calendar):

    calendar = convertdate.gregorian
    debug = False


if __name__ == '__main__':
    b=Gregorian()
    b.insert()
