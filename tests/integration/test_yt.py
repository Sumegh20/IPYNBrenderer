import pytest
from myIPYNBrenderer.youtube import render_YouTube_video
from myIPYNBrenderer.custom_exception import InvalidURLException

class TestYTvideoRenderer:
    good_URL_SUCCESS_data = [
        ("https://www.youtube.com/watch?v=Tw1fgeEKk-E&t=198s", "SUCCESS"),
        ("https://youtu.be/Tw1fgeEKk-E", "SUCCESS"),
        ("https://www.youtube.com/watch?v=Tw1fgeEKk-E", "SUCCESS"),
    ]

    bad_URL_SUCCESS_data = [
        ("https://www.youtube.com/watch?v==Tw1fgeEKk-E&t=198s"),
        ("https://www.youtube.com/watch?v=Tw1fgeEKk-E&t==198s"),
        ("https://youtu.be/Tw1fgeEKk-EreTR"),
        ("https://www.youtube.com/watch?v=Tw1fgeE&t"),
    ]

    @pytest.mark.parametrize("URL, responce", good_URL_SUCCESS_data)
    def test_render_YT_SUCCESS(self, URL, responce):
        assert render_YouTube_video(URL) == responce

    @pytest.mark.parametrize("URL", bad_URL_SUCCESS_data)
    def test_render_YT_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_YouTube_video(URL)
