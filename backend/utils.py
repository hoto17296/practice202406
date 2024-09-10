import json
from typing import Any, NotRequired, Type

from pydantic import Json


def encode_json(obj: Any, **kwargs) -> Json[Any]:
    """オブジェクトの値を JSON 文字列に変換しつつ、形を Json[Any] 型にして返す"""
    return json.dumps(obj, **kwargs)


def cast_json_dict[T](cls: Type[T], value: Any) -> T:
    """dict 風オブジェクトを指定した TypedDict 型に変換して返す"""
    # cls が TypedDict かどうかをチェックしたいが issubclass(cls, TypedDict) はできない (PEP 589) のでこうしている
    assert issubclass(cls, dict) and hasattr(cls, "__annotations__")
    values = {}
    for key in cls.__annotations__.keys():
        if value.get(key) is not None:
            values[key] = value.get(key)
        elif getattr(cls.__annotations__[key], "__origin__", None) is NotRequired:
            pass
        else:
            values[key] = None
    return cls(**values)
