import os

from kivy.config import Config
# Configuración del tamaño de la ventana
Config.set("graphics", "width", "350")
Config.set("graphics", "height", "600")
Config.set("graphics", "resizable", False)  # Evita cambios de tamaño
Config.set("graphics", "multisamples", "0")  # Desactiva multisampling para evitar problemas de gráficos
Config.set("kivy", "log_level", "debug")  # Modo de depuración
Config.set('graphics', 'backend', 'sdl2')  # Usa SDL2 explícitamente
Config.set("graphics", "vsync", "0")

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle



class SplashScreen(BoxLayout):
    def __init__(self, on_finish, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (1, 1)
        self.size = (350, 600)

        # Fondo blanco
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Blanco
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)


        logo_path = os.path.abspath("app/assets/logo/logo.png")
        if not os.path.exists(logo_path):
            print(f"Error: La imagen no existe en {logo_path}")
        else:
            print(f"Imagen encontrada: {logo_path}")

        try:
            self.logo = Image(
                source=logo_path,
                size_hint=(None, None),
                size=(400, 400),
                pos_hint={"center_x": 0.5, "y": 0.5},
            )
            print(f"Logo loaded successfully: {self.logo}")
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.logo = Label(
                text="Logo no encontrado",
                font_size="20sp",
                color=(0, 0, 0, 1),
            )

        self.add_widget(self.logo)

        # Programar la transición
        Clock.schedule_once(lambda dt: on_finish(), 2)

    def _update_rect(self):
        """Actualiza el fondo al cambiar tamaño/posición."""
        if hasattr(self, 'rect'):  # Asegúrate de que 'rect' existe
            self.rect.size = self.size
            self.rect.pos = self.pos

