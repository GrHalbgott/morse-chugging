#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json


def load_from_file(filename):
    """Load content from a file."""
    with open(filename, "r") as file:
        return file.read().strip()


def load_asset(filename):
    """Load an asset file."""
    with open(f"assets/{filename}.json", "r") as f:
        return json.load(f)


def save_to_file(output_file, midi):
    """Save content to a file."""
    with open(f"{output_file}.mid", "wb") as output_file:
        midi.writeFile(output_file)
