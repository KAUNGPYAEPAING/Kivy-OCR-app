# Simple Kivy OCR app

Developed By Aung Kaung Pyae Paing

Making Optical character recognition (OCR) app using Python and Kivy. This project is based on only image processing without any machine learning or deep learning methods. In order to make the system more accurate, you need to use deep learning methods.

# Require Packages
Python
Kivy
opencv
pytesseract

#How to use the system
You just need to run this program in one of the code editors, which I use as Visual Studio code. If you have all the packages, the program will run without a problem.

<img width="771" alt="Screenshot 2566-10-10 at 00 55 35" src="https://github.com/aungkaungpyaepaing/Kivy-OCR-app/assets/88584127/0409419a-31cf-496e-8e18-f1d24f350682">

#How this program work
First it will take a picture as soon as "Click Here" button is clicked. Then it is going to tranform the capture image into white by using <img width="413" alt="Screenshot 2566-10-10 at 00 58 57" src="https://github.com/aungkaungpyaepaing/Kivy-OCR-app/assets/88584127/42429168-00f6-4662-836f-586ee5188856">
After that, it is going to tranform the image using threshold method <img width="556" alt="image" src="https://github.com/aungkaungpyaepaing/Kivy-OCR-app/assets/88584127/d1732fd0-ddcb-474c-8017-03c426172637"> so that it would be easier to transform into text from image by using pytesseract <img width="542" alt="Screenshot 2566-10-10 at 01 02 55" src="https://github.com/aungkaungpyaepaing/Kivy-OCR-app/assets/88584127/1d155c0f-af31-40b3-94f5-70e44c84ec31">

Note- This project only use image processing method and pytesseract. Based on the image and what you want to do, there could be better way. Normally OCR app use Deep learning methods.
