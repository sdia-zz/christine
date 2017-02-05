#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Islamic(Calendar):

    calendar = convertdate.islamic
    debug = False


if __name__ == '__main__':
    b=Islamic()
    b.insert()
