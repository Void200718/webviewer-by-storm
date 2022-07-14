import webbrowser
import time
import os

def clearConsole():
	command = "clear"
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)

clearConsole()

url = "https://youtu.be/HIivmyGZwiU"

while True:
	clearConsole()
	webbrowser.open_new(url)
	print('--=--')
	print("1 View Done")
	print('--=--')
	time.sleep(2)