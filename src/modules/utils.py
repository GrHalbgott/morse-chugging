#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import logging

import modules.file_handler as file_handler


def encode_to_morse(text):
    """Encode text to Morse code."""
    morse_dict = file_handler.load_asset("morse_dict")
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
        description="Translate (text to) Morse code to a MIDI track full of (melodic) chugging."
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
        help="Name of output MIDI file. Default: example/midi_output.",
        default="example/midi_output",
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
        help="Root note on guitar (bass is an octave lower). Default: B0.",
        default="B0",
    )
    optional_args.add_argument(
        "-s",
        "--scale",
        dest="scale",
        type=str,
        metavar="\b",
        help="Scale to create melody. Default: None (stay at root note).",
        default=None,
    )
    optional_args.add_argument(
        "--song",
        dest="song",
        action="store_true",
        help="Create full song (guitar, bass, drums)? Otherwise only one track (piano).",
    )

    return parser


def init_logger(name):
    """Set up a stream logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%I:%M:%S",
    )
    # Add stream handler
    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.INFO)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)

    return logger
