# PNG Prompt Exporter with Exiftool

Extract all positive prompts from PNG images (with StableDiffusion metadata) in a folder and its subfolders, and export them to a text file.

## Features

- Recursive search in all subfolders
- Uses exiftool for accurate metadata reading (parameters field)
- Parses and cleans JSON found in the parameters field
- Outputs `filename : prompt` lines in a TXT file

## Usage

### Prerequisites

- Python 3.6+
- [Exiftool](https://exiftool.org/) installed on your system

### Install

1. Download or clone this repo
2. Install exiftool and set its path in the script (see `EXIFTOOL_PATH`)
3. Place the script in the folder where your PNG files are, run it with `python extract_pos_prompt_png.py`

### Output

- Creates `positive_prompts.txt` with one line per file:  
  `path/to/image.png : prompt text`

## Credits

Script made with the assistance of GitHub Copilot Chat. Free to use and share!