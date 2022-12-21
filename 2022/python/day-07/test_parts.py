from src.bin.helpers import process_part1, process_part2
import pytest


INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test_part1():
    assert process_part1(INPUT) == 95437


@pytest.mark.skip(reason="Not implemented yet")
def test_part2():
    assert process_part2(INPUT) == 19