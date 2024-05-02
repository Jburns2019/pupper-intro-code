#!/usr/bin/env python3

from src.MovementGroup import MovementGroups

def move():
    move = MovementGroups()

    move.move_forward()

    MovementLib = move.MovementLib

if __name__ == "__main__":
    move()