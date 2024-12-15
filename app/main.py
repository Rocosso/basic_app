from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

from app.ui.views.activation_view import ActivationView
from app.ui.views.splash_screen import SplashScreen
from app.ui.views.tank_view import TankView

Config.set('graphics', 'backend', 'sdl2')  # Usa SDL2 explícitamente

class SiCallApp(App):
    def build(self):
        self.root = BoxLayout()

        # Función para abrir ActivationView
        def open_activation_view():
            self.root.clear_widgets()
            self.root.add_widget(ActivationView(controller=self.controller, go_back_callback=open_tank_view))

        # Función para volver a TankView
        def open_tank_view():
            self.root.clear_widgets()
            self.root.add_widget(TankView(controller=self.controller,
                                          open_activation_view_callback=open_activation_view))


        # Controlador de prueba
        class DummyController:
            def activate_valve(self):
                print(" Activada")
                # Todo agregar la logica que activa la electrovalvula

            def deactivate_valve(self):
                print(" Desactivada")
                # Todo agregar la logica que desactiva la electrovalvula

        self.controller = DummyController()

        def show_main_view():
            # Limpia el widget raíz y carga la vista principal
            self.root.clear_widgets()
            self.root.add_widget(ActivationView(controller=self.controller, go_back_callback=open_tank_view))

        # Inicia con el SplashScreen
        return SplashScreen(on_finish=show_main_view)


if __name__ == "__main__":
    SiCallApp().run()
