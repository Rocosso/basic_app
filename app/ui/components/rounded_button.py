from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import ListProperty


class RoundedButton(ButtonBehavior, BoxLayout):
    bg_color = ListProperty([0.2, 0.6, 1, 1])  # Color predeterminado (RGBA)

    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.text = text

        # Canvas para el fondo redondeado
        with self.canvas.before:
            self.bg_color_instruction = Color(*self.bg_color)
            self.bg_rect = RoundedRectangle(radius=[20], size=self.size, pos=self.pos)

        # Etiqueta del texto
        self.label = Label(
            text=self.text,
            font_size="18sp",
            color=(1, 1, 1, 1),  # Texto blanco
        )
        self.add_widget(self.label)

        # Vincula cambios en tamaño, posición y color
        self.bind(pos=self._update_rect, size=self._update_rect, bg_color=self._update_color)

    def _update_rect(self, *args):
        """Actualiza el fondo al cambiar tamaño o posición."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def _update_color(self, *args):
        """Actualiza el color de fondo al cambiar `bg_color`."""
        self.bg_color_instruction.rgba = self.bg_color
