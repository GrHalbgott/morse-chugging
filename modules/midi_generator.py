#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from midiutil import MIDIFile

import modules.file_manager as file_manager


class MorseToMidi:
    def __init__(self, morse_code, tempo, root_note, scale, song):
        self.morse_code = morse_code
        self.tempo = tempo
        self.root_note = root_note
        self.scale = scale
        self.song = song

        self.sixteenth_note = 0.25
        self.eight_note = 0.5
        self.midi, self.tracks = self.create_midi_file()

    def create_midi_file(self):
        if self.song:
            midi = MIDIFile(3)
        else:
            midi = MIDIFile(1)
        midi, tracks = self.create_tracks(midi)
        midi.addTempo(track=0, time=0, tempo=self.tempo)
        return midi, tracks

    def create_tracks(self, midi):
        guitar_track = 0
        guitar_channel = 0
        midi.addTrackName(guitar_track, 0, "Guitar")
        midi.addProgramChange(guitar_track, guitar_channel, 0, 30)

        if self.song:
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

    def enhance_drums(self, total_time):
        drum_notes = {
            "snare": 40,
            "china": 52,
            "crash": 49,
        }

        # China
        for time in range(0, int(total_time)):  # every beat
            self.midi.addNote(
                track=self.tracks["drums"][0],
                channel=self.tracks["drums"][1],
                pitch=drum_notes["china"],
                time=time,
                duration=self.sixteenth_note,
                volume=100,
            )

        # Snare
        for time in range(2, int(total_time), 4):  # start on 3rd beat and repeat every 4 beats
            self.midi.addNote(
                track=self.tracks["drums"][0],
                channel=self.tracks["drums"][1],
                pitch=drum_notes["snare"],
                time=time,
                duration=self.sixteenth_note,
                volume=100,
            )

        # Crash
        for time in range(0, int(total_time), 16):  # start on 1st and repeat every 16 beats
            self.midi.addNote(
                track=self.tracks["drums"][0],
                channel=self.tracks["drums"][1],
                pitch=drum_notes["crash"],
                time=time,
                duration=self.sixteenth_note,
                volume=100,
            )

    def convert(self):
        if self.scale:
            scale_notes = file_manager.load_asset("scales")[self.scale]
            weights = [len(scale_notes) if num == 0 else 1 for num in scale_notes]

        time = 0
        for symbol in self.morse_code:
            if symbol == ".":
                duration = self.sixteenth_note  # Short duration for dot (16)
            elif symbol == "-":
                duration = self.eight_note  # Longer duration for dash (8)
            elif symbol == " ":
                time += self.sixteenth_note  # Short pause between letters (16)
                continue
            elif symbol == "/":  # Skip word end (16 + 16 = eighth note)
                continue
            elif symbol == "\n":
                time += self.eight_note  # Longer pause between sentences (16 + 8 + 16 = quarter note)
                continue
            else:
                continue

            if self.scale:
                pitch = self.root_note + random.choices(scale_notes, weights=weights, k=1)[0]
            else:
                pitch = self.root_note

            if self.song:
                self.midi.addNote(
                    track=self.tracks["guitar"][0],
                    channel=self.tracks["guitar"][1],
                    pitch=pitch,
                    time=time,
                    duration=duration,
                    volume=100,
                )
                self.midi.addNote(
                    track=self.tracks["bass"][0],
                    channel=self.tracks["bass"][1],
                    pitch=pitch - 12,
                    time=time,
                    duration=duration,
                    volume=100,
                )
                self.midi.addNote(
                    track=self.tracks["drums"][0],
                    channel=self.tracks["drums"][1],
                    pitch=35,
                    time=time,
                    duration=duration,
                    volume=100,
                )
            else:
                self.midi.addNote(track=0, channel=0, pitch=pitch, time=time, duration=duration, volume=100)

            time += duration  # Update time after adding the note

        if self.song:
            self.enhance_drums(time)

        return self.midi
