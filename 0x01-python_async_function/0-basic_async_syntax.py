#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (int, optional): The maximum delay (in seconds) for the
        coroutine to wait. Defaults to 10.

    Returns:
        float: The actual delay the coroutine waited.
    """
    # Generate a random delay
    delay = random.uniform(0, max_delay)
    # wait for the delay
    await asyncio.sleep(delay)
    return delay
