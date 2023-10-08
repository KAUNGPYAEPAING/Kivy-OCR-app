from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import pytesseract

class MainApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.image = Image()
        self.label = Label() 
        layout.add_widget(self.image)
        layout.add_widget(self.label)
        layout.save_img_button = Button(
            text="Click Here",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None, None)
        )
        layout.save_img_button.bind(on_press=self.take_picture)
        layout.add_widget(layout.save_img_button)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.8 / 30.0)
        return layout

    def load_video(self, *avgs):
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def take_picture(self, *args):
        image_name = 'picture_at_2_02.png'
        img = cv2.cvtColor(self.image_frame, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        text_data = pytesseract.image_to_string(img, lang='eng', config="--psm 6")
        self.label.text = text_data

if __name__ == '__main__':
    MainApp().run()
