import pytest
from myIPYNBrenderer import is_valid_URL

URL_test_data = [
    ("https://pytorch.org", True),
    ("http://pytorch.org", True),
    ("https://pytorch", False),
    ("http://pytorch", False),
    ("https:/pytorch.org", False),
    ("https//pytorch.org", False),
    ("https/pytorch.org", False),
    ("https:pytorch.org", False),
    ("pytorch.org", False),
    ("https://asyef", False)
]

@pytest.mark.parametrize("URL, response", URL_test_data)
def test_is_valid_URL(URL, response):
    assert is_valid_URL(URL) == response


# run the test using 
# pytest -v