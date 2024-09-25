from tempfile import NamedTemporaryFile

import pytest

import app.fileutils as fileutils


def test_json_content():
    expected = {'last_status_update': '2024-07-22T17:19:49.515439+00:00'}
    assert expected == fileutils.json_content('tests/status_sample.json')
