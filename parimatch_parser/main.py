import asyncio
import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from html_parser import parse_html


def get_driver():
    """Returns webdriver instance for browser manipulation"""

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=options)

    return driver


async def was_page_opened(driver):

    await asyncio.sleep(1)
    block_xpath = './/a[@class="live-block-competitors"]'
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, block_xpath)))


async def get_page_source(driver, url):

    page_source = None
    driver.get(url)

    try:
        await was_page_opened(driver)
    except TimeoutException:
        print('{} page block was not found'.format(driver.current_url))
    else:
        # Need to scroll to bottom of the page to have links assigned to all fight blocks
        await scroll_to_page_bottom(driver)
        page_source = driver.page_source

    return page_source


async def scroll_to_page_bottom(driver):
    """Scrolling to page bottom to load entire page"""

    for k in range(1, 11):  # split body height to 10 parts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*{})".format(k / 10))
        await asyncio.sleep(1)


async def parse(url):

    driver = get_driver()
    page_source = await get_page_source(driver, url)
    driver.close()
    parsed_dict = {url: parse_html(page_source)}

    return parsed_dict


async def main(urls):

    result_dict = {}
    futures = [parse(url) for url in urls]
    for future in asyncio.as_completed(futures):
        future_res = await future
        result_dict.update(future_res)

    with open('parsed_parimatch.json', 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, ensure_ascii=False)

if __name__ == '__main__':
    links = ['https://www.parimatch.ru/prematch/all/1|F', 'https://www.parimatch.ru/prematch/all/1|MA']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(links))
    loop.close()