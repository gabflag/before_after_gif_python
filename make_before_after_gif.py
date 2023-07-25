import numpy as np
from PIL import Image


def generate_comparative_gif(
        image1_path, image2_path, output_path, gif_duration=100, gif_delay=50):

    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    np_image1 = np.array(image1)
    np_image2 = np.array(image2)

    composite_image = np.hstack(
        (np_image1[:, :np_image1.shape[1] // 2], np_image2[:, np_image2.shape
                                                           [1] // 2:]))

    # Criar o GIF
    frames = []
    for i in range(0, composite_image.shape[1], 5):
        frame = composite_image.copy()
        frame[:, :i] = np_image1[:, :i]
        frame[:, i:] = np_image2[:, i:]
        frames.append(Image.fromarray(frame))

    for i in range(composite_image.shape[1], 0, -5):
        frame = composite_image.copy()
        frame[:, :i] = np_image1[:, :i]
        frame[:, i:] = np_image2[:, i:]
        frames.append(Image.fromarray(frame))

    # Salvar o GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=gif_duration,
        loop=0,
        optimize=True,
        quality=80,
        delay=gif_delay
    )


image1_path = "after.jpg"
image2_path = "before.jpg"
output_gif_path = "yourgif.gif"

generate_comparative_gif(image1_path, image2_path, output_gif_path)
