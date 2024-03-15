import PySimpleGUI as sg

def signup_login():
    layout = [
        [sg.Text("Login or Sign Up")],
        [sg.Button("Login", sg.Button("Sign Up"))]
    ]

    window = sg.Window("Login or Sign Up", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Login":
            login()
        
        if event == "Sign Up":
            signup()

        if event == None:
            break

def login():
    pass


def signup():
    pass


if __name__=="__main__":
    signup_login() 