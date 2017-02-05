#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Bahai(Calendar):

    calendar = convertdate.bahai
    debug = False


if __name__ == '__main__':
    b=Bahai()
    b.insert()
