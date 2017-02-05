#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class ISO(Calendar):

    calendar = convertdate.iso
    debug = False


if __name__ == '__main__':
    b=ISO()
    b.insert()
