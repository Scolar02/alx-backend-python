#!/usr/bin/env python3
"""
Async Generator Module
This module defines an async gen that yields a random no
with delay of 1-10 second
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generatr random number asynchronously

    Yields:
        float: A random number between 0-10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
