"""
helper functions relating to drawing code on terminal
"""

from colorama import Fore, Back

def draw_code(
    codelines_to_draw: list[str],
    line_index: int,
) -> None:
    """
    prints code with line_number highlighted + vars
    """
    longest_codeline_length = max([len(cl.line) for cl in codelines_to_draw])

    RESET_ALL: str = Fore.RESET + Back.RESET    
    print(RESET_ALL)
    for index, codeline_to_draw in enumerate(codelines_to_draw):
        line_length: int = len(codeline_to_draw.line)
        padding = (longest_codeline_length - line_length + 2) * " " 

        if index == line_index:
            print(
                Fore.GREEN + 
                codeline_to_draw.line + 
                padding + 
                Fore.RED + 
                codeline_to_draw.comment
            )
        else:
            print(
                RESET_ALL + 
                codeline_to_draw.line + 
                padding +
                Fore.RED + codeline_to_draw.comment
            )
    print(RESET_ALL)