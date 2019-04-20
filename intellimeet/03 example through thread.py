import threading
import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"{threading.currentThread().getName()}: Read {len(response.content)} from {url}")


def download_all_sites(sites):
    threads = []
    with requests.Session() as session:
        for url in sites:
            t = threading.Thread(target=download_site, args=(url,session))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()


if __name__ == "__main__":
    sites = [
        "http://www.jython.org",
        "http://tothenew.com",
    ] * 400

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")