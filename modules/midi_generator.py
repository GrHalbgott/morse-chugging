#!/usr/bin/env python
# -*- coding: utf-8 -*-


from midiutil import MIDIFile


def create_tracks(midi, song):
    """Create tracks for the MIDI file."""
    guitar_track = 0
    guitar_channel = 0
    midi.addTrackName(guitar_track, 0, "Guitar")
    midi.addProgramChange(guitar_track, guitar_channel, 0, 30)

    if song:
        bass_track = 1
        bass_channel = 5
        midi.addTrackName(bass_track, 0, "Bass")
        midi.addProgramChange(bass_track, bass_channel, 0, 33)

        return midi, {"guitar": (guitar_track, guitar_channel), "bass": (bass_track, bass_channel)}
    else:
        return midi, {"guitar": (guitar_track, guitar_channel)}


def morse_to_midi(morse_code, tempo, root_note, song):
    """Convert Morse code to a MIDI file."""
    if song:
        midi = MIDIFile(3)
    else:
        midi = MIDIFile(1)
    midi, tracks = create_tracks(midi, song)
    midi.addTempo(track=0, time=0, tempo=tempo)

    sixteenth_note = 0.25
    eight_note = 0.5

    time = 0
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

        if song:
            midi.addNote(
                track=tracks["guitar"][0],
                channel=tracks["guitar"][1],
                pitch=root_note,
                time=time,
                duration=duration,
                volume=100,
            )
            midi.addNote(
                track=tracks["bass"][0],
                channel=tracks["bass"][1],
                pitch=root_note - 12,
                time=time,
                duration=duration,
                volume=100,
            )
        else:
            midi.addNote(track=0, channel=0, pitch=root_note, time=time, duration=duration, volume=100)

        time += duration  # Update time after adding the note

    return midi
