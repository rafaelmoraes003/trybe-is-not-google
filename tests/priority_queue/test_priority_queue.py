from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    assert len(priority_queue) == 0

    items = [
        {"qtd_linhas": 4},
        {"qtd_linhas": 2},
        {"qtd_linhas": 8},
        {"qtd_linhas": 3},
    ]

    # ENQUEUE

    for item in items:
        priority_queue.enqueue(item)

    assert len(priority_queue) == 4
    assert len(priority_queue.high_priority) == 3
    assert len(priority_queue.regular_priority) == 1

    # ---------------------

    correct_queue = [
        {"qtd_linhas": 4},
        {"qtd_linhas": 2},
        {"qtd_linhas": 3},
        {"qtd_linhas": 8},
    ]

    # ---------------------

    # SEARCH

    for i in range(len(correct_queue)):
        assert priority_queue.search(i) == correct_queue[i]

    with pytest.raises(IndexError):
        priority_queue.search(100)

    # DEQUEUE

    for i in range(len(correct_queue)):
        assert priority_queue.dequeue() == correct_queue[i]
