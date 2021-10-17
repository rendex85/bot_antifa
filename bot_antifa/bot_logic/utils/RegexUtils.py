import re


def compare_add_text(add_string: str) -> bool:
    regex_string = r'^!добавить .{1,4096}[|].{1,4096}'
    return bool(re.match(regex_string, add_string))


def compare_remove_text(add_string: str) -> bool:
    regex_string = r'^!убрать .{1,4096}'
    return bool(re.match(regex_string, add_string))


def compare_add_simple(add_string: str) -> bool:
    regex_string = r'^!добавить .{1,4096}'
    return bool(re.match(regex_string, add_string))


def compare_ban(add_string: str) -> bool:
    regex_string = r'^!бан (\[(id|public)[0-9]{1,4096}[|].{1,4096}]|(id|public)[0-9]{1,4096}).{0,4096}'
    return bool(re.match(regex_string, add_string))


def compare_ban_command(add_string: str) -> bool:
    regex_string = r'^!бан_ком .{1,4096}'
    return bool(re.match(regex_string, add_string))


def compare_unban_command(add_string: str) -> bool:
    regex_string = r'^!разбан_ком .{1,4096}'
    return bool(re.match(regex_string, add_string))


def compare_unban(add_string: str) -> bool:
    regex_string = r'^!разбан (\[(id|public)[0-9]{1,4096}[|].{1,4096}]|(id|public)[0-9]{1,4096}).{0,4096}'
    return bool(re.match(regex_string, add_string))


def compare_chess(add_string: str) -> bool:
    regex_string = r'^[a-h][1-8][a-h][1-8]$'
    return bool(re.match(regex_string, add_string))
