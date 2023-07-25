# before_after_gif_python

# Programming Language used:

    Python 3.11.2
    To start the program just run the file make_before_after_gif.py

# About the program:
    
    This is a Python script that generates a GIF for you. Just insert the "before" and "after" files, which must be in jpg format and named "after.jpg" and "before.jpg," respectively.
    For the program to work excellently, try to use files with the same dimensions.

# About the tests:

    On my computer, this routine took about 1 minute. Both files were 639 KB and had dimensions of 640*512. The generated GIF has 62MB, keeping the same dimensions.
    One way to reduce processing time and storage space for this GIF is by adding an image resizing layer. This significantly reduces the work needed to construct the GIF.
    Here's the code that should be added:

    def generate_comparative_gif(image1_path, image2_path, output_path, gif_duration=100, gif_delay=50, resolution=(320, 256)):
        ...

        # Resize the images to the desired resolution
        image1 = image1.resize(resolution)
        image2 = image2.resize(resolution)

    This way it decreases to 23 seconds of processing and a resulting final image with 8MB