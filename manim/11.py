from manim import *
from scipy.ndimage import convolve
import numpy as np


class Conv:
    def kernel_cst(self, n=3):
        return np.ones((n, n)) / n**2

    def kernel_gaussian(self, sigma=1, n=3):
        t = np.linspace(-1, 1, n)
        x, y = np.meshgrid(t, t)
        ret = np.exp(-(x**2 + y**2)/sigma**2 / 2)
        return ret / ret.sum()

    def blurred(self, img, kernel, n=1):
        for _ in range(n):
            img = convolve(img, kernel)
        return img


conv = Conv()


class Convolution(Scene):

    heart = np.uint8([
        [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
        [255, 255, 255,   0,   0,   0,   0, 255, 255, 255,   0,   0,   0,   0, 255, 255, 255],
        [255, 255,   0, 180, 180, 180, 180,   0, 255,   0, 180, 180, 180, 100,   0, 255, 255],
        [255,   0, 180, 180, 255, 255, 180, 180,   0, 180, 180, 180, 180, 180, 100,   0, 255],
        [255,   0, 180, 255, 255, 180, 180, 180, 180, 180, 180, 180, 180, 180, 100,   0, 255],
        [255,   0, 180, 255, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 100,   0, 255],
        [255,   0, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 100,   0, 255],
        [255,   0, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 100,   0, 255],
        [255, 255,   0, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 100,   0, 255, 255],
        [255, 255, 255,   0, 180, 180, 180, 180, 180, 180, 180, 180, 100,   0, 255, 255, 255],
        [255, 255, 255, 255,   0, 180, 180, 180, 180, 180, 180, 100,   0, 255, 255, 255, 255],
        [255, 255, 255, 255, 255,   0, 180, 180, 180, 180, 100,   0, 255, 255, 255, 255, 255],
        [255, 255, 255, 255, 255, 255,   0, 180, 180, 100,   0, 255, 255, 255, 255, 255, 255],
        [255, 255, 255, 255, 255, 255, 255,   0, 100,   0, 255, 255, 255, 255, 255, 255, 255],
        [255, 255, 255, 255, 255, 255, 255, 255,   0, 255, 255, 255, 255, 255, 255, 255, 255],
        [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    ])

    def imageAsMobject(self, arr):
        ret = ImageMobject(arr)
        ret.height = 2
        ret.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        return ret

    def construct(self):
        imgs1 = Group(*(self.imageAsMobject(conv.blurred(self.heart, conv.kernel_cst(), n))
                      for n in range(4)))
        imgs2 = Group(*(self.imageAsMobject(conv.blurred(self.heart, conv.kernel_gaussian(), n))
                      for n in range(4)))
        imgs = Group(imgs1, imgs2)
        imgs2.arrange()
        self.add(imgs2)
