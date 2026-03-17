class TextEditor:
    def __init__(self):
        self.document = ""
        self.history = []

    def write(self, text):
        self.history.append(self.document)
        self.document = (self.document + " " + text).strip()

    def undo(self):
        if self.history:
            self.document = self.history.pop()

e = TextEditor()
e.write("hello")
e.write("world")
e.write("war")
e.undo()
print(e.document)