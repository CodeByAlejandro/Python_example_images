import subprocess
from PIL import Image, ImageFilter, ImageShow

# Create custom viewer to be able to set ImageMagick's display
# geometry cmd line option
class MyViewer(ImageShow.DisplayViewer):

    # Method overwrite
    def show_file(self, path, **options):
        """
        Display given file.
        """
        args = ["display"]
        title = options.get("title")
        if title:
            args += ["-title", title]
        # BEGIN: ADD GEOMETRY CMD LINE OPTIONS
        geometry = options.get("geometry")
        if geometry:
            args += ["-geometry", geometry]
        # END: ADD GEOMETRY CMD LINE OPTIONS
        args.append(path)

        subprocess.Popen(args)
        return 1

# Set our custom image viewer and give it the highest priority
# in the list of viewers
ImageShow.register(MyViewer(), 0)

# img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# apply greyscale conversion
# img = img.convert('L')
# box = (100, 100, 400, 400)
# img = img.crop(box)
# img = img.rotate(180)
# img = img.resize((300, 300))
# img.save('grey.png', 'png',)

img = Image.open('./astro.jpg')
# Resize while maintaining aspect ratio to get as close ass posible to size
img.thumbnail((400, 400))
print(img.size)

# Set geometry with custom viewer to set position of image viewer on WSL2 distro
ImageShow.show(img, geometry='+450+100')
