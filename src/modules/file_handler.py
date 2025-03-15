#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import logging

logger = logging.getLogger()


def load_from_file(filename):
    """Load content from a file."""
    try:
        with open(filename, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        logger.error(f"File {filename} not found.")
        exit(1)
    except PermissionError:
        logger.error(f"Permission denied. Please ensure that you have reading rights for {filename}.")
        exit(1)


def load_asset(filename):
    """Load an asset file."""
    try:
        with open(f"assets/{filename}.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Asset file {filename}.json not found.")
        exit(1)


def save_to_file(output_file, midi):
    """Save content to a file."""
    try:
        with open(f"{output_file}.mid", "wb") as output_file:
            midi.writeFile(output_file)
    except PermissionError:
        logger.error(
            "Permission denied. Please close the output file and ensure that you have writing rights at that location."
        )
        exit(1)
