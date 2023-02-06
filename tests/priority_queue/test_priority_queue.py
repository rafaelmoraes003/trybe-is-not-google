from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    assert len(priority_queue) == 0

    items = [
        {"qtd_linhas": 4},
        {"qtd_linhas": 2},
        {"qtd_linhas": 8},
    ]

    # ENQUEUE

    for item in items:
        priority_queue.enqueue(item)

    assert len(priority_queue) == 3
    assert len(priority_queue.high_priority) == 2
    assert len(priority_queue.regular_priority) == 1

    # SEARCH

    assert priority_queue.search(0) == {"qtd_linhas": 4}
    assert priority_queue.search(1) == {"qtd_linhas": 2}
    assert priority_queue.search(2) == {"qtd_linhas": 8}

    with pytest.raises(IndexError):
        priority_queue.search(100)

    # DEQUEUE

    i = 0

    while i < len(priority_queue):
        assert priority_queue.dequeue() == items[i]
        i += 1
