from typing import Optional

# checking this function with mypy will produce no errros 
# mypy with default settings will find no isses for the types that are not declared using type hint annotations
def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'