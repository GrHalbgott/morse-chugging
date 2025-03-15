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
    morse_to_midi_converter = midi_generator.MorseToMidi(
        morse_code=morse_data,
        tempo=args.tempo,
        root_note=file_manager.load_asset("midi_notes")[args.root_note],
        scale=args.scale,
        song=args.song,
    )
    midi = morse_to_midi_converter.convert()

    logger.info("Saving MIDI file...")
    try:
        file_manager.save_to_file(args.output_file, midi)
    except PermissionError:
        logger.error(
            "Permission denied. Please close the output file and ensure that you have writing rights at that location."
        )
        exit(1)

    logger.info(f"Finished! Enjoy your chugging: {args.output_file}")


if __name__ == "__main__":
    main()
