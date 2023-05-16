import numpy as np


def f(x):
    return np.sin(x)


def true_integral_f(a, b):
    return np.cos(a) - np.cos(b)


def rectangle(f, u, v):
    return (v-u) * f(u)


def rectangle_composite(f, a, b, n):
    x = np.linspace(a, b, n)

    tot = 0
    for u, v in zip(x[:-1], x[1:]):
        tot += rectangle(f, u, v)

    return tot


def point_milieu(f, u, v):
    return (v-u) * f((u+v)/2)


def point_milieu_composite(f, a, b, n):
    x = np.linspace(a, b, n)

    tot = 0
    for u, v in zip(x[:-1], x[1:]):
        tot += point_milieu(f, u, v)

    return tot


def trapeze(f, u, v):
    return (v-u) * (f(u) + f(v))/2


def trapeze_composite(f, a, b, n):
    x = np.linspace(a, b, n)

    tot = 0
    for u, v in zip(x[:-1], x[1:]):
        tot += trapeze(f, u, v)

    return tot


def simpson(f, u, v):
    return (v-u) * (f(u)/6 + f(v)/6 + 4/6 * f((u+v)/2))


def simpson_composite(f, a, b, n):
    x = np.linspace(a, b, n)

    tot = 0
    for u, v in zip(x[:-1], x[1:]):
        tot += simpson(f, u, v)

    return tot


def test_methode(methode_base, methode_composite):
    a, b = 3, 4
    ns = (10, 100, 1000)
    name = methode_base.__name__
    true = true_integral_f(a, b)
    erreur_base = true - methode_base(f, a, b)
    erreurs_composite = {n: true - methode_composite(f, a, b, n) for n in ns}

    print(f"-------- Méthode du {name} --------")
    print(" {:>4}  {:<10}".format("n", "|erreur|"))
    print(" {:>4}  {:<10.5e}".format(2, np.abs(erreur_base)))
    for n, erreur in erreurs_composite.items():
        print(" {:>4}  {:<10.5e}".format(n, np.abs(erreur)))
    print()


def main():
    test_methode(rectangle, rectangle_composite)
    test_methode(point_milieu, point_milieu_composite)
    test_methode(trapeze, trapeze_composite)
    test_methode(simpson, simpson_composite)


if __name__ == "__main__":
    main()
