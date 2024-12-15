# # app/ui/views/activate_view.py
from kivy.config import Config
Config.set("graphics", "width", "350")
Config.set("graphics", "height", "600")
Config.set("graphics", "resizable", False)  # Evita cambios en tamaño
Config.set("kivy", "log_level", "debug")

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

from app.ui.components.rounded_button import RoundedButton



class ActivationView(BoxLayout):
    def __init__(self, controller, go_back_callback, **kwargs):
        """
        Vista de activación/desactivación de la electroválvula.
        :param controller: Controlador que maneja la lógica de la electroválvula.
        :param go_back_callback: Función para volver a TankView.
        """
        super().__init__(orientation="vertical", **kwargs)
        self.size_hint = (None, None)
        self.size = (350, 600)

        # Fondo blanco
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Blanco
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Botón para activar el IOT
        self.activate_button = RoundedButton(
            text="Activar",
            bg_color=(0.65, 0.93, 0.85, 1),  # Azul Celeste (RGBA)
            size_hint=(0.5, 0.1),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "y": 0.8},
        )
        self.activate_button.bind(on_press=lambda instance: controller.activate_valve())
        self.add_widget(self.activate_button)

        # Botón para desactivar el IOT
        self.deactivate_button = RoundedButton(
            text="Desactivar",
            size_hint=(0.5, 0.1),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "y": 0.2},
            bg_color=(0.50, 0.80, 0.92, 1)  # Azul Celeste (RGBA)
        )
        self.deactivate_button.bind(on_press=lambda instance: controller.deactivate_valve())
        self.add_widget(self.deactivate_button)

        # Botón para volver a TankView
        self.back_button = RoundedButton(
            text="nivel de satisfacción",
            size_hint=(0.5, 0.1),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "y": 0.2},
            bg_color=(0.50, 0.80, 0.92, 1)
        )
        self.back_button.bind(on_press=lambda instance: go_back_callback())
        self.add_widget(self.back_button)

    def _update_rect(self, instance, value):
        """Actualiza el fondo al cambiar tamaño/posición."""
        if hasattr(self, 'rect'):  # Asegúrate de que 'rect' existe
            self.rect.size = self.size
            self.rect.pos = self.pos
