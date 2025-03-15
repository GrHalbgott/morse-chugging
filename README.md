# Morse to chugging

Morse code is a beautiful thing - consisting solely of short and long notes, you can directly translate it to MIDI data.
And this MIDI data, it rocks hard.
My dear people, it's time for some hard-hitting chugs!

## Installation

### 1. Setup new virtual environment and install poetry (package manager)

> There are two supported options to create new virtual environments, Mamba/Conda and Venv + Pip.
> We recommend using [Mamba](https://mamba.readthedocs.io/en/latest/index.html).

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

**Example**:

```shell
python src/main.py -i example/example.txt -t 120 -r E2 -s harmonic_minor --song
```

**Usage**:

```shell
python src/main.py -h
usage: src/main.py [-h] -i [-o] [-t] [-r] [-s] [--song]

Translate (text to) Morse code to a MIDI song full of (melodic) chugging.

options:
  -h, --help            show this help message and exit

required arguments:
  -i, --input_file      Input text file.

optional arguments:
  -o, --output_file     Name of output MIDI file. Default: example/midi_output.
  -t, --tempo           Tempo of the MIDI file. Default: 142 bpm.
  -r, --root_note       Root note on guitar (bass is an octave lower). Default: B0.
  -s, --scale           Snap to scale. Default: None (stay at root note).
  --song                Create full song (guitar, bass, drums)? Otherwise only one track.
```

<details>
    <summary><b>Available scales</b></summary>

| Scale Name         | Notes as intervals from root note          |
|--------------------|--------------------------------------------|
| major              | [0, 2, 4, 5, 7, 9, 11]                     |
| minor              | [0, 2, 3, 5, 7, 8, 10]                     |
| harmonic_minor     | [0, 2, 3, 5, 7, 8, 11]                     |
| dorian             | [0, 2, 3, 5, 7, 9, 10]                     |
| mixolydian         | [0, 2, 4, 5, 7, 9, 10]                     |
| phrygian           | [0, 1, 3, 5, 7, 8, 10]                     |
| lydian             | [0, 2, 4, 6, 7, 9, 11]                     |
| locrian            | [0, 1, 3, 5, 6, 8, 10]                     |
| pentatonic_major   | [0, 2, 4, 7, 9]                            |
| pentatonic_minor   | [0, 3, 5, 7, 10]                           |
| blues              | [0, 3, 5, 6, 7, 10]                        |
| whole_tone1        | [0, 1, 3, 5, 7, 9, 11]                     |
| whole_tone2        | [0, 2, 4, 6, 8, 10]                        |
| chromatic          | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]     |

</details>

## License

This project is licensed under the MIT License - see the [LICENSE file](./LICENSE) for details.
