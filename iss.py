#!/bin/python3

import json
import turtle
import urllib.request

url2 = 'http://api.open-notify.org/iss-now.json'
resposta2 = urllib.request.urlopen(url2)
resultado2 = json.loads(resposta2.read())
local = resultado2['iss_position']
latitude = local['latitude']
longitude = local['longitude']
print()
print(f'Latitude: {latitude}')
print(f'Longitude: {longitude}')
print()

url = 'http://api.open-notify.org/astros.json'
resposta = urllib.request.urlopen(url)
resultado = json.loads(resposta.read())
print('No momento tem pessoas', resultado['number'], 'no espaço!')
pessoas = resultado['people']

for p in pessoas:
    print(p['name'], ' está na  ', p['craft'])

"""""
tela = turtle.Screen()
tela.bgpic('mapa.jpg')
tela.setup(720, 360)
tela.setworldcoordinates(-180, -90, 180, 90)


iss.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(longitude, latitude)
"""""