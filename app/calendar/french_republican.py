#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class French_republican(Calendar):

    calendar = convertdate.french_republican
    debug = False


if __name__ == '__main__':
    b=French_republican()
    b.insert()
