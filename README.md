## Installation 
    pip install audio_convert
    or run setup.py install

## Intro
    This is a simple tool for converting audio files.
    There are probably better ones out there, but I needed ideas for portfolio projects.

## Usage

    audio_convert --base_name {MY_NAME_OR_DIR} --to [{NEW_EXTENSION}]
    This converts a filename or directory to the given extensions.

## Optional Args

    --from, default = [""], help = If a value is specified, the program will only convert the file if the extension matches one of the elements. 
    --out_path, default = [""], help = If a value is specified, the program will put the new files in the given directories. Else it will use the base directory that the file was found in.

## Requires
    
    pydub