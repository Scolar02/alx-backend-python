import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10 after waiting for 1 second in each iteration.

    Returns:
        Generator[float, None, None]: A generator yielding random floating-point numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
