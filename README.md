# Python_example_images
Python example project to showcase working with images

# Installation
Install in virtual environment using following commands:
```shell
git clone https://github.com/CodeByAlejandro/Python_example_images.git
cd Python_example_images
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

# Usage
1. Run the `images.py` module to apply modifications to images included in pokedex source directory and write them out under a different name.
2. Run the `JPGtoPNGconverter.py` module to convert all JPG images found in the directory given as first argument on the cmd line to PNG images into the directory given as second argument on the cmd line. If the destination directory does not exist, it will be created.

## Examples
```shell
python images.py
```
```shell
python JPGtoPNGconverter.py pokedex new
```

# Uninstall
Deactivate the virtual environment using the exported shell function `deactivate`:
```shell
deactivate
```
Remove the project:
```shell
cd ..
rm -rf Python_example_images
```
