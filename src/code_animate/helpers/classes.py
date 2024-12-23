from typing import NamedTuple, Any
from dataclasses import dataclass

class CleanSrcDirtySrcPair(NamedTuple):
    clean_src: str  # src to be printed
    dirty_src: str  # src with inspect code

class InspectInfo(NamedTuple):
    clean_src_lines: list[str]
    dirty_src_lines: list[str]
    dict_line_number_pair: tuple[dict[str, Any], int]
    output: Any

@dataclass
class CodeLineToDraw:
    line: str       # actual code line
    comment: str    # printed afterwards
