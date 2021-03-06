#!/usr/bin/python
# -*- coding: utf8 -*-

from currency2text.ctt_objects import ctt_currency

class uah(ctt_currency):
    def _init_currency(self):
        self.language = u'lt_LT'
        self.code = u'UAH'
        self.fractions = 100
        self.cur_singular = u' grivna'
        # default plural form for currency
        self.cur_plural = u' grivnų'
        # betwean 1 and 10 yields different plural form, if defined
        self.cur_plural_2to10 = u' grivnai'
        self.frc_singular = u' kapeika'
        # default plural form for fractions
        self.frc_plural = u' kapeikų'
        # betwean 1 and 10 yields different plural form, if defined
        self.frc_plural_2to10 = u' kapeikos'
        # grammatical genders: f - feminine, m - masculine, n -neuter
        self.cur_gram_gender = 'm'
        self.frc_gram_gender = 'm'
    
uah()
