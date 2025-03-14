#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import logging

import modules.file_manager as file_manager


def encode_to_morse(text):
    """Encode text to Morse code."""
    morse_dict = file_manager.load_asset("morse_dict")
    morse_code = []
    for char in text.upper():
        if char == " ":
            morse_code.append("/")  # Split words
        elif char in morse_dict:
            morse_code.append(morse_dict[char])
    return " ".join(morse_code)


def args_parser():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Translate (text to) Morse code to a MIDI song full of chugging."
    )
    required_args = parser.add_argument_group("required arguments")
    optional_args = parser.add_argument_group("optional arguments")

    required_args.add_argument(
        "-i",
        "--input_file",
        required=True,
        dest="input_file",
        type=str,
        metavar="\b",
        help="Input text file.",
    )
    optional_args.add_argument(
        "-o",
        "--output_file",
        dest="output_file",
        type=str,
        metavar="\b",
        help="Name of output MIDI file. Default: midi_output.mid.",
        default="midi_output.mid",
    )
    optional_args.add_argument(
        "-t",
        "--tempo",
        dest="tempo",
        type=int,
        metavar="\b",
        help="Tempo of the MIDI file. Default: 142 bpm.",
        default=142,
    )
    optional_args.add_argument(
        "-r",
        "--root_note",
        dest="root_note",
        type=str,
        metavar="\b",
        help="Root note on guitar. Default: B0.",
        default="B0",
    )

    return parser


def init_logger(name, log_file_name=None):
    """
    Set up a logger instance with stream and file logger
    :return:
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m-%d-%Y %I:%M:%S",
    )
    # Add stream handler
    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.INFO)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)
    # Log file handler
    if log_file_name:
        assert log_file_name.parent.exists(), "Error during logger setup: Directory of log file does not exist."
        filehandler = logging.FileHandler(filename=log_file_name)
        filehandler.setLevel(logging.INFO)
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

    return logger
