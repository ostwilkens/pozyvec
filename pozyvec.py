#%%
import drawSvg
import opensimplex
import time

drawSvg.Drawing

def noise(coords, frequency=1, amplitude=1, octaves=1, lacunarity=2, gain=0.5):
    octave_amplitude = amplitude
    octave_frequency = frequency
    result = 0
    for i in range(octaves):
        if type(coords) is int:
            result += octave_amplitude * opensimplex.noise2(
                coords * octave_frequency, 0
            )
        elif len(coords) == 1:
            result += octave_amplitude * opensimplex.noise2(
                coords[0] * octave_frequency, 0
            )
        elif len(coords) == 2:
            result += octave_amplitude * opensimplex.noise2(
                coords[0] * octave_frequency, coords[1] * octave_frequency
            )
        elif len(coords) == 3:
            result += octave_amplitude * opensimplex.noise3(
                octave_frequency * coords[0],
                octave_frequency * coords[1],
                octave_frequency * coords[2],
            )
        elif len(coords) == 4:
            result += octave_amplitude * opensimplex.noise4(
                octave_frequency * coords[0],
                octave_frequency * coords[1],
                octave_frequency * coords[2],
                octave_frequency * coords[3],
            )

        octave_amplitude *= gain
        octave_frequency *= lacunarity
    return result


class Pozyvec:
    drawing = None

    def _init(self, width, height, pixel_scale, stroke_width, stroke_color):
        self.drawing = drawSvg.Drawing(width, height, displayInline=True)
        self.drawing.setPixelScale(pixel_scale)
        self.drawing.stroke_width = stroke_width
        self.drawing.stroke_color = stroke_color
        self.drawing.current_path = None
        self.drawing.move = _move_to.__get__(pozyvec.drawing)
        self.drawing.draw = _line_to.__get__(pozyvec.drawing)
        self.drawing.finish = _finish.__get__(pozyvec.drawing)
        opensimplex.seed(int(round(time.time() * 1000)))


pozyvec = Pozyvec()


def init(width, height, pixel_scale=2, stroke_width=1, stroke_color="black"):
    pozyvec._init(width, height, pixel_scale, stroke_width, stroke_color)


def _move_to(self, x, y):
    # if there is a current path, end and append it
    if self.current_path is not None:
        self.append(self.current_path)
        self.current_path = None

    # create a new path
    self.current_path = drawSvg.Path(
        stroke_width=self.stroke_width, stroke=self.stroke_color, fill="none"
    )

    # move to x, y
    self.current_path.M(x, y)

    return self


def _line_to(self, x, y):
    # if there is no current path, create it
    if self.current_path is None:
        self.current_path = drawSvg.Path(
            stroke_width=self.stroke_width, stroke=self.stroke_color, fill="none"
        )

    # draw a line to x, y
    self.current_path.L(x, y)

    return self


def _finish(self):
    if self.current_path is not None:
        self.append(self.current_path)
        self.current_path = None

    return self


def move(x, y):
    return pozyvec.drawing.move(x, y)


def draw(x, y):
    return pozyvec.drawing.draw(x, y)


def finish():
    return pozyvec.drawing.finish()

def save(filename = None):
    if filename is None:
        filename = str(int(round(time.time() * 1000))) + ".svg"

    pozyvec.drawing.finish()
    pozyvec.drawing.saveSvg(filename)
    return pozyvec.drawing

init(100, 100)
