#!/usr/bin/python3
"""a function that returns a number of given char"""


def write_file(filename="", text=""):
    """Write a str to a UTF8 text file
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as x:
        return x.write(text)
