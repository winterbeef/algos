#!/usr/bin/env python

import datetime
import pprint

class Person(object):
    def __init__(self, born, died=None):
        self.born = born
        self.died = died

    def __str__(self):
        return "{0}, {1}-{2}".format(
            id(self),
            self.born,
            self.died if self.died else ''
        )



def histogram_life_years(ppl):
    histogram = {}
    cur_year = datetime.date.today().year
    for person in ppl:
        for alive in range(person.born, person.died if person.died else cur_year):
            if alive not in histogram:
                histogram[alive] = 0
            histogram[alive] += 1
    return histogram

def events_count(ppl):
    deltas = {}
    # O(P)
    for person in ppl:
        if not person.born in deltas:
            deltas[person.born] = 1
        else:
            deltas[person.born] += 1

        if person.died:
            if not person.died in deltas:
                deltas[person.died] = -1
            else:
                deltas[person.died] -= 1

    most = -1
    mostyear = None
    cur = 0
    # O(Y)
    data = {}
    for year in sorted(deltas.keys()):
        delta = deltas[year]
        cur += delta
        if cur > most:
            most = cur
            mostyear = year

        data[year] = {
            'delta': delta,
            'cur': cur,
            'was_most': mostyear == year
        }
    return dict(data=data, most=most, mostyear=mostyear)


if __name__ == '__main__':
    sample_ppl_data = [
        Person(1945, 1987),
        Person(1935, 1977),
        Person(1935, 2011),
        Person(1937, 1987),
        Person(1962),
        Person(1963),
        Person(1978, 2015),
        Person(1985),
        Person(1968,),
        Person(1978, 2012),
        Person(2004,),
        Person(1999),
    ]

    hist = histogram_life_years(sample_ppl_data)
    most = max(hist.values())

    summary = events_count(sample_ppl_data)
    data = summary['data']
    mostyear = summary['mostyear']
    most = summary['most']

    for year in sorted(data.keys()):
        datum = data[year]
        print "{}\t{}\t{}".format(year, datum['cur'], '*' if datum['cur'] == most else '')

    # for year,num in hist.iteritems():
    #     print "{}\t{}{}".format(year, num, '*' if num == most else '')

