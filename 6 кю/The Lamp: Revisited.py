'''
https://www.codewars.com/kata/570e6e32de4dc8a8340016dd/train/python
'''

class Lamp:

    def __init__(self,color):
        self.color = color
        self.on = False

    def toggle_switch(self):
        if self.on == False:
            self.on = True
        else:
            self.on = False

    def state(self):
        if self.on == False:
            return "The lamp is off."
        else:
            return "The lamp is on."
