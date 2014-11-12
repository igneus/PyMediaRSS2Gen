# coding=utf-8

""" fixtures """

import pytest
import PyMediaRSS2Gen as mrss

FEED_URL = 'http://nowhere.org/rss.xml'

@pytest.fixture
def feed():
    """ fixture creating an empty feed """
    return mrss.MediaRSS2(
        title = 'Test Feed',
        link = 'http://nowhere.org/nopost',
        description = 'A testing feed'
    )