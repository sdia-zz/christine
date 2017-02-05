#!/usr/bin/env python
#-*- coding:utf-8 -*-



import sys
import requests
from datetime import datetime, timedelta
from calendar import Calendar
import psycopg2
import settings
from settings import log
from urlparse import urlparse
from bs4 import BeautifulSoup



PG_CONN = psycopg2.connect(
            database=settings.PG_DATABASE,
            user=settings.PG_USER,
            password=settings.PG_PWD,
            host=settings.PG_HOST,
            port=settings.PG_PORT)

WIKIPEDIA_TABLE_RAW = 'christine.wikipedia_raw'
WIKIPEDIA_TABLE_PARSED = 'christine.wikipedia_parsed'
WIKIPEDIA_TABLE_PARSED_STG = 'christine.wikipedia_parsed_stg'


WIKIPEDIA_PAGE_TEMPLATE = 'https://en.wikipedia.org/wiki/Portal:Current_events/{YYYY}_{Month}_{D}'
MONTHS = [None,
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']








def get_domain_from_url(url_string):
    parsed_uri = urlparse(url_string)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain




def fetch_wikipedia_raw_page(year, month, day):

    wiki_url = WIKIPEDIA_PAGE_TEMPLATE.format(
                       YYYY = year,
                       Month = MONTHS[month],
                       D = day)

    log.debug('GET %s', wiki_url)
    r = requests.get(wiki_url)
    try:
        r.raise_for_status()
    except:
        log.error('NOT FOUND')
        return 'NOT FOUND: ' + wiki_url

    return r.text


def insert_wikipedia_raw(date_str):

    with PG_CONN.cursor() as cur:
        c = 0
        for year, month, day in date_generator(date_str):
            event_raw = fetch_wikipedia_raw_page(year, month, day)
            event_date = datetime(year, month, day)
            cmd = 'INSERT INTO {table} (event_date, event_raw) VALUES (%s, %s);'
            cmd = cmd.format(table=WIKIPEDIA_TABLE_RAW)
            log.debug(cmd)
            cur.execute(cmd, (event_date, event_raw))

            c+=1
            if c % 20:
                PG_CONN.commit()

    PG_CONN.commit()
    log.debug('Done.')


def parse_wiki_event(date_str):
    for year, month, day in date_generator(date_str):
        event_date = '{}-{}-{}'.format(year, month, day)
        with PG_CONN.cursor() as cur:
            cmd = "SELECT event_raw FROM {table} where event_date='{event_date}' ORDER BY inserted_at DESC;"
            cmd = cmd.format(table=WIKIPEDIA_TABLE_RAW, event_date=event_date)
            cur.execute(cmd)

            event_raw = cur.fetchone()[0]

            soup = BeautifulSoup(event_raw, 'html.parser')

            try:
                event_table = soup.find('table', {'class':'vevent'})
                event_types = event_table.find('td', {'class': 'description'}).find_all('dl')
                event_types_str = [o.text.strip() for o in event_types]

                log.debug(event_types_str)

                events_uls = event_table.find('td', {'class': 'description'}).select('> ul')
                #log.debug(events_uls)
                #log.debug(len(events_uls))
                # each ul correspond to an event_type
                # in one ul several events

                assert len(event_types_str) == len(events_uls)

                for event_type_str, uls in zip(event_types_str, events_uls):
                    for event in  uls.select('> li'):
                        event_type = event_type_str
                        event_title = event.find('a').text
                        event_body = event.text
                        event_sources = [get_domain_from_url(o['href']) for o in event.find_all('a', {'rel':'nofollow', 'class': 'external text'})]

                        cmd = ('INSERT INTO {table} (event_date, event_type, event_title, event_body, event_sources) '
                               'VALUES (%s, %s, %s, %s, %s);')
                        cmd = cmd.format(table=WIKIPEDIA_TABLE_PARSED_STG)

                        cur.execute(cmd, (event_date, event_type, event_title, event_body, event_sources))
                        PG_CONN.commit()

                        print 'EVENT TYPE ', event_type
                        print 'EVENT TITLE ', event_title
                        print 'EVENT BODY', event_body
                        print 'EVENT SOURCES', event_sources

            except Exception, e:
                log.error('could not parse %s', event_date)
                # exit(e)


def date_generator(date_str):

    '''Input:
       - YYYY-MM-DD
       - YYYY-MM
       - YYYY
    '''

    dsplit = date_str.split('-')

    if len(dsplit) == 3: # assume date
        d = datetime.strptime(date_str, '%Y-%m-%d')
        yield (d.year, d.month, d.day)

    elif len(dsplit) == 2: # assume year-month
        month = int(dsplit[1])
        dobj = datetime.strptime(date_str, '%Y-%m')
        while True:
            if dobj.month != month:
                break
            else:
                yield (dobj.year, dobj.month, dobj.day)
                dobj += timedelta(days=1)

    elif len(dsplit) == 1:
        year = int(date_str)
        dobj = datetime.strptime(date_str, '%Y')
        while True:
            if dobj.year != year:
                break
            else:
                yield (dobj.year, dobj.month, dobj.day)
                dobj += timedelta(days=1)

    else:
        raise Exception('Unknown date format %s' % date_str)




if __name__ == '__main__':
    # date_str = sys.argv[1]
    # [insert_wikipedia_raw(str(y)) for y in range(2000, 2016)]
    [parse_wiki_event(str(y)) for y in range(2000, 2016)]
