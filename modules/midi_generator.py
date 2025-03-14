#!/usr/bin/env python
# -*- coding: utf-8 -*-


from midiutil import MIDIFile


def morse_to_midi(morse_code, tempo, root_note):
    """Convert Morse code to a MIDI file."""
    track = 0
    channel = 0
    time = 0

    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)

    sixteenth_note = 0.25
    eight_note = 0.5

    for symbol in morse_code:
        if symbol == ".":
            duration = sixteenth_note  # Short duration for dot (16)
        elif symbol == "-":
            duration = eight_note  # Longer duration for dash (8)
        elif symbol == " ":
            time += sixteenth_note  # Short pause between letters (16)
            continue
        elif symbol == "/":  # Skip word end (16 + 16 = eighth note)
            continue
        elif symbol == "\n":
            time += eight_note  # Longer pause between sentences (16 + 8 + 16 = quarter note)
            continue
        else:
            continue

        midi.addNote(track, channel, root_note, time, duration, 100)
        time += duration  # Update time after adding the note

    return midi
