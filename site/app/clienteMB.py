# -*- coding: utf8 -*-
# client_app.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
import socket
 
class ClientApp(MDApp):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10 )
        
        self.output_label = Label(text='Resposta do servidor será exibida aqui')
        layout.add_widget(self.output_label)

        input_box = BoxLayout(orientation='horizontal', spacing=10)
        self.input_text = TextInput(hint_text='Digite algo...')
        send_button = Button(text='Enviar', on_press=self.send_data)
        input_box.add_widget(self.input_text)
        input_box.add_widget(send_button)
        layout.add_widget(input_box)

        return layout

    def send_data(self, instance):
        self.on_start()
        data = self.input_text.text
        self.client_socket.sendall(data.encode())
        response = self.client_socket.recv(4096).decode()
        self.output_label.text = f'Resposta do servidor: {response}'
        self.on_stop()
    def on_start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 8080))
    def on_stop(self):
        self.client_socket.close()

if __name__ == '__main__':
    ClientApp().run()
