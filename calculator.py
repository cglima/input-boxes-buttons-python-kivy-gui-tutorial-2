from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

# Designate Our .kv design file
Builder.load_file('calculator.kv')

# Set the app size
Window.size = (500, 700)


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    # Create a button pressing function
    def button_press(self, button):
        # create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # create maths function
    def math_sign(self, sign):
        # create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'

    # create Function to remove las character of the box
    def remove(self):
        prior = self.ids.calc_input.text
        # remove the last item in the textbox
        prior = prior[:-1]
        # output back to the textbox
        self.ids.calc_input.text = prior

    # create a function to make textbox positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there´s a - signal already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Create a decimal function

    def dot(self):
        prior = self.ids.calc_input.text

        if "." in prior:
            pass
        else:
            # add a decimal to the end of the text
            prior = f'{prior}.'
            # output back to the text box
            self.ids.calc_input.text = prior

    # create equals to function
    def equals(self):
        prior = self.ids.calc_input.text

        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            # loop thru our list
            for number in num_list:
                answer = answer + float(number)

            # print the answer in the text box
            self.ids.calc_input.text = str(answer)


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
