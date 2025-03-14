#!/usr/bin/env python
# -*- coding: utf-8 -*-


import modules.utils as utils
import modules.file_manager as file_manager
import modules.midi_generator as midi_generator


def main():
    logger = utils.init_logger("Morse to chugging")
    args = utils.args_parser().parse_args()

    logger.info("Converting text to Morse code...")
    morse_data = utils.encode_to_morse(file_manager.load_from_file(args.input_file))

    logger.info("Generating MIDI data...")
    midi = midi_generator.morse_to_midi(
        morse_data, args.tempo, file_manager.load_asset("midi_notes")[args.root_note], args.song, args.scale
    )

    logger.info("Saving MIDI file...")
    file_manager.save_to_file(args.output_file, midi)

    logger.info(f"Finished! Enjoy your chugging: {args.output_file}")


if __name__ == "__main__":
    main()
