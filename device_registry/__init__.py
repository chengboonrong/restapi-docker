from flask import Flask
import os
import markdown as md
import subprocess
app = Flask(__name__)

@app.route("/")
def index():
	currentDir = "Current directory: %s" % os.getcwd()
	with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdownFile:
		content = markdownFile.read()
		
	return md.markdown(content)

@app.route("/api")
def getUser():
	myCmd = os.popen('cat /etc/passwd | grep bash').read()
	subprocess.call(["ls", "-l", "."])
	return myCmd
