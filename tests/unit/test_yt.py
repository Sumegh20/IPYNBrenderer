import pytest
from myIPYNBrenderer import get_time_info
from myIPYNBrenderer.custom_exception import InvalidURLException

# list of good data (URL)
good_URL_data = [
    ("https://www.youtube.com/watch?v=Tw1fgeEKk-E&t=198s", 198),
    ("https://youtu.be/Tw1fgeEKk-E", 0),
    ("https://www.youtube.com/watch?v=Tw1fgeEKk-E", 0),
]

# list of bad data (URL)
bad_URL_data = [
    ("https://www.youtube.com/watch?v==Tw1fgeEKk-E&t=198s"),
    ("https://www.youtube.com/watch?v=Tw1fgeEKk-E&t==198s"),
    ("https://youtu.be/Tw1fgeEKk-EreTR"),
    ("https://www.youtube.com/watch?v=Tw1fgeE&t"),
]

# Testing for good data 
@pytest.mark.parametrize("URL, responce", good_URL_data)
def test_get_time_info(URL, responce):
    assert get_time_info(URL) == responce

# Testing for bad data
@pytest.mark.parametrize("URL", bad_URL_data)
def test_get_time_info_faild(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)