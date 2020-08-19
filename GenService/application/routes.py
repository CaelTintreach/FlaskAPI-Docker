from random import randint
from application import app
from flask import request, Response

@app.route('/animal/name', METHOD=['GET'])
def animal_name():
	animals = ["Cat", "Dog", "Parrot"]
	return Response(animals[randint(0,2)], mimetype='text/plain')

@app.route('/animal/noise', methods=['POST'])
def animal_noise():
	animal = request.data.decode("utf-8")
	if animal == "Cat":
		noise = "Meow"
	if animal == "Dog":
		noise = "Bark"
	if animal == "Parrot":
		noise = "Caw"
	else:
		noise = "ERROR"
	return Response(noise, mimetype='text/plain')