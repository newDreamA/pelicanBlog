#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mr Tang'
SITENAME = u'My Blog'
#SITEURL = 'http://localhost:8000'
SITEURL = 'http://newDreamA.github.io'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_DATE = 'fs'


PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
LOCALE = ("zh_CN")  # 设置语言环境

THEME = "pelican-elegant"

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img', 'neighbors', 'latex', 'related_posts', 'assets', 'share_post', 'series']
MD_EXTENSIONS = ['codehilite(css_class=highlight,linenums=True)', 'extra', 'headerid', 'toc(permalink=true)', 'fenced_code', ]

SITEMAP = {
    'format': 'xml',
    'priorities': {
         'articles': 0.5,
         'indexes': 0.5,
         'pages': 0.5
     },
     'changefreqs': {
         'articles': 'monthly',
         'indexes': 'daily',
         'pages': 'monthly'
     }
}


TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Misc'


# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'

USE_FOLDER_AS_CATEGORY = True
FILENAME_METADATA = '(?P<slug>.*)'
DEFAULT_CATEGORY = 'Misc'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
USE_SHORTCUT_ICONS = True
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
SE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Contact'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Share on:'
COMMENTS_INTRO = u'Comments Below:'


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

LANDING_PAGE_ABOUT = {'title': ' Mr Tang博客',
        'details': """<div itemscope itemtype="http://schema.org/Person">
        <p></p>
        <p></p>
        <p> </p></div>"""}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
