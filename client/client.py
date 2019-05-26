from tkinter import *
import requests
import json

# Diese Datei muss separat gestartet werden.

class Client():

    # (default) Fenstergröße:
    __WINDOW_WIDTH = 400
    __WINDOW_HEIGHT = 400

    # Die Ein- und Ausgabefelder
    inputRow = None
    inputColumn = None
    output = None

    def __init__(self):
        self.__root = Tk() # Initialisierung des GUI-Frameworks TKinter
        self.__root.title("Roboter - Client")
        self.__canvas = Canvas(self.__root, width=Client.__WINDOW_WIDTH, height=Client.__WINDOW_HEIGHT)  # dies ist das "Fenster" (=Zeichenfläche) der GUI

        self.__drawContent()

    def display(self):
        self.__root.mainloop()

    # Zeichne die GUI
    def __drawContent(self):
        Label(self.__root, text="Zeile (absolut oder relativ)").grid(row=0)
        Label(self.__root, text="Spalte  (absolut oder relativ)").grid(row=1)

        Client.inputRow = Entry(self.__root)
        Client.inputColumn = Entry(self.__root)

        Client.inputRow.grid(row=0, column=1)
        Client.inputColumn.grid(row=1, column=1)

        buttonAbsolute = Button(self.__root, text="absenden (absolut)", command=self.sendAbsolute)
        buttonAbsolute.grid(sticky="W", row=2, column=0)

        buttonRelative = Button(self.__root, text="absenden (relativ)", command=self.sendRelative)
        buttonRelative.grid(sticky="W", row=3, column=0)

        buttonRelative = Button(self.__root, text="Start Game", command=self.startGame)
        buttonRelative.grid(sticky="W", row=4, column=0)

        Label(self.__root, text="Rückmeldung:", anchor="w").grid(sticky="W", row=5, column = 0)
        Client.output = Label(self.__root, text="")
        Client.output.grid(sticky="W", row=5, column=1)


    # Sende die neue Roboterposition (absolut)
    @classmethod
    def sendAbsolute(event):
        Client.output.configure(text='')        # Meldung löschen

        try:
            row = Client.inputRow.get()
            column = Client.inputColumn.get()
            data = {"row": str(row), "column": str(column)}
            json_data = json.dumps(data)
            print(json_data)
            res = requests.post('http://localhost:4996/v1/roboter/moveAbsolute', json=json_data)
            Client.output.configure(text=res.text)
        except Exception as e:
            print(e)
            Client.output.configure(text='Server nicht erreichbar!')

    # Sende die neue Roboterposition (relativ)
    @classmethod
    def sendRelative(event):
        Client.output.configure(text='')        # Meldung löschen

        try:
            row = Client.inputRow.get()
            column = Client.inputColumn.get()
            data = {"row": str(row), "column": str(column)}
            json_data = json.dumps(data)
            print(json_data)
            res = requests.post('http://localhost:4996/v1/roboter/moveRelative', json=json_data)
            Client.output.configure(text=res.text)
        except Exception as e:
            print(e)
            Client.output.configure(text='Server nicht erreichbar!')



    # Setze die Roboterposition zurück
    @classmethod
    def startGame(event):
        Client.output.configure(text='')        # Meldung löschen

        try:
            req = requests.get('http://localhost:4996/v1/roboter/start')
            Client.output.configure(text=req.text)
        except:
            Client.output.configure(text='Server nicht erreichbar!')



# Erzeuge die GUI und stelle sie dar
client = Client()
client.display()