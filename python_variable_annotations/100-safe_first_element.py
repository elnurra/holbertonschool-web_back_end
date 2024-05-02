#!/usr/bin/env python3
""" 10. Duck typing - first element of a sequence
"""

from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Gets first element safely.
    """
    if lst:
        return lst[0]
    else:
        return None
