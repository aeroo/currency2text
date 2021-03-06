#!/usr/bin/python
# -*- coding: utf8 -*-

from currency2text.ctt_objects import ctt_currency

class eur(ctt_currency):
    def _init_currency(self):
        self.language = u'lv_LV'
        self.code = u'EUR'
        self.fractions = 100
        self.cur_singular = u' eiro'
        self.cur_plural = u' eiro'
        self.frc_singular = u' cents'
        # default plural form for fractions
        self.frc_plural = u' centu'
        # betwean 1 and 10 yields different plural form, if defined
        self.frc_plural_2to10 = u' centi'
        # grammatical genders: f - feminine, m - masculine, n -neuter
        self.cur_gram_gender = 'm'
        self.frc_gram_gender = 'm'
    
eur()
