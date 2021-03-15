"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
>> count_dots_on_i("https://example.com/")
59
* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import urllib.request
from urllib.error import HTTPError, URLError


def count_dots_on_i(url: str) -> int:
    """
    Takes url and count "i" on a page, with any network
    error raise ValueError("Unreachable {url}")
    Args:
        url: url to some web page

    Returns: int count of all "i" on a page, otherwise raise ValueError
    """
    try:
        res = urllib.request.urlopen(url)
        data = res.read().decode("utf-8")
        return data.count("i")
    except (HTTPError, URLError):
        raise ValueError(f"Unreachable {url}")
