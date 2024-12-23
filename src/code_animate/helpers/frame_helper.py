
import re
from typing import Any, Optional

def filter_framedict(
    framedict: dict[str, Any],
    selected_keys: Optional[set[str]] = None
) -> dict[str, Any]:
    """
    Filters selected keys we wish to display
    """
    if selected_keys:
        # limit framedict only to selected keys
        framedict: dict[str, Any] = {
            key: value 
            for key, value in framedict.items()
            if key in selected_keys
        }
    else:
        # simply remove keys starting with _
        framedict: dict[str, Any] = {
            key: value
            for key, value in framedict.items()
            if str(key)[0] != "_"
        }

    # remove key-value pairs with non-informative values
    return {
        key: value
        for key, value in framedict.items()
        if not re.match(r"<.*>", str(value))
    }

def compute_diff(
    current_framedict: dict[str, Any],
    new_framedict: dict[str, Any],
) -> dict[str, Any]:
    """
    Extract only changes
    """
    return {
        key: value
        for key, value in new_framedict.items()
        if (
            key not in current_framedict
            or value != current_framedict[key]
        )
    }