def color_red(text: str) -> str:
    """
        Returns a string with the text in red color
    """
    return f"\033[31m{text}\033[0m"


def color_green(text: str) -> str:
    """
        Returns a string with the text in green color
    """
    return f"\033[32m{text}\033[0m"


def color_yellow(text: str) -> str:
    """
        Returns a string with the text in yellow color
    """
    return f"\033[33m{text}\033[0m"


def color_blue(text: str) -> str:
    """
        Returns a string with the text in blue color
    """
    return f"\033[34m{text}\033[0m"


def text_bold(text: str) -> str:
    """
        Returns a string with the text in bold
    """
    return f"\033[1m{text}\033[0m"
