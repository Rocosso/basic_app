from kivy.uix.progressbar import ProgressBar
from kivy.graphics import PushMatrix, PopMatrix, Rotate


class VerticalProgressBar(ProgressBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Rotación de 90 grados
        with self.canvas.before:
            PushMatrix()
            self.rotation = Rotate(origin=self.center, angle=90)

        with self.canvas.after:
            PopMatrix()

        # Vincular cambios en tamaño/posición
        self.bind(pos=self._update_rotation, size=self._update_rotation)

    def _update_rotation(self, *args):
        """Actualiza el origen de la rotación al cambiar el tamaño o la posición."""
        self.rotation.origin = self.center