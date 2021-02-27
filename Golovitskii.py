from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer



from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):

        s=Scatter()
        fl=FloatLayout(size=(300, 300))
        f2=FloatLayout(size=(300,300))
        s.add_widget(f2)
        s.add_widget(fl)
        fl.add_widget(Button(
            text="А я вторая",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1,0,1,1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(320, 250)));
        f2.add_widget(Button(
            text="Я первая кнопка",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1,3,0,1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(320, 330)));    
        return s
    def btn_press(self, instance):        
        instance.text='Я нажата'
        
if __name__=="__main__":
    myApp().run()
