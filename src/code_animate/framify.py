import inspect
from functools import wraps
from typing import Any, Callable
from textwrap import dedent

from .helpers.classes import InspectInfo
from .helpers.main_helper import gen_clean_src_dirty_src_pair
from .helpers.func_helper import create_func_from_src
from .helpers.string_helper import clean_up_src

def framify(
    func: Callable
) -> Callable:
    """
    Makes a function returns additional list[FrameType]

    eg. if a function originally "return some_number"
        it now "return frames, some_number"

    where frames is a list of inspect.frames
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> InspectInfo:
        
        # get dedented source code of original func
        src: str = clean_up_src(inspect.getsource(func))

        # modify source code: insert inspect statements
        clean_src, dirty_src = gen_clean_src_dirty_src_pair(src)

        # create function from new_src
        new_func: Callable = create_func_from_src(dirty_src)

        # return original output
        frames, output = new_func(*args, **kwargs)

        return InspectInfo(
            clean_src_lines=clean_src.split("\n"),
            dirty_src_lines=dirty_src.split("\n"),
            dict_line_number_pair=frames,
            output=output,
        )
    
    return wrapper