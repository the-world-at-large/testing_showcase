import time


def slow_function():
    time.sleep(0.1)
    return "done"


def test_perf(benchmark):
    result = benchmark(slow_function)
    assert result == "done"
