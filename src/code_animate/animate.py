import re
from functools import wraps
from typing import Any, Callable, Sequence, Optional

from .helpers.draw_helper import draw_code
from .helpers.frame_helper import filter_framedict, compute_diff
from .helpers.classes import CodeLineToDraw
from .framify import framify

from unprint import unprint

def animate(*args: Optional[Sequence[str]]) -> Callable:
    """
    Animates your function step by step, printing changes in variables at each step

    Args
        *args (Optional[Sequence[str]]): variable names you want to focus on. Only these will be printed in animation
    Returns
        (Callable) modified function with animation capabilities.
    """

    SELECTED_KEYS = {arg for arg in args if isinstance(arg, str)}
    
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:

            # framify original function
            newfunc = framify(func)

            # call modified function
            (
                clean_src_lines, 
                dirty_src_lines, 
                frames, 
                output,
            ) = newfunc(*args, **kwargs)

            current_framedict: dict[str, Any] = {}

            # comments printed after codeline in terminal
            codelines_to_draw: list[CodeLineToDraw] = [
                CodeLineToDraw(line=line, comment="") 
                for line in clean_src_lines
            ]

            for framedict, line_number in frames:

                line_index: int = line_number - 1
                
                # filter wanted pairs in framedict eg. in selected_keys, meaningful values
                framedict: dict[str, Any] = filter_framedict(framedict, SELECTED_KEYS)

                # compute difference between current_framedict and framedict
                diff: dict[str, Any] = compute_diff(current_framedict, framedict)

                # add comment to codelines_to_draw
                codelines_to_draw[line_index].comment = str(diff)

                draw_code(codelines_to_draw, line_index)
                
                input("\n>>>")
                unprint(len(clean_src_lines) + 5)

                current_framedict = framedict

            try:
                draw_code(
                    src_lines=clean_src_lines,
                    line_number=line_number,
                    vars=framedict,
                )
            except: pass

            return output

        return wrapper
    
    return decorator
