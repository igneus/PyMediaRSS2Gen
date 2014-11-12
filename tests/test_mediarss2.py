# coding=utf-8

"""
tests of the main class -
MediaRSS2
"""

import pytest
import PyMediaRSS2Gen as mrss

import fixtures

class Test_EmptyFeed(object):

    def test_toXML(self, feed):
        """ it is possible to render an empty feed """
        output = feed.to_xml()
        assert output.startswith('<?xml')
        assert '</channel>' in output
        assert '<item>' not in output

    @pytest.mark.xfail(reason='PyRSS2Gen ignores the attribute')
    def test_hasNamespace(self, feed):
        """ the feed defines the media module namespace """
        output = feed.to_xml()
        print output
        assert 'xmlns:media="http://search.yahoo.com/mrss/"' in output

class Test_Items(object):

    def test_noMedia(self, feed):
        """
        it is possible to have an item without media content
        in a media-enabled feed

        The test simply shouldn't throw an error
        """
        feed.items = [
            mrss.MediaRSSItem(
                title="Item without media content",
                description="It has no media content",
            )
        ]
        output = feed.to_xml()
