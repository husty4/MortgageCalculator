from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MortgageCalculator(MDApp):
    def build(self):
        return MDLabel(text = 'hello world', halign = 'center')





if __name__ == '__main__':
    MortgageCalculator().run()
