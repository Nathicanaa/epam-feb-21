# A test for task1 homework 10
import asyncio

import aiohttp
import pytest

from homework10.tasks.task1 import (
    get_company_information,
    get_exchange,
    get_final_information,
    get_urls_and_initial_company_information,
)


@pytest.fixture
def event_loop():
    """A fixture for calling async functions with sync syntax"""
    loop = asyncio.get_event_loop()
    yield loop


def test_get_exchange(event_loop):
    """Runs get_exchange func, passes if no exceptions were raised"""
    event_loop.run_until_complete(get_exchange(aiohttp.ClientSession()))


def test_get_urls_and_initial_company_information(event_loop):
    """Runs get_urls_and_initial_company_information func, passes if no exceptions were raised"""
    event_loop.run_until_complete(get_urls_and_initial_company_information())


@pytest.mark.parametrize(
    "url",
    [
        "https://markets.businessinsider.com/stocks/mmm-stock",
        "https://markets.businessinsider.com/stocks/aos-stock",
        "https://markets.businessinsider.com/stocks/abt-stock",
    ],
)
def test_get_company_information(event_loop, url):
    """Runs get_company_information func, passes if no exceptions were raised"""
    event_loop.run_until_complete(
        get_company_information(aiohttp.ClientSession(), 10, url)
    )


@pytest.mark.timeout(60)
@pytest.mark.asyncio
async def test_get_final_information():
    """The final function without saving to json files
    Passes if every value of name, code and url columns are unique and
    get_final_information func runs without an exception"""
    data = await get_final_information(aiohttp.ClientSession())
    names = [data[key]["name"] for key in data]
    codes = [data[key]["code"] for key in data]
    urls = [data[key]["url"] for key in data]
    assert len(data) == len(set(names)) == len(set(codes)) == len(set(urls))


loop = asyncio.get_event_loop()
loop.run_until_complete(get_final_information(aiohttp.ClientSession()))
