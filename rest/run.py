# Write a RESTful service to determine a useful piece of information of your computer

import platform
import socket
import getpass
import os
from eve import Eve

# Settings
settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'DOMAIN': {}
}

app = Eve(settings=settings)


# Function to get Processor information
@app.route('/getProcessor')
def processor():
    processorName = platform.processor()
    systemInfo = platform.system()
    architecture = platform.architecture()[0]
    return ("System Information - "
            + "<br/> Processor Name: " + processorName
            + "<br/> Operating System: " + systemInfo
            + "<br/> Architecture: " + architecture)



# Function to get User details
@app.route('/getUserData')
def user():
    username = getpass.getuser()
    hostname = socket.gethostname()
    return ("User Details - "
            + "<br/> User Name: " + username
            + "<br/> Hostname: " + hostname)


if __name__ == "__main__":
    app.run()
