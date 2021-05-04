import asyncio
import json
from heapq import nlargest, nsmallest
from operator import itemgetter
from typing import Dict, Tuple

import aiohttp
from bs4 import BeautifulSoup


async def get_exchange(session: aiohttp.ClientSession) -> float:
    """
    Takes a current exchange rate rub to usd from the cbr website
    Args:
        session: a session object to provide a connection

    Returns: current exchange rate USA usd to russian rubble

    """
    async with session.get("http://www.cbr.ru/scripts/XML_daily.asp") as response:
        text = await response.read()
        return float(
            BeautifulSoup(text, "lxml")
            .find(id="R01235")
            .find("value")
            .text.replace(",", ".")
        )


async def get_urls_and_initial_company_information() -> Dict:
    """
    Parses companies urls from businessinsider's s&p_500 rating
    with urls parses initial information as well:
    name of company and 1 year growth
    creates a dict with the information about companies

    Returns: a dict with a name, an url and 1 year growth
    columns code, price, pe_ratio and potential_profit are None
    for this stage and will be filled further

    """
    async with aiohttp.ClientSession() as session:
        company_info = {}
        for i in range(1, 11):  # Walking through every s&p_500 page
            async with session.get(
                f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
            ) as response:
                html = await response.text()
                table = (
                    BeautifulSoup(html, "lxml")
                    .find(class_="table table-small")
                    .find_all("tr")
                )
                for row in table[1:]:  # Taking information from table string by string
                    name = row.find("a")["title"]
                    link = row.find("a")["href"]
                    growth = row.find_all("td")[-2].text.split()[1]
                    company_info[name] = {
                        "code": None,
                        "name": name,
                        "price": None,
                        "pe_ratio": None,
                        "growth": float(growth[:-1]),
                        "potential_profit": None,
                        "url": "https://markets.businessinsider.com" + link,
                    }
        return company_info


async def get_company_information(
    session: aiohttp.ClientSession, rate: float, url: str
) -> Tuple[str, str, float, float, float]:
    """
    Takes a session, an exchange rate and a company page url, then get
    information about company: code, price, pe_ratio and potential_profit
    Taken information will be returned as a tuple

    Args:
        session: a session object to provide a connection
        rate: current exchange rate USA usd to russian rubble
        url: a company url

    Returns: a tuple with parsed information about companies with url

    """
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "lxml")
        table = soup.find_all("div", class_="snapshot__data-item")
        week_low = float(table[6].contents[0].strip().replace(",", ""))
        week_high = float(table[7].contents[0].strip().replace(",", ""))
        potential_profit = round((week_high - week_low) / week_low * 100, 2)
        pe_ratio = float(table[8].contents[0].strip().replace(",", ""))
        price = round(
            float(
                soup.find("span", class_="price-section__current-value").text.replace(
                    ",", ""
                )
            )
            * rate,
            2,
        )
        code = (
            soup.find("span", class_="price-section__category")
            .text.split(",")[1]
            .strip()
        )
        return url, code, price, pe_ratio, potential_profit


async def get_final_information(session: aiohttp.ClientSession) -> Dict:
    """
    Makes final dict with whole information about companies by updating
    dict with initial information with tuples returned by get_company_information func

    Args:
        session: a session object to provide a connection

    Returns: a dict with full information about companies

    """
    async with session:
        rate = await get_exchange(session)
        companies = await get_urls_and_initial_company_information()

        tasks = []
        urls = [companies[key]["url"] for key in companies]
        for url in urls:
            task = asyncio.create_task(get_company_information(session, rate, url))
            tasks.append(task)
        result = await asyncio.gather(*tasks)

        for key in companies:
            for element in result:
                if companies[key]["url"] == element[0]:
                    companies[key]["code"] = element[1]
                    companies[key]["price"] = element[2]
                    companies[key]["pe_ratio"] = element[3]
                    companies[key]["potential_profit"] = element[4]
        return companies


def save_in_json(data: Dict) -> None:
    """
    Takes a final dict with full information about companies and saves into 4 json files
    with a certain sorting:
        top 10 highest prices per stock in rubbles,
        top 10 lowest p/e ratio
        top 10 highest growth last year
        top 10 highest potential profit
    Args:
        data: dict with companies information

    Returns: 4 json files with sorted objects

    """
    with open("10_top_price" + ".json", "w", encoding="utf-8") as file1:
        top_10_price = nlargest(10, data.values(), key=itemgetter("price"))
        top_price = [
            {"name": dct["name"], "code": dct["code"], "price": dct["price"]}
            for dct in top_10_price
        ]
        json.dump(top_price, file1, indent=2)

    with open("10_lowest_pe" + ".json", "w", encoding="utf-8") as file2:
        top_10_lowest_pe = nsmallest(10, data.values(), key=itemgetter("pe_ratio"))
        lowest_pe = [
            {"name": dct["name"], "code": dct["code"], "pe_ratio": dct["pe_ratio"]}
            for dct in top_10_lowest_pe
        ]
        json.dump(lowest_pe, file2, indent=2)

    with open("10_top_growth" + ".json", "w", encoding="utf-8") as file3:
        top_10_growth = nlargest(10, data.values(), key=itemgetter("growth"))
        top_growth = [
            {"name": dct["name"], "code": dct["code"], "growth": dct["growth"]}
            for dct in top_10_growth
        ]
        json.dump(top_growth, file3, indent=2)

    with open("10_top_potential_profit" + ".json", "w", encoding="utf-8") as file4:
        top_10_profit = nlargest(10, data.values(), key=itemgetter("potential_profit"))
        top_profit = [
            {
                "name": dct["name"],
                "code": dct["code"],
                "potential_profit": dct["potential_profit"],
            }
            for dct in top_10_profit
        ]
        json.dump(top_profit, file4, indent=2)


async def main() -> None:
    """
    Main function, enter point
    """
    async with aiohttp.ClientSession() as session:
        res = await get_final_information(session)
        save_in_json(res)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
