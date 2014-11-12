# coding=utf-8

""" fixtures """

import pytest

@pytest.fixture
def feed():
    """ fixture creating an empty feed """
    return mrss.MediaRSS2(
        title = 'Test Feed',
        link = 'https://github.com/wedi/PyMediaRSS2Gen/',
        description = 'A testing feed'
    )