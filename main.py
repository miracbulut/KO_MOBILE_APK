from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.utils import platform
import time

# Pencere boyutunu en başta ayarla (Kivy başlamadan önce)
if platform != 'android':
    Window.size = (400, 700)

if platform == 'android':
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    Settings = autoclass('android.provider.Settings')
    Toast = autoclass('android.widget.Toast')

class Point:
    def __init__(self, x, y, delay=0):
        self.x = x
        self.y = y
        self.delay = delay

class Manager:
    def __init__(self):
        self.points = []
        self.recording = False
        self.playing = False
        self.last_time = 0
    def start_rec(self):
        self.points = []
        self.recording = True
        self.last_time = time.time()
    def stop_rec(self):
        self.recording = False
        return len(self.points)
    def add(self, x, y):
        if not self.recording:
            return
        now = time.time()
        delay = int((now - self.last_time) * 1000) if self.points else 0
        self.last_time = now
        self.points.append(Point(x, y, delay))

class Panel(FloatLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.make_mini()
    def make_mini(self):
        self.clear_widgets()
        btn = Button(text='⚙️', size_hint=(None, None), size=(60, 60), pos=(Window.width - 70, 10), background_color=(0, 0.6, 1, 0.9), font_size='28sp')
        btn.bind(on_release=self.make_big)
        self.add_widget(btn)
    def make_big(self, *args):
        self.clear_widgets()
        box = BoxLayout(orientation='vertical', size_hint=(None, None), size=(Window.width - 20, 280), pos=(10, 10), padding=10, spacing=8)
        with box.canvas.before:
            Color(0.1, 0.1, 0.15, 0.95)
            self.bg = Rectangle(pos=box.pos, size=box.size)
        box.bind(pos=self.upd, size=self.upd)
        h = BoxLayout(size_hint_y=0.15, spacing=5)
        h.add_widget(Label(text='[b]BULUT[/b]', markup=True, font_size='20sp'))
        c = Button(text='✕', size_hint_x=0.2, background_color=(1, 0.3, 0.3, 1))
        c.bind(on_release=lambda x: self.make_mini())
        h.add_widget(c)
        box.add_widget(h)
        self.st = Label(text=f'{len(self.app.mgr.points)} nokta', size_hint_y=0.12, font_size='14sp')
        box.add_widget(self.st)
        b1 = BoxLayout(size_hint_y=0.3, spacing=5)
        self.rec = Button(text='🔴', background_color=(1, 0.2, 0.2, 1), font_size='20sp', bold=True)
        self.rec.bind(on_release=self.app.tog_rec)
        b1.add_widget(self.rec)
        self.play = Button(text='▶', background_color=(0.2, 1, 0.2, 1), font_size='20sp', bold=True)
        self.play.bind(on_release=self.app.play)
        b1.add_widget(self.play)
        self.stop = Button(text='⏹', background_color=(1, 0.7, 0, 1), font_size='20sp', bold=True, disabled=True)
        self.stop.bind(on_release=self.app.stop)
        b1.add_widget(self.stop)
        box.add_widget(b1)
        b2 = BoxLayout(size_hint_y=0.25, spacing=5)
        cl = Button(text='🗑 Temizle', background_color=(0.7, 0.2, 0.2, 1), font_size='16sp')
        cl.bind(on_release=self.app.clear)
        b2.add_widget(cl)
        box.add_widget(b2)
        if platform == 'android':
            p = Button(text='⚙️ zinler', size_hint_y=0.18, background_color=(1, 0.5, 0, 1))
            p.bind(on_release=self.app.perm)
            box.add_widget(p)
        self.add_widget(box)
    def upd(self, *args):
        if hasattr(self, 'bg'):
            self.bg.pos = self.children[0].pos
            self.bg.size = self.children[0].size

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mgr = Manager()
        
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Beyaz arka plan
        
        if platform == 'android':
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.SYSTEM_ALERT_WINDOW])
        
        main = FloatLayout()
        
        # Test butonu - ekranın ortasında büyük
        test_btn = Button(
            text='TEST\nBURAYA TIK',
            size_hint=(None, None),
            size=(200, 200),
            pos=(100, 250),
            background_color=(1, 0, 0, 1),
            font_size='30sp',
            bold=True
        )
        test_btn.bind(on_release=lambda x: print("TEST BAŞARILI!"))
        main.add_widget(test_btn)
        
        self.touch = FloatLayout()
        self.touch.bind(on_touch_down=self.on_touch)
        main.add_widget(self.touch)
        
        self.panel = Panel(self)
        main.add_widget(self.panel)
        
        return main
    def on_touch(self, inst, touch):
        if self.panel.collide_point(*touch.pos):
            return False
        if self.mgr.recording:
            self.mgr.add(touch.x, touch.y)
            with self.touch.canvas:
                Color(0, 1, 0, 0.7)
                Ellipse(pos=(touch.x - 15, touch.y - 15), size=(30, 30))
            Clock.schedule_once(lambda dt: self.touch.canvas.clear(), 0.5)
            if hasattr(self.panel, 'st'):
                self.panel.st.text = f'{len(self.mgr.points)} nokta'
            return True
        return False
    def tog_rec(self, *args):
        if self.mgr.recording:
            c = self.mgr.stop_rec()
            self.panel.rec.text = '🔴'
            self.panel.rec.background_color = (1, 0.2, 0.2, 1)
            self.msg(f'{c} nokta!')
        else:
            self.mgr.start_rec()
            self.panel.rec.text = '⏹'
            self.panel.rec.background_color = (1, 0.6, 0, 1)
            self.msg('Kayıt başladı!')
    def play(self, *args):
        if not self.mgr.points:
            self.msg('Önce kayıt yap!')
            return
        self.mgr.playing = True
        self.panel.play.disabled = True
        self.panel.stop.disabled = False
        self.panel.rec.disabled = True
        self.run_macro(0)
    def run_macro(self, idx):
        if not self.mgr.playing or idx >= len(self.mgr.points):
            self.done()
            return
        p = self.mgr.points[idx]
        with self.touch.canvas:
            Color(1, 1, 0, 0.8)
            Ellipse(pos=(p.x - 15, p.y - 15), size=(30, 30))
        Clock.schedule_once(lambda dt: self.touch.canvas.clear(), 0.3)
        if platform == 'android':
            print(f"Click: {p.x}, {p.y}")
        Clock.schedule_once(lambda dt: self.run_macro(idx + 1), p.delay / 1000.0)
    def stop(self, *args):
        self.mgr.playing = False
        self.done()
    def done(self):
        self.mgr.playing = False
        self.panel.play.disabled = False
        self.panel.stop.disabled = True
        self.panel.rec.disabled = False
    def clear(self, *args):
        self.mgr.points = []
        self.msg('Temizlendi!')
        if hasattr(self.panel, 'st'):
            self.panel.st.text = '0 nokta'
    def perm(self, *args):
        if platform == 'android':
            try:
                i = Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS)
                PythonActivity.mActivity.startActivity(i)
            except:
                pass
    def msg(self, txt):
        print(txt)
        if platform == 'android':
            try:
                Toast.makeText(PythonActivity.mActivity, txt, Toast.LENGTH_SHORT).show()
            except:
                pass

if __name__ == '__main__':
    MyApp().run()
