#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from midiutil import MIDIFile

import modules.file_manager as file_manager


def morse_to_midi(morse_code, tempo, root_note, song, scale):
    """Convert Morse code to a MIDI file."""
    if song:
        midi = MIDIFile(3)
    else:
        midi = MIDIFile(1)
    midi, tracks = create_tracks(midi, song)
    midi.addTempo(track=0, time=0, tempo=tempo)

    sixteenth_note = 0.25
    eight_note = 0.5

    if scale:
        scale_notes = file_manager.load_asset("scales")[scale]
        weights = [8 if num == 0 else 1 for num in scale_notes]

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

        if scale:
            pitch = root_note + random.choices(scale_notes, weights=weights, k=1)[0]
        else:
            pitch = root_note

        if song:
            midi.addNote(
                track=tracks["guitar"][0],
                channel=tracks["guitar"][1],
                pitch=pitch,
                time=time,
                duration=duration,
                volume=100,
            )
            midi.addNote(
                track=tracks["bass"][0],
                channel=tracks["bass"][1],
                pitch=pitch - 12,
                time=time,
                duration=duration,
                volume=100,
            )
            midi.addNote(
                track=tracks["drums"][0],
                channel=tracks["drums"][1],
                pitch=35,
                time=time,
                duration=duration,
                volume=100,
            )
        else:
            midi.addNote(track=0, channel=0, pitch=pitch, time=time, duration=duration, volume=100)

        time += duration  # Update time after adding the note

    if song:
        midi = enhance_drums(midi, tracks, time)

    return midi


def create_tracks(midi, song):
    """Create tracks for the MIDI file."""
    guitar_track = 0
    guitar_channel = 0
    midi.addTrackName(guitar_track, 0, "Guitar")
    midi.addProgramChange(guitar_track, guitar_channel, 0, 30)

    if song:
        bass_track = 1
        bass_channel = 4
        midi.addTrackName(bass_track, 0, "Bass")
        midi.addProgramChange(bass_track, bass_channel, 0, 33)

        drums_track = 2
        drums_channel = 9
        midi.addTrackName(drums_track, 0, "Drums")

        return midi, {
            "guitar": (guitar_track, guitar_channel),
            "bass": (bass_track, bass_channel),
            "drums": (drums_track, drums_channel),
        }
    else:
        return midi, {"guitar": (guitar_track, guitar_channel)}


def enhance_drums(midi, tracks, total_time):
    """Enhance the drums track with crashes and a snare."""
    sixteenth_note = 0.25
    drum_notes = {
        "snare": 40,
        "china": 52,
        "crash": 49,
    }

    # China
    time = 0
    for time in range(0, int(total_time)):  # every beat
        midi.addNote(
            track=tracks["drums"][0],
            channel=tracks["drums"][1],
            pitch=drum_notes["china"],
            time=time,
            duration=sixteenth_note,
            volume=100,
        )

    # Snare
    time = 0
    for time in range(2, int(total_time), 4):  # start on 3rd beat and repeat every 4 beats
        midi.addNote(
            track=tracks["drums"][0],
            channel=tracks["drums"][1],
            pitch=drum_notes["snare"],
            time=time,
            duration=sixteenth_note,
            volume=100,
        )

    # Crash
    time = 0
    for time in range(0, int(total_time), 16):  # start on 1st and repeat every 16 beats
        midi.addNote(
            track=tracks["drums"][0],
            channel=tracks["drums"][1],
            pitch=drum_notes["crash"],
            time=time,
            duration=sixteenth_note,
            volume=100,
        )

    return midi
