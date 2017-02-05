#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Mayan(Calendar):

    calendar = convertdate.mayan
    columns_list = ['isodate', 'baktun', 'katun', 'tun', 'uinal', 'kin']

    debug = False


    def insert(self):
        todml = ''
        values_tuple = []
        for d in self._generate_date():
            isoyear, isomonth, isoday = d
            isodate = '{:04d}-{:02d}-{:02d}'.format(isoyear, isomonth, isoday)
            baktun, katun, tun, uinal, kin = self.calendar.from_gregorian(isoyear, isomonth, isoday)
            str_tuple = "('{isodate}',\t{baktun},\t{katun},\t{tun},\t{uinal},\t{kin})"
            str_tuple = str_tuple.format(
                isodate=isodate,
                baktun=baktun,
                katun=katun,
                tun=tun,
                uinal=uinal,
                kin=kin)

            values_tuple.append(str_tuple)

        cmd_insert = self.DML_CMD_INSERT.format(
            TABLE_NAME = self.table_name,
            COLUMNS_LIST = ','.join(self.columns_list),
            VALUES_TUPLE = '\n, '.join(values_tuple))

        todml += self.dml_header
        todml += cmd_insert

        if self.debug:
            print 'DEBUG mode'
            print 'writting to {}...'.format(self.dml_path),
            with open(self.dml_path, 'w') as f:
                f.write(todml)
        else:
            print 'Inserting to {}...'.format(self.table_name)
            with self.pgconn.cursor() as cur:
                cur.execute(todml)
            self.pgconn.commit()

        print 'OK.'



if __name__ == '__main__':
    b=Mayan()
    b.insert()
