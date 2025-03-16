#!/usr/bin/env python
# -*- coding: utf-8 -*-


import modules.utils as utils
import modules.file_handler as file_handler
import modules.midi_generator as midi_generator


def main():
    logger = utils.init_logger("Morse to chugging")
    args = utils.args_parser().parse_args()

    logger.info("Converting text to Morse code...")
    morse_data = utils.encode_to_morse(file_handler.load_from_file(args.input_file))

    logger.info("Generating MIDI data...")
    morse_to_midi_converter = midi_generator.MorseToMidi(morse_code=morse_data, args=args)
    midi = morse_to_midi_converter.convert()

    logger.info("Saving MIDI file...")
    file_handler.save_to_file(args.output_file, midi)

    logger.info(f"Finished! Enjoy your chugging: {args.output_file}")


if __name__ == "__main__":
    main()
