**[释放Flask端口的方法](https://deepinout.com/flask/flask-questions/516_flask_release_python_flask_port_when_script_is_terminated.html)**

在开发和测试Flask应用时，有时会遇到端口被占用的问题，特别是在脚本终止后。以下是几种解决方法，以确保在脚本终止时正确释放Flask使用的端口。

**使用atexit模块**

通过atexit模块，可以在脚本终止时执行特定的清理函数来释放端口。

**示例：**

import atexit

import socket

from flask import Flask

 

app = Flask(__name__)

 

@app.route('/')

def hello_world():

return 'Hello, World!'

 

def release_port():

sock = socket.socket()

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('localhost', 5000))

sock.close()

 

atexit.register(release_port)

 

if __name__ == '__main__':

app.run()

![复制](file:///C:/Users/26394/AppData/Local/Temp/msohtmlclip1/01/clip_image001.png)

在这个示例中，release_port函数会在脚本终止时被调用，从而释放端口。

**使用werkzeug库**

werkzeug库中的run_simple函数可以在终止脚本时自动释放端口。

**示例：**

from flask import Flask

from werkzeug.serving import run_simple

 

app = Flask(__name__)

 

@app.route('/')

def hello():

return 'Hello, Flask!'

 

if __name__ == "__main__":

run_simple('localhost', 5000, app)

![复制](file:///C:/Users/26394/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

通过使用run_simple函数，可以确保在脚本终止时端口被正确释放。

**使用signal模块**

通过signal模块，可以捕捉和处理操作系统发送的信号，在处理程序中释放端口。

**示例：**

import signal

from flask import Flask

 

app = Flask(__name__)

 

@app.route('/')

def hello():

return 'Hello, Flask!'

 

def cleanup(signal, frame):

\# 在这里释放端口的逻辑

pass

 

signal.signal(signal.SIGINT, cleanup)

signal.signal(signal.SIGTERM, cleanup)

 

if __name__ == "__main__":

app.run()

![复制](file:///C:/Users/26394/AppData/Local/Temp/msohtmlclip1/01/clip_image003.png)

在这个示例中，注册了两个信号处理程序，分别处理SIGINT和SIGTERM信号，以确保在接收到这些信号时释放端口**[2](https://geek-docs.com/flask/flask-questions/516_flask_release_python_flask_port_when_script_is_terminated.html)**。

通过以上方法，可以有效地解决Flask应用在脚本终止后端口被占用的问题，为开发提供更方便和高效的环境。

 