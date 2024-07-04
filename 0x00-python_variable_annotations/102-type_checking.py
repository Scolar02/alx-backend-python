#!/usr/bin/env python3
"""
Module 102-type_checking
Contains a function that zooms into an array by a given factor.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a zoomed-in list by repeating each element in lst factor times."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
