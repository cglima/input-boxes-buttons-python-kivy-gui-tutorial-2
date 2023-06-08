from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty


# Designate Our .kv design file
Builder.load_file('update_label.kv')


class MyLayout(Widget):
    def press(self):
        # Create variables for our widget
        name = self.ids.name_input.text

        # Update the label
        self.ids.name_label.text = f'Hello {name}!'
        # clear input box
        self.ids.name_input.text = ""


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
