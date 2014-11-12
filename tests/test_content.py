# coding=utf-8

"""
tests of MediaContent
"""

import pytest
import PyMediaRSS2Gen as mrss

from fixtures import *

class TestMediaContent(object):

    def test_output(self, feed):
        """ output of a basic content should look like this """

        image = mrss.MediaContent(
            type='image',
            url='http://nowhere.org/img/hippo.jpg',
        )
        item = mrss.MediaRSSItem(
            title="Item with thumbnail",
            media_content=image
        )
        feed.items = [item]
        output = feed.to_xml()

        assert output.endswith(
            '<media:content url="http://nowhere.org/img/hippo.jpg" type="image"></media:content>'+
            '</item></channel></rss>'
        )