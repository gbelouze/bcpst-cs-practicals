from manim import *
import numpy as np


class TriBulle(Scene):

    def construct(self):
        n = 20
        l = 5 * np.arange(1, n+1) / n
        np.random.shuffle(l)

        lines = [Line([x, -3, 0], [x, l[i]-2, 0], stroke_width=20)
                 for i, x in enumerate(np.linspace(-6, 6, n))]
        self.play(LaggedStart(
            *[GrowFromEdge(line, DOWN) for line in lines],
            lag_ratio=0.1,
            run_time=2
        ))

        changed = True
        for upto in range(n-1, -1, -1):
            changed = False
            self.play(lines[0].animate.set_stroke(color=BLUE, opacity=1),
                      run_time=0.2)
            for i in range(upto):
                changed_rn = False
                if l[i] > l[i+1]:
                    changed = True
                    changed_rn = True
                    l[i], l[i+1] = l[i+1], l[i]
                    self.play(
                        lines[i].animate.set_x(lines[i+1].get_x()),
                        lines[i+1].animate.set_x(lines[i].get_x()),
                        run_time=0.2
                    )
                    lines[i], lines[i+1] = lines[i+1], lines[i]
                if not changed_rn:
                    if i < upto-2:
                        self.play(
                            lines[i].animate.set_stroke(color=WHITE, opacity=1),
                            lines[i+1].animate.set_stroke(color=BLUE, opacity=1),
                            run_time=0.2
                        )
                    else:
                        self.play(
                            lines[i].animate.set_stroke(color=WHITE, opacity=1),
                            lines[i+1].animate.set_stroke(color=BLUE, opacity=1),
                            run_time=0.2
                        )
            if not changed:
                break
        self.play(
            *(line.animate.set_stroke(color=BLUE, opacity=1) for line in lines),
            run_time=0.2
        )


class TriInsertion(Scene):

    def construct(self):
        n = 20
        l = 5 * np.arange(1, n+1) / n
        np.random.shuffle(l)

        lines = [Line([x, -3, 0], [x, l[i]-2, 0], stroke_width=20)
                 for i, x in enumerate(np.linspace(-6, 6, n))]
        self.play(LaggedStart(
            *[GrowFromEdge(line, DOWN) for line in lines],
            lag_ratio=0.1,
            run_time=2
        ))

        for i in range(1, n):
            self.play(lines[i].animate.set_stroke(color=BLUE, opacity=1), run_time=0.2)
            k = i
            x = l[i]
            goes_to = []

            while (k > 0) and (x < l[k-1]):
                k -= 1
                l[k+1] = l[k]
                goes_to.append((lines[k], lines[k+1].get_x()))
                self.play(lines[k].animate.set_stroke(color=RED, opacity=1), run_time=0.2)
            if (k > 0):
                self.play(lines[k-1].animate.set_stroke(color=GREEN, opacity=1), run_time=0.2)
            l[k] = x
            goes_to.append((lines[i], lines[k].get_x()))

            self.play(
                *(line.animate.set_x(x) for line, x in goes_to),
                run_time=0.4
            )
            self.play(
                *(lines[j].animate.set_stroke(color=WHITE, opacity=1)
                  for j in range(max(0, k-1), i+1)),
                run_time=0.2
            )
            for j in range(i, k, -1):
                lines[j], lines[j-1] = lines[j-1], lines[j]
        self.play(
            *(line.animate.set_stroke(color=BLUE, opacity=1) for line in lines),
            run_time=0.2
        )


class TriSelection(Scene):

    def construct(self):
        n = 20
        l = 5 * np.arange(1, n+1) / n
        np.random.shuffle(l)

        lines = [Line([x, -3, 0], [x, l[i]-2, 0], stroke_width=20)
                 for i, x in enumerate(np.linspace(-6, 6, n))]
        self.play(LaggedStart(
            *[GrowFromEdge(line, DOWN) for line in lines],
            lag_ratio=0.1,
            run_time=2
        ))

        for toPos in range(n-1, 0, -1):
            imax = None
            for j in range(toPos + 1):
                if imax is None or l[imax] < l[j]:
                    if imax is not None:
                        self.play(
                            lines[imax].animate.set_stroke(color=RED, opacity=1),
                            lines[j].animate.set_stroke(color=GREEN, opacity=1),
                            run_time=0.2)
                    else:
                        self.play(
                            lines[j].animate.set_stroke(color=GREEN, opacity=1),
                            run_time=0.2)
                    imax = j
                else:
                    self.play(lines[j].animate.set_stroke(color=RED, opacity=1), run_time=0.2)

            self.play(
                *(lines[j].animate.set_x(lines[j-1].get_x()) for j in range(imax+1, toPos+1)),
                lines[imax].animate.set_x(lines[toPos].get_x()),
                run_time=0.4
            )

            self.play(
                *(lines[j].animate.set_stroke(color=WHITE, opacity=1) for j in range(toPos+1)),
                lines[imax].animate.set_stroke(color=BLUE, opacity=1),
                run_time=0.2
            )
            for j in range(imax, toPos):
                lines[j], lines[j+1] = lines[j+1], lines[j]
                l[j], l[j+1] = l[j+1], l[j]
        self.play(lines[0].animate.set_stroke(color=BLUE, opacity=1), run_time=0.2)
