from dataclasses import dataclass
from typing import Any


@dataclass
class Message:
    """
    Объект параметров для отправки сообщения в вк
    """
    # TODO: Разобраться с типизацией элементов (строка или инты)
    message: str = None
    attachment: Any = None
    reply: Any = None
    forward: Any = None
    forward_mes: Any = None
    sticker: Any = None
    keyboard: Any = None
    dont_parse_links: int = 0
    disable_mentions: int = 0
