import pytest
from myIPYNBrenderer import render_site
from myIPYNBrenderer.custom_exception import InvalidURLException


class TestRenderSite:
    Good_URL_test_data = [
        ("https://pytorch.org", "SUCCESS"),
        ("http://pytorch.org", "SUCCESS"),
    ]

    Bad_URL_test_data = [
        ("https://pytorch"),
        ("http://pytorch"),
        ("https:/pytorch.org"),
        ("https//pytorch.org"),
        ("https/pytorch.org"),
        ("https:pytorch.org"),
        ("pytorch.org"),
        ("https://asyef"),
    ]

    @pytest.mark.parametrize("URL, responce", Good_URL_test_data)
    def test_render_site_success(self, URL, responce):
        assert render_site(URL) == responce

    @pytest.mark.parametrize("URL", Bad_URL_test_data)
    def test_render_site_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_site(URL)