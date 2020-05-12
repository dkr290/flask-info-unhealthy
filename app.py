import os, platform
import socket
from flask import Flask
from multiprocessing import Value

counter = 0

app = Flask(__name__)



@app.route('/')
def hostname():
    hostname = socket.gethostname()
    global counter 
    
    if counter >= 5:
        counter = 0
        return 'bad request!', 500
        
    else:
        counter += 1
        return "The hostname is " + hostname + " and IP: " + socket.gethostbyname(hostname) 
@app.route('/osrelease')
def os_release():
    return "The os name is " + os.name + "| system: "  + platform.system() + "| architecture: " + str(platform.architecture())  + "| release: " + platform.release()  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
