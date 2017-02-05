#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Hebrew(Calendar):

    calendar = convertdate.hebrew
    debug = False


if __name__ == '__main__':
    b=Hebrew()
    b.insert()
