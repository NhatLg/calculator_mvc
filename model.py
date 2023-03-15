class Model:
    def __init__(self):
        self.value = ''
        self.previous_value = ''
        self.operator = ''
    def calculate(self, caption):
        if caption == 'C':
            self.value = ''
            self.previous_value = ''
            self.operator = ''
        elif isinstance(caption, int): self.value += str(caption)
        elif caption == "+/-":
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
        elif caption == "%":
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value/100)
        elif caption == ".":
            if caption not in self.value:
                self.value += "."
        elif caption == "=":
            value = str(self._evaluate())
            if ".0" in str(value):
                value = int(value)
            self.value = str(value)

        else: # for + - / *
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self):
        return eval(self.previous_value + self.operator + self.value)