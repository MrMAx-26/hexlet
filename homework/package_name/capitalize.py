def capitalize(input_str: str) -> str:
    if input_str == '':
        return ''
    elif not input_str:
        return None
    first_char = input_str[0].upper()
    return first_char + input_str[1:]