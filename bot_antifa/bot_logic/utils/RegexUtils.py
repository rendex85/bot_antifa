import re


def compare_add_text(add_string: str) -> bool:
    regex_string = r'^!добавить .{1,4096}[|].{1,4096}'
    return bool(re.match(regex_string, add_string))


def compare_add_media(add_string: str) -> bool:
    regex_string = r'^!добавить .{1,4096}[|]media_key'
    return bool(re.match(regex_string, add_string))
