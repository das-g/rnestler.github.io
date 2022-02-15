#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'rnestler'
SITENAME = 'blog.rnstlr.ch'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('coredump', 'http://www.coredump.ch/'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/rnstlr'),
          ('github', 'https://github.com/rnestler'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
