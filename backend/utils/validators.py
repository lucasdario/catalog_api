from typing import Type


def validate_type(value: object, type: Type, key: str):
    if not isinstance(value, type):
        raise TypeError(f"{key.capitalize()} must be {type}.")
    return value
