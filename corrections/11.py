# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
from pathlib import Path

figure_dir = Path(__file__).parent.parent / 'figures' / '11'


def load_as_gray_array(name):
    img = Image.open(name).convert('L')
    return np.asarray(img).copy()


def save_gray_array_as_img(array, name):
    img = Image.fromarray(array).convert('L')
    img.save(figure_dir / "{}.png".format(name), format='PNG')


def load_as_rgb_array(name):
    img = Image.open(name).convert('RGB')
    return np.asarray(img).copy()


def save_rgb_array_as_img(array, name):
    img = Image.fromarray(array.astype(np.uint8), mode="RGB")
    img.save(figure_dir / "{}.png".format(name), format="PNG")


def blur(array, ns=1):
    """
        Blurs an image by averaging each pixel with its neighbours.
        ns is the neighbourhood size: pixels (i1, j1) and (i2, j2)
        are neighbours if max(|i1-i2|, |j1-j2|) ≤ ns
    """
    blurred = np.zeros(array.shape)
    h, w = array.shape
    for i in range(h):
        for j in range(w):
            count_neighbours = 0
            sum_neighbours = 0
            for di in range(-ns, ns+1):
                for dj in range(-ns, ns+1):
                    if 0 <= i + di < h and 0 <= j + dj < w:
                        sum_neighbours += array[i+di, j+dj]
                        count_neighbours += 1
            blurred[i, j] += sum_neighbours / count_neighbours
    return np.uint8(blurred)


def edge(array, ns=1):
    ret = array.astype(np.float64) - blur(array, ns=ns)
    ret[ret < 0] = 0
    ret[ret > 255] = 255
    return np.uint8(255 - ret)


def red():
    arr = np.zeros((100, 100, 3))
    arr[:, :, 0] = 255
    return arr


def green():
    arr = np.zeros((100, 100, 3))
    arr[:, :, 1] = 255
    return arr


def blue():
    arr = np.zeros((100, 100, 3))
    arr[:, :, 2] = 255
    return arr


def rgb_squares():
    arr = np.zeros((100, 100, 3))
    arr[:50, :50, 0] = 255
    arr[50:, :50, 1] = 255
    arr[:50, 50:, 2] = 255
    arr[50:, 50:, :] = 255
    return arr


def rgb_venn():
    arr = np.zeros((100, 100, 3))
    centers = [(35, 50), (65, 35), (65, 65)]

    t = np.arange(100)
    xx, yy = np.meshgrid(t, t)

    for i, (cy, cx) in enumerate(centers):
        arr[(xx-cx)**2 + (yy-cy)**2 < 25**2, i] = 255

    return arr


def main():
    poivrons = load_as_gray_array(figure_dir / "poivrons.png")

    save_gray_array_as_img(blur(poivrons), "poivrons-blurry")
    save_gray_array_as_img(blur(poivrons, ns=4), "poivrons-very-blurry")
    save_gray_array_as_img(edge(poivrons), "fine-edge-poivrons")
    save_gray_array_as_img(edge(poivrons, ns=4), "coarse-edge-poivrons")

    save_rgb_array_as_img(red(), "red")
    save_rgb_array_as_img(green(), "green")
    save_rgb_array_as_img(blue(), "blue")
    save_rgb_array_as_img(rgb_squares(), "rgb-squares")
    save_rgb_array_as_img(rgb_venn(), "rgb-venn")


if __name__ == "__main__":
    main()
