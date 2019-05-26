from flask import Flask, Response
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.json import jsonify
import time
import json
import threading
from threading import Thread
import traceback
from spielfeld import Gui
from tkinter import Tk
import tkinter as tk

class Server(Thread):
    app = Flask(__name__)
    def __init__(self):
        super().__init__()
        

    def start(self):
        super().start()

    def run(self):
        self.app.run(host='0.0.0.0', port=4996)

    @app.route('/v1/roboter/start', methods=['GET'])
    def startGame():
        result = {}
        try:
            gui = Gui.getReference()
            gui.start_game()
            result = "Ok"
        except:
            result = "Failed"
            print(traceback.format_exc())
        return json.dumps(result)

    @app.route('/v1/roboter/moveAbsolute', methods=['POST'])
    def moveAbsolute():
        result = {}
        json_data = json.loads(request.get_json())
        print(request.get_json())
        gui = Gui.getReference()
        gui.moveAbsolute(int(json_data["row"]), int(json_data["column"]))
        result = "Ok"
        return json.dumps(result)

    @app.route('/v1/roboter/moveRelative', methods=['POST'])
    def moveRelative():
        result = {}
        json_data = json.loads(request.get_json())
        print(request.get_json())
        gui = Gui.getReference()
        gui.moveRelative(int(json_data["row"]), int(json_data["column"]))
        result = "Ok"
        return json.dumps(result)



# class Test(Thread):
#     def __init__(self):
#         super().__init__()

        

#     def start(self):
#         super().start()

#     def run(self):
#         gui = Gui.getReference()
#         gui.start_game()
#         gui.moveRelative(1,1)


def startGame():
    root = Tk()
    Gui(root)
    # test = Test()
    # test.start()
    root.mainloop()

server = Server()
server.start()

startGame()



