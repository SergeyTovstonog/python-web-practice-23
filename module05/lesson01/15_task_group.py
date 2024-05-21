import asyncio


# Function to perform an asynchronous sleep
async def sleep_task(name, duration):
    print(f"Task {name} started, sleeping for {duration} seconds...")
    await asyncio.sleep(duration)
    print(f"Task {name} completed after {duration} seconds.")
    return f"Result from {name}"


# Function demonstrating the usage of asyncio.TaskGroup
async def run_tasks():
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(sleep_task(f"Task {i}", i)) for i in range(10)]


    # Accessing the results of each task using .result()


    print("All tasks completed.")
    print("Results:", [task.result() for task in tasks])


# Main function to run the async tasks
def main():
    asyncio.run(run_tasks())


if __name__ == "__main__":
    main()
