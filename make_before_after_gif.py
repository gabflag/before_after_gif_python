import os

import numpy as np
from PIL import Image


def resize_image(background_path, new_width):
    '''
    Transforma a imagem com a largura especificada
    sem perder suas dimensões e salva a imagem redimensionada no disco.
    '''
    background = Image.open(background_path)

    width_percent = (new_width / float(background.size[0]))
    new_height = int((float(background.size[1]) * float(width_percent)))

    resized_background = background.resize(
        (new_width, new_height), Image.LANCZOS)

    resized_background.save(background_path)

    return background_path


def compress_image(input_path, output_path, max_size):
    image = Image.open(input_path)
    quality = 95  # Qualidade inicial da imagem (0-100)

    # Loop para reduzir a qualidade até que o tamanho seja 
    # menor ou igual ao máximo permitido
    while True:
        image.save(output_path, optimize=True, quality=quality)

        # Verifica o tamanho da imagem após salvar
        if os.path.getsize(output_path) <= max_size * 1024:
            break

        # Reduz a qualidade em 5 unidades a cada iteração
        quality -= 5


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


input_image_path = 'after.jpg'
output_image_path = '01_after_reduce.jpg'
max_file_size_kb = 32
compress_image(input_image_path, output_image_path, max_file_size_kb)

input_image_path = 'before.jpg'
output_image_path = '01_before_reduce.jpg'
max_file_size_kb = 32
compress_image(input_image_path, output_image_path, max_file_size_kb)


image1_path_str = resize_image(
    "01_after_reduce.jpg", 400)

image2_path_str = resize_image(
    "01_before_reduce.jpg", 400)

output_gif_path = "yourgif.gif"

generate_comparative_gif(image1_path_str, image2_path_str, output_gif_path)
