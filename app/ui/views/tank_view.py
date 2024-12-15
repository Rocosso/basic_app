# app/ui/views/tank_view.py
from kivy.config import Config
# Configuración del tamaño de la ventana
Config.set("graphics", "width", "350")
Config.set("graphics", "height", "600")
Config.set("graphics", "resizable", False)  # Evita cambios en tamaño
Config.set("kivy", "log_level", "debug")

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

from app.ui.components.rounded_button import RoundedButton
from app.ui.components.vertical_progress_bar import VerticalProgressBar



class TankView(BoxLayout):
    def __init__(self, controller, open_activation_view_callback, **kwargs):
        """
        Vista principal del tanque.
        :param controller: Controlador que maneja la lógica del tanque.
        :param open_activation_view_callback: Función para abrir ActivationView.
        """
        super().__init__(orientation="vertical", **kwargs)
        self.controller = controller
        self.tank_level = 80
        self.size_hint = (None, None)
        self.size = (350, 600)

        # Fondo blanco
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Blanco
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Nivel del estanque
        self.level_label = Label(
            text=f"Nivel del satisfacción: {self.tank_level}%",
            font_size="20sp",
            color=(0, 0, 0, 1),  # Texto negro
        )
        self.add_widget(self.level_label)

        # Barra de progreso vertical
        self.progress_bar = VerticalProgressBar(max=100, value=self.tank_level, size_hint=(None, None), size=(350, 450))
        self.add_widget(self.progress_bar)

        # Botón para abrir ActivationView
        self.activate_view_button = RoundedButton(
            text="Activar una funcion con un boton",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "y": 0.4},
            bg_color=(0.50, 0.80, 0.92, 1)
        )
        self.activate_view_button.bind(on_press=lambda instance: open_activation_view_callback())
        self.add_widget(self.activate_view_button)



    def _update_rect(self, instance, value):
        """Actualiza el fondo al cambiar tamaño/posición."""
        if hasattr(self, 'rect'):  # Asegúrate de que 'rect' existe
            self.rect.size = self.size
            self.rect.pos = self.pos


