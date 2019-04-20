import threading
import requests
import time
from concurrent.futures import ThreadPoolExecutor

SIZE_MAX_WORKERS = 4


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=SIZE_MAX_WORKERS) as executor:
        for url in sites:
            executor.submit(
                download_site,url,requests.Session()
            )  # non blocking call


if __name__ == "__main__":
    sites = [
        "http://www.jython.org",
        "http://tothenew.com",
    ] * 40

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print('ok')
    print(f"Downloaded {len(sites)} in {duration} seconds")