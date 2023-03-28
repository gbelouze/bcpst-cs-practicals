import matplotlib.pyplot as plt
from pathlib import Path

# plt.style.use("seaborn")

# See https://jwalton.info/Embed-Publication-Matplotlib-Latex/ for instructions
# on working with matplotlib and LaTeX
tex_fonts = {
    "text.usetex": True,
    "font.family": "serif",
    "axes.labelsize": 10,
    "font.size": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 300
}
plt.rcParams.update(tex_fonts)

figure_dir = Path(__file__).parent.parent / "figures"


def get_size(width=512, fraction=1, figure_ratio="golden", subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string
            Document width in points, or string of predined document type
            Default to 345 which is the output of \\showthe\\textwidth in my LaTeX document
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    figure_ratio: float or string
            Height / width figure ratio. Defaults to the golden ratio
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width == "thesis":
        width_pt = 426.79135
    elif width == "beamer":
        width_pt = 307.28987
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    if figure_ratio == "golden":
        figure_ratio = (5**0.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * figure_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)


def set_size(width=345, ratio=1, figure_ratio="golden"):
    plt.gcf().set_size_inches(get_size(width=width, fraction=ratio, figure_ratio=figure_ratio))


def clear_plot():
    """Clear current matplotlib axis
    """
    plt.clf()
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
