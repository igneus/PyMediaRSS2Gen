# coding=utf-8

"""
tests of MediaThumbnail
"""

import pytest
import PyMediaRSS2Gen as mrss

from fixtures import *

@pytest.fixture
def itemWithThumbnail():
    """ fixture creating an item with thumbnail """
    thumb = mrss.MediaThumbnail(
        url='http://nowhere.org/img/hippo_tn.jpg',
        time='00:15:46',
        width=150,
        height=652
    )
    image = mrss.MediaContent(
        type='image',
        url='http://nowhere.org/img/hippo.jpg',
        media_thumbnails=thumb
    )
    return mrss.MediaRSSItem(
        title="Item with thumbnail",
        media_content=image
    )

class TestMediaThumbnail(object):

    def test_withoutUrl(self):
        """ url is required """
        with pytest.raises(AttributeError):
            mrss.MediaThumbnail(url=None)

    def test_withoutTime(self):
        """ is ok """
        mrss.MediaThumbnail(url=FEED_URL)

    def test_withInvalidTime(self):
        """ time must be in the NTP format """
        with pytest.raises(AttributeError):
            mrss.MediaThumbnail(url=FEED_URL, time='notime')

    def test_withValidTime(self):
        """ is ok """
        mrss.MediaThumbnail(url=FEED_URL, time='00:05:10')
        mrss.MediaThumbnail(url=FEED_URL, time='00:05:10.5')

    def test_XMLOutputContainsThumbnail(self, feed, itemWithThumbnail):
        """ first output test: the thumbnail element must be in the output """
        feed.items = [itemWithThumbnail]
        output = feed.to_xml()
        assert '<media:thumbnail' in output

    def test_publishesCorrectly(self, feed, itemWithThumbnail):
        """ the thumbnail element should be output with the desired argument order """
        feed.items = [itemWithThumbnail]
        output = feed.to_xml()

        assert output.endswith(
            '<media:thumbnail url="http://nowhere.org/img/hippo_tn.jpg" width="150" height="652" time="00:15:46"></media:thumbnail>' +
            '</media:content>' +
            '</item></channel></rss>'
        )
