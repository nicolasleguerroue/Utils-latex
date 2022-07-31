#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run
import os

class Server(object):
	"Initialisation de la classe Serveur"

	def __init__(self, location="HTML_render", port=10000, ip='127.0.0.1'):
		print("Initialisation...")
		self.location = location
		self.port = port
		self.ip = ip
		@route('/') 
		def ok(): 
			fichier = open("index.html", "r")
			data = fichier.read()
			fichier.close()

			return  data 


	def run(self):
		print("Localisation : " + self.location)
		print("Port : " + str(self.port))
		print("Ip : " + self.ip)
		run(host=str(self.ip), port=self.port)


if __name__ == "__main__":
	
	main = Server()
	main.run()
        

		
		






