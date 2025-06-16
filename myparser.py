import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text

def parse_main_page(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    table = soup.find("table", class_="table")
    if not table:
        return results
    rows = table.find_all("tr")[2:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            code = cols[0].text.strip()
            name = cols[1].text.strip()
            link_tag = cols[0].find("a")
            if not link_tag:
                for col in cols:
                    a = col.find("a")
                    if a:
                        link_tag = a
                        break
            if link_tag and "href" in link_tag.attrs:
                link = urljoin(base_url, link_tag["href"])
                results.append({"code": code, "name": name, "link": link})
    return results

from bs4 import BeautifulSoup

def parse_detail_page(html):
    soup = BeautifulSoup(html, "html.parser")

    # Поиск таблицы okrsků: первая таблица после nadpisu "Okrsky"
    okrsky_table = soup.find("table", {"summary": lambda s: s and "Okrsky" in s})
    if not okrsky_table:
        okrsky_table = soup.find_all("table", class_="table")[0]  # backup

    # Считаем celkem všechny okrsky:
    total_voters = total_envelopes = total_valid = 0
    rows = okrsky_table.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 8:
            total_voters += int(cols[3].text.strip().replace('\xa0','').replace(' ', ''))
            total_envelopes += int(cols[4].text.strip().replace('\xa0','').replace(' ', ''))
            total_valid += int(cols[7].text.strip().replace('\xa0','').replace(' ', ''))

    # Теперь продолжаем парсить výsledky podle stran:
    parties = {}
    for tbl in soup.find_all("table", class_="table")[1:]:
        for tr in tbl.find_all("tr")[1:]:
            tds = tr.find_all("td")
            if len(tds) >= 3:
                party = tds[1].text.strip()
                votes = tds[2].text.strip().replace('\xa0','').replace(' ', '')
                if votes.isdigit():
                    parties[party] = parties.get(party, 0) + int(votes)

    return total_voters, total_envelopes, total_valid, parties