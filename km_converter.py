from kivy.app import App
from kivy.app import Builder


class km_converter(App):
    temp=""
    def build(self):
        self.title="Convert Miles to Kilometres"
        self.root=Builder.load_file("km_converter.kv")
        return self.root
    def up(self):
        temp=int(self.root.ids.input_text.text)+1
        self.root.ids.input_text.text=str(temp)
    def down(self):
        temp=int(self.root.ids.input_text.text)-1
        self.root.ids.input_text.text=str(temp)
    def convert(self):
        temp=int(self.root.ids.input_text.text)*1.60934
        self.root.ids.label1.text=str(temp)

km_converter().run()