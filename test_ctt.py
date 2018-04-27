#!/usr/bin/python
# -*- coding: utf8 -*-

from currency2text import currency_to_text, supported_language
amount = 23.45

for lang in supported_language.keys():
    print lang
    for currency in supported_language.get(lang).supported_currency.keys():
        print ('%s: %s') % (currency, supported_language.get(lang).currency_to_text(23.45, currency).decode('utf-8'),)
