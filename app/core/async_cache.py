
import asyncio
import os
import functools
import pickle
import typing

import aiofiles
import cachetools

# Make the cache folder
os.makedirs(".cache", exist_ok=True)


def cached(cache : cachetools.Cache):

    def decerator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Check the cache
            key = (args, frozenset(sorted(kwargs.items())))
            cache_match = cache.get(key)
            if cache_match:
                return cache_match
            # Run the original function
            result = await func(*args, **kwargs)
            # Add it to the cache
            cache[key] = result
            return result
        return wrapper
    return decerator

def __test_cached():
    import time
    @cached(cache=cachetools.TTLCache(100,1000))
    async def get_thing(arg):
        time.sleep(1)
        return arg
    
    async def main():
        await get_thing(123)
        await get_thing(456)
        await get_thing(123)

    asyncio.run(main())


async def async_save_data(filename, data):
    pickled_data = pickle.dumps(data) # Synchronous CPU operation
    async with aiofiles.open(filename, 'wb') as f:
        await f.write(pickled_data) # Asynchronous I/O operation

async def async_load_data(filename):
    async with aiofiles.open(filename, 'rb') as f:
        pickled_data = await f.read() # Asynchronous I/O operation
    data = pickle.loads(pickled_data) # Synchronous CPU operation
    return data

def disk_cached():
    def decerator(func : typing.Coroutine):
        pkl_name = f".cache/{func.__name__}.pkl"
        if os.path.exists(pkl_name):
            cache : cachetools.TTLCache = asyncio.run(async_load_data(pkl_name))
        else:
            cache = cachetools.TTLCache(maxsize=8096, ttl=3600)
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Check the cache
            key = (args, frozenset(sorted(kwargs.items())))
            cache_match = cache.get(key)
            if cache_match:
                return cache_match
            # Run the original function
            result = await func(*args, **kwargs)
            # Add it to the cache
            cache[key] = result
            await async_save_data(pkl_name, cache)
            return result
        return wrapper
    return decerator


def __test_disk_cached():
    import time
    @disk_cached()
    async def get_thing(arg):
        time.sleep(1)
        return arg
    
    async def main():
        await get_thing(123)
        await get_thing(456)
        await get_thing(123)

    asyncio.run(main())


if __name__ == "__main__":
    __test_disk_cached()