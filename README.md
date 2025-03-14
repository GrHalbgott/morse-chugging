# Morse to chugging

Morse code is a beautiful thing - out of short and long notes, you can directly translate it to MIDI data.
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
python main.py -i text.txt -t 169 -r C3
```

**Usage**:

```shell
python main.py -h
usage: main.py [-h] -i [-o] [-t] [-r] [-s] [--octaves]

Translate (text to) Morse code to a MIDI song full of chugging.

options:
  -h, --help            show this help message and exit

required arguments:
  -i, --input_file      Input text file.

optional arguments:
  -o, --output_file     Name of output MIDI file. Default: midi_output.mid.
  -t, --tempo           Tempo of the MIDI file. Default: 142 bpm.
  -r, --root_note       Root note on guitar. Default: B0.
  --song                Create full song (guitar, bass, drums)? Otherwise only one track. Default: False.
```

## License

This project is licensed under the MIT License - see the [LICENSE file](./LICENSE) for details.
