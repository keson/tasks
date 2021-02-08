from collections import defaultdict
from typing import Dict


def give_boxes(p_item_count: int) -> Dict:
    """returns dict of types and amounts of cartons needed to pack desired amount of items"""
    if not (0 < p_item_count < 100):
        raise ValueError('Item count has to be > 0 and < 100')

    item_count = p_item_count
    boxes_to_go = defaultdict(int)
    boxes_types = {'small': 3, 'middle': 6, 'big': 9}
    boxes_types = dict(sorted(boxes_types.items(), key=lambda x: x[1]))
    biggest_box = max(boxes_types.items(), key=lambda x: x[1])
    while item_count > 0:
        box_name, box_space = next(((key, val) for (key, val) in boxes_types.items() if val >= item_count), biggest_box)
        item_count -= box_space
        boxes_to_go[box_name] += 1
    if sum(boxes_to_go.values()) > 1:  # if more than one box, group box is added
        boxes_to_go['group'] = ((p_item_count - 1) // 27) + 1  # it is better to check space then box count

    return dict(boxes_to_go)
