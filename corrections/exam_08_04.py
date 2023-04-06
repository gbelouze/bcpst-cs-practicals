import numpy as np
from PIL import Image
from pathlib import Path

figure_dir = Path(__file__).parent.parent / 'figures' / 'exams'


def load_as_gray_array(name):
    img = Image.open(figure_dir / f'{name}.png').convert('L')
    return np.asarray(img).copy()


def save_gray_array_as_img(array, name):
    img = Image.fromarray(array).convert('L')
    img.save(figure_dir / "{}.png".format(name), format='PNG')


def hflip(im):
    return im[::, ::-1]


def vflip(im):
    return im[::-1, ::]


def transpose(im):
    return im.T


def main():
    boat = load_as_gray_array('boat')
    save_gray_array_as_img(hflip(boat), 'boat_hflip')
    save_gray_array_as_img(vflip(boat), 'boat_vflip')
    save_gray_array_as_img(transpose(boat), 'boat_transpose')


if __name__ == "__main__":
    main()
