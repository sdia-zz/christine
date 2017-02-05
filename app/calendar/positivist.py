#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Positivist(Calendar):

    calendar = convertdate.positivist
    debug = False


if __name__ == '__main__':
    b=Positivist()
    b.insert()
