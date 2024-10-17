#!/usr/bin/python3
def canUnlockAll(boxes):
    # Initialize a set to track boxes that can be opened
    opened_boxes = {0}  # The first box (0) is already unlocked
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_key = keys.pop()  # Get a key
        for key in boxes[current_key]:  # Iterate through the keys in the current box
            if key not in opened_boxes:  # If this box hasn't been opened yet
                opened_boxes.add(key)  # Mark it as opened
                keys.append(key)  # Add the key to the list for further unlocking

    # Check if all boxes can be opened
    return len(opened_boxes) == len(boxes)
