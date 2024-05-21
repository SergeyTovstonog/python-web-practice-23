import asyncio
import aiohttp
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# List of sample API endpoints
API_ENDPOINTS = [ f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(100)]
#     "https://jsonplaceholder.typicode.com/posts/1",
#     "https://jsonplaceholder.typicode.com/posts/2",
#     "https://jsonplaceholder.typicode.com/posts/3",
#     "https://jsonplaceholder.typicode.com/posts/4",
#     "https://jsonplaceholder.typicode.com/posts/5"
# ]


# Synchronous function to fetch data from APIs
def fetch_data_sync(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}


def sync_mode():
    results = []
    for url in API_ENDPOINTS:
        results.append(fetch_data_sync(url))
    write_to_file("sync_results.txt", results)


# Asynchronous function to fetch data from APIs
async def fetch_data_async(session, url):
    async with session.get(url, ssl=False) as response:
        if response.status == 200:
            return await response.json()
        else:
            return {"error": "Failed to fetch data"}


async def async_mode():
    results = []
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch_data_async(session, url)) for url in API_ENDPOINTS]
            for task in tasks:
                results.append(await task)
    write_to_file("async_results.txt", results)


# Threaded function to fetch data from APIs
def fetch_data_threaded(url, results, index):
    results[index] = fetch_data_sync(url)


def threaded_mode():
    results = [None] * len(API_ENDPOINTS)
    threads = []
    for i, url in enumerate(API_ENDPOINTS):
        thread = threading.Thread(target=fetch_data_threaded, args=(url, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    write_to_file("threaded_results.txt", results)


# Function to write results to a file
def write_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")


# Main function to execute all modes
def main():
    start_time = time.time()
    print("Running sync mode...")
    sync_mode()
    print(f"Sync mode finished in {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    print("Running async mode...")
    asyncio.run(async_mode())
    print(f"Async mode finished in {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    print("Running threaded mode...")
    threaded_mode()
    print(f"Threaded mode finished in {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
