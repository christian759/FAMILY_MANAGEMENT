from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.core.text import LabelBase




# Define the main app class
class MyApp(App):
    def build(self):
        # Create the popup
        popup = Popup(title="Hello World", size_hint=(None, None), size=(400, 400))

        # Create the UI
        layout = ScrollView(size_hint=(None, None), size=(400, 400))
        layout.add_widget(Label(text="This is a popup screen."))
        popup.content = layout

        # Return the popup
        return popup


# Run the app
if __name__ == "__main__":
    MyApp().run()