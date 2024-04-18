#!/usr/bin/python3
'''The module provides function definition to check if all the boxes of
the lockboxes problem are unlockable'''


def canUnlockAll(boxes):
    '''The function checks if all the boxes in a lockboxes problem
    are unlockable'''
    num_doors = len(boxes)
    unlockable = [False for i in range(num_doors)]
    keys = [0]
    while len(keys):
        new_keys = []
        for key in keys:
            if key < num_doors and not unlockable[key]:
                unlockable[key] = True
                new_keys.extend(boxes[key])
        keys = new_keys

    return all(unlocked for unlocked in unlockable)
