

from src.code_animate import animate, framify

@animate()
def pyramid(letters: str) -> None:
    row_length: int = 1
    start_index: int = 0
    output: list[str] = []

    while start_index < len(letters):

        end_index: int = start_index + row_length

        row: str = letters[start_index: end_index]
        output.append(row)

        row_length += 1
        start_index = end_index

    return "\n".join(output)

print(pyramid("abcdefg"))
