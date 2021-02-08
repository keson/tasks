import pytest

from src.boxes import give_boxes


def test_give_boxes_boundaries():
    """tests for parameter ValueError"""
    with pytest.raises(ValueError, match=r".* 100.*"):
        give_boxes(-1)
        give_boxes(101)


def test_give_boxes_count():
    """tests amount ot all boxes"""
    assert sum(give_boxes(6).values()) == 1
    assert sum(give_boxes(9).values()) == 1
    assert sum(give_boxes(11).values()) == 3


def test_give_boxes_group_boxes_count():
    """tests amount of group boxes"""
    assert sum(value for key, value in give_boxes(5).items() if key == 'group') == 0
    assert sum(value for key, value in give_boxes(15).items() if key == 'group') == 1
    assert sum(value for key, value in give_boxes(28).items() if key == 'group') == 2
    assert sum(value for key, value in give_boxes(99).items() if key == 'group') == 4


def test_give_boxes_group_boxes_dict():
    """tests exact function return"""
    assert give_boxes(5) == {'middle': 1}
    assert give_boxes(12) == {'big': 1, 'small': 1, 'group': 1}
    assert give_boxes(35) == {'big': 4, 'group': 2}
    assert give_boxes(95) == {'big': 10, 'middle': 1, 'group': 4}
