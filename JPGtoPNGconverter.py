import sys
from pathlib import Path
from PIL import Image

if len(sys.argv) != 3:
    print("Error: Please provide 2 arguments:",
          "input directory with PNG files to process",
          "output directory to create with PNG files",
          sep="\n")
    sys.exit(1)

input_dir = Path(sys.argv[1])
output_dir = Path(sys.argv[2])

if not input_dir.is_dir():
    print("Error: First argument must be existing directory wit PNG files")

output_dir.mkdir(mode = 0o755, exist_ok = True)

for image in input_dir.iterdir():
    if image.suffix == ".jpg":
        print(f"Converting image {str(image)} ...")
        converted_image = output_dir.joinpath(image.stem + ".png")
        img = Image.open(image)
        img.save(converted_image, "png")
