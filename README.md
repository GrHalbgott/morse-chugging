# Morse to (melodic) chugging

Morse code is a beautiful thing - consisting solely of short and long notes as well as pauses, you can directly translate it to MIDI data. And this MIDI data, it rocks hard.

**My dear people, it's time for some hard-hitting chugs!**

> Possible applications (checkout [examples](./README.md#example-1-chugs-song)):
> - Create a melody line to be directly used in the DAW of your choice based on a Morse code, which is encoded from an input text on-the-fly
> - Create a MIDI song with a given song structure and three instruments playing chugs or melodies based on a Morse code, which is encoded from an input text on-the-fly

***More to come, stay tuned!***

## Installation

### 1. Setup new virtual environment and install poetry (package manager)

> There are two supported options to create new virtual environments, Mamba/Conda and Venv + Pip.
> Using [Mamba](https://mamba.readthedocs.io/en/latest/index.html) is recommended.

Using [Mamba](https://mamba.readthedocs.io/en/latest/index.html) (if using [Conda](https://docs.conda.io/en/latest/), replace `mamba` with `conda` below):

```shell
mamba env create --file environment.yaml
mamba activate morse-chugging
```

Using venv and pip (built-in):

```shell
sudo apt install python3.11 # if not installed already
python3.11 -m venv .venv
source .venv/bin/activate
python3.11 -m pip install poetry
```

### 2. Install necessary dependencies and packages using Poetry

Poetry will detect and respect any existing virtual environment that has been externally activated and will install the dependencies into that environment with:

```shell
poetry install
```

**Optional**: To update the packages to their latest suitable versions (and the poetry.lock file), run:

```shell
poetry update
```

## Run the program

There are multiple options to use the program, ranging from pure hard-hitting chugs in a song-like context to a somewhat random-sounding melody, directly usable in your DAW of choice. Checkout the examples below.

### General usage

```shell
python src/main.py -h
usage: src/main.py [-h] -i [-o] [-t] [-r] [-s] [--song]

Translate (text to) Morse code to a MIDI track full of (melodic) chugging.

options:
  -h, --help            show this help message and exit

required arguments:
  -i, --input_file      Input text file.

optional arguments:
  -o, --output_file     Name of output MIDI file. Default: example/midi_output.
  -t, --tempo           Tempo of the MIDI file. Default: 120 bpm.
  -r, --root_note       Root note on guitar (bass is an octave lower). Default: E1.
  -s, --scale           Scale to create melody. Default: None (stay at root note).
  -oct, --octaves       Octaves to play the scale in (1-4). Default: 1.
  --song                Create full song (guitar, bass, drums)? Otherwise only one track (piano).
```

> **Note**: Conduct the file [scales.json](./assets/scales.json) for all available scales.

### Example 1: chugs song

```shell
python src/main.py -i example/example.txt -o example/chugs -r B0 -t 142 --song
```

Produces a track with three instruments (Guitar, Bass, Drums). The tempo is 142 bpm, the root note is B0 and the instruments only play the root note. The intro consists of a half note pause and two ride hits, each a quarter note long, then the chugging starts. On the first beat of every 4 bars, a crash is played, a china on every beat. For tracks longer than 12 bars, the drum introduces variability by looping through 8 bars of china cymbal and 8 bars of open hi-hat. The ending is a final hit of bass drum, snare, and a crash.


### Example 2: melodic riffage

```shell
python src/main.py -i example/example.txt -o example/melodic_riffage -s harmonic_minor --song
```

Produces a track with three instruments (Guitar, Bass, Drums). The tempo is 120 bpm, the root note is E1 and the instruments play a melody based on the harmonic minor scale with a range of one octave (root note still plays more often than the other notes). Otherwise similar song structure as above.

### Example 3: melody creation

```shell
python src/main.py -i example/example.txt -o example/melody -t 80 -r A2 -s blues_minor -oct 3
```

Produces a melody line played by a piano with tempo 80 bpm in scale blues minor with a range of 3 octaves from the root note E2. All intro and outro pauses are omitted (so no song structure), making the melody ready to be used in you DAW of choice.

### Example 4: text to Morse

```shell
python src/main.py -i example/example.txt -o example/morse -t 100 -r C3
```

Produces a Morse code played by a piano with tempo 100 bpm and root note C3 without any song structure.

### Example 5: utter chaos

```shell
python src/main.py -i example/example.txt -o example/utter_chaos -t 269 -r C0 -oct 9 -s chromatic --song
```

It's exactly that - utter chaos, with the full range of octaves, nearly every note possible, paired with thundering drums, and delivered in a lightning fast tempo. Utter chaos.

## Contribution

Any advice, proposal for improvement, or question is welcome on all communication channels!

If you want to contribute code, please use pre-commit by running:

```shell
pre-commit install
```

Using this, it is ensured that the code you provide suits the custom formatting rules before committing or creating a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE file](./LICENSE) for details.
