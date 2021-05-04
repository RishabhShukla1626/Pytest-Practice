from companies.naive import fibonacci_naive, fibonacci_cached
import pytest
from typing import Callable, List, Tuple, Dict
from companies.fixtures import time_tracker

def test_naive():
    res = fibonacci_naive(0)
    assert res == 0

    res = fibonacci_naive(5)
    assert res == 5

    res = fibonacci_naive(6)
    assert res == 8

    res = fibonacci_naive(8)
    assert res == 21

    res = fibonacci_naive(20)
    assert res == 6765


"""The above code is redundent, let's write parameterize tests"""


@pytest.mark.parametrize("value, result", [(0, 0), (5, 5), (6, 8), (8, 21), (20, 6765)])
def test_naive2(value, result):
    res = fibonacci_naive(value)
    assert res == result


"""Parametrize implementation from scratch"""

Decorator = Callable


def get_list_of_kwargs_for_function(
    identifiers: str, values: List[Tuple[int, int]]
) -> List[Dict[str, int]]:
    print(f"getting list of kwargs for function,\n{identifiers=}, {values=}")
    parsed_identifiers = identifiers.split(",")
    list_of_kwargs_for_function = []
    for tuple_value in values:
        kwargs_for_function = {}
        for i, keyword in enumerate(parsed_identifiers):
            kwargs_for_function[keyword] = tuple_value[i]
        list_of_kwargs_for_function.append(kwargs_for_function)

    print(f"{list_of_kwargs_for_function=}")
    return list_of_kwargs_for_function


def my_parametrized(identifiers: str, values: List[Tuple[int, int]]) -> Decorator:
    def my_parametrized_decorator(function: Callable) -> Callable:
        def run_func_parametrized() -> None:
            list_of_kwargs_for_function = get_list_of_kwargs_for_function(
                identifiers=identifiers, values=values
            )
            for kwargs_for_function in list_of_kwargs_for_function:
                print(
                    f"calling function {function.__name__} with  {kwargs_for_function=}"
                )
                function(**kwargs_for_function)

        return run_func_parametrized

    return my_parametrized_decorator

@my_parametrized(identifiers= "val,result", values=[(0, 0), (5, 5), (6, 8), (8, 21), (20, 6765)])

def test_naive3(val, result):
    res = fibonacci_naive(val)
    assert res == result

@pytest.mark.parametrize("value, result", [(0, 0), (5, 5), (6, 8), (8, 21), (20, 6765)])
def test_cached(time_tracker, value, result):
    res = fibonacci_cached(value)
    time_tracker
    assert res == result