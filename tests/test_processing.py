from typing import Any, Dict, List

from src.widget.processing import filter_by_state, sort_by_date


# Тест функции №1
# Тест на правильную сортировку по дате
def test_sort_by_date() -> Any:
    input_list = [{"date": "2022-03-20"}, {"date": "2022-03-18"}, {"date": "2022-03-25"}]
    expected_output = [{"date": "2022-03-18"}, {"date": "2022-03-20"}, {"date": "2022-03-25"}]
    assert sort_by_date(input_list) == expected_output


# Тест на обратную сортировку
def test_sort_by_date_reverse() -> Any:
    input_list = [{"date": "2022-03-20"}, {"date": "2022-03-18"}, {"date": "2022-03-25"}]
    expected_output = [{"date": "2022-03-25"}, {"date": "2022-03-20"}, {"date": "2022-03-18"}]
    assert sort_by_date(input_list, reverse_order=True) == expected_output


# Тест на пустой список
def test_sort_by_date_empty_list() -> Any:
    input_list: List[Any] = [Any]
    assert sort_by_date(input_list) == []


# Тест функции №2
# Тест на фильтрацию по указанному состоянию
def test_filter_by_state() -> Any:
    input_list: List[Dict[str, Any]] = [
        {"id": 1, "state": "IN_PROGRESS"},
        {"id": 2, "state": "EXECUTED"},
        {"id": 3, "state": "FAILED"},
        {"id": 4, "state": "EXECUTED"},
    ]
    expected_output: List[Dict[str, Any]] = [{"id": 2, "state": "EXECUTED"}, {"id": 4, "state": "EXECUTED"}]
    assert filter_by_state(input_list) == expected_output


# Тест на фильтрацию по другому указанному состоянию
def test_filter_by_state_custom_state() -> Any:
    input_list: List[Dict[str, Any]] = [
        {"id": 1, "state": "IN_PROGRESS"},
        {"id": 2, "state": "EXECUTED"},
        {"id": 3, "state": "FAILED"},
        {"id": 4, "state": "EXECUTED"},
    ]
    expected_output = [{"id": 1, "state": "IN_PROGRESS"}]
    assert filter_by_state(input_list, target_state="IN_PROGRESS") == expected_output
