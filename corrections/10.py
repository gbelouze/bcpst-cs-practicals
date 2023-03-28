from PIL import Image
import numpy as np
from pathlib import Path
import importlib
lf = importlib.import_module("10_light_func")

figure_dir = Path(__file__).parent.parent / 'figures'


def load_as_gray_array(name):
    img = Image.open(name).convert('L')
    return np.asarray(img).copy()


def save_gray_array_as_img(array, name):
    img = Image.fromarray(array).convert('L')
    img.save(figure_dir / "{}.png".format(name), format='PNG')


def mirror(array):
    h, w = array.shape
    mirrored = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            mirrored[i, j] = array[i, w - 1 - j]
    return mirrored


def negative(array):
    h, w = array.shape
    negated = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            negated[i, j] = 255 - array[i, j]
    return negated


def negative_better(array):
    return 255 - array


def left_half(array):
    h, w = array.shape
    halved = np.zeros((h, w//2))
    for i in range(h):
        for j in range(w // 2):
            halved[i, j] = array[i, j]
    return halved


def left_half_better(array):
    h, w = array.shape
    return array[:, :w//2]
    # en numpy, on peut écrire M[a:b] pour représenter M[a], M[a+1], ..., M[b-1]
    # de la même manière qu'on écrit range(a, b) pour a, a+1, ..., b-1


def lighten(array):
    return lf.lighten(array.astype(np.float64)).astype(np.uint8)


def darken(array):
    return lf.darken(array.astype(np.float64)).astype(np.uint8)


def decontrast(array):
    return lf.decontraste(array.astype(np.float64)).astype(np.uint8)


def contrast(array):
    return lf.contraste(array.astype(np.float64)).astype(np.uint8)


poivrons = load_as_gray_array(figure_dir / "poivrons.png")

save_gray_array_as_img(mirror(poivrons), "miroir")
save_gray_array_as_img(negative(poivrons), "negatif")
save_gray_array_as_img(left_half(poivrons), "moitie_gauche")
save_gray_array_as_img(lighten(poivrons), "eclairci")
save_gray_array_as_img(darken(poivrons), "noirci")
save_gray_array_as_img(contrast(poivrons), "contraste")
save_gray_array_as_img(decontrast(poivrons), "decontraste")
