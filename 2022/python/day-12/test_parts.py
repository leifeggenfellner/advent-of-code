from src.bin.helpers import process_part1, process_part2
import pytest

INPUT = """"""


def test_part1():
    assert process_part1(INPUT) == 13140


@pytest.mark.skip(reason="Not implemented yet")
def test_part2():
    assert process_part2(INPUT) == 0
