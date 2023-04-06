import numpy as np
import matplotlib.pyplot as plt
import plotting
from pathlib import Path

figure_dir = Path(__file__).parent.parent / "figures" / '10'


def lighten(p):
    return np.sqrt(p * 255)


def darken(p):
    return p**2 / 255


def contraste(p):
    return 255 / (2 * np.pi) * np.sin(- 2 * np.pi * p / 255) + p


def decontraste(p):
    return 255 / (2 * np.pi) * np.sin(2 * np.pi * p / 255) + p


def main():
    t = np.linspace(0, 255, 256)

    plotting.clear_plot()
    plt.plot(t, lighten(t), lw="0.4", label='eclairci')
    plt.plot(t, t, "k--", alpha=0.5, lw="0.4")
    plt.legend()
    plotting.set_size(ratio=0.4)
    plt.savefig(figure_dir / "eclair_func.png", bbox_inches="tight")

    plotting.clear_plot()
    plt.plot(t, darken(t), lw="0.4", label='noirci')
    plt.plot(t, t, "k--", alpha=0.5, lw="0.4")
    plt.legend()
    plotting.set_size(ratio=0.4)
    plt.savefig(figure_dir / "noirci_func.png", bbox_inches="tight")

    plotting.clear_plot()
    plt.plot(t, contraste(t), lw="0.4", label='contraste')
    plt.plot(t, t, "k--", alpha=0.5, lw="0.4")
    plt.legend()
    plotting.set_size(ratio=0.4)
    plt.savefig(figure_dir / "contraste_func.png", bbox_inches="tight")

    plotting.clear_plot()
    plt.plot(t, decontraste(t), lw="0.4", label='decontraste')
    plt.plot(t, t, "k--", alpha=0.5, lw="0.4")
    plt.legend()
    plotting.set_size(ratio=0.4)
    plt.savefig(figure_dir / "decontraste_func.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
