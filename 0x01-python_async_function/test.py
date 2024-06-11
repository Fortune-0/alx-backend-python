# import asyncio

# async def async_function():
#     print('Hello ...')
#     print('about to sleep')
#     await asyncio.sleep(1)
#     print('... World!')
    
# loop = asyncio.get_event_loop()
# loop.run_until_complete(async_function)
# loop.close

# asyncio.run(async_function())
import asyncio

async def example_async_function():
    print('about to sleep')
    await asyncio.sleep(1)
    print("Async function executed")

loop = asyncio.get_event_loop()
loop.run_until_complete(example_async_function())
loop.close()