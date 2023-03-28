from PIL import Image
import numpy as np
from pathlib import Path

figure_dir = Path(__file__).parent.parent / 'figures'


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


def blur(array, neighbour_size=1):
    blurred = np.zeros(array.shape)
    voisinage = [(dy, dx) for dy in range(-neighbour_size, neighbour_size+1)
                 for dx in range(-neighbour_size, neighbour_size+1)]
    h, w = array.shape
    for i in range(h):
        for j in range(w):
            for di, dj in voisinage:
                if i+di < 0:
                    di = - 1 - di
                if i+di >= h:
                    di = 1 - di
                if j+dj < 0:
                    dj = - 1 - dj
                if j+dj >= h:
                    dj = 1 - dj
                blurred[i, j] += array[i+di, j+dj]
    return np.uint8(blurred / len(voisinage))


def edge(array, neighbour_size=1):
    ret = array.astype(np.float64) - blur(array, neighbour_size=neighbour_size)
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
    save_gray_array_as_img(blur(poivrons, neighbour_size=4), "poivrons-very-blurry")
    save_gray_array_as_img(edge(poivrons), "fine-edge-poivrons")
    save_gray_array_as_img(edge(poivrons, neighbour_size=4), "coarse-edge-poivrons")

    save_rgb_array_as_img(red(), "red")
    save_rgb_array_as_img(green(), "green")
    save_rgb_array_as_img(blue(), "blue")
    save_rgb_array_as_img(rgb_squares(), "rgb-squares")
    save_rgb_array_as_img(rgb_venn(), "rgb-venn")


if __name__ == "__main__":
    main()
