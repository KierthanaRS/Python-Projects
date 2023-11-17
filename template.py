import PySimpleGUI as sg
import pandas as pd
import mysql.connector as mc
def welcome():
    sg.theme("Tan")
    col1=   [[sg.Image("1.png")],
             [sg.Button('Ok')]]
    layout=[[sg.Column(col1)]]
    window=sg.Window("WELCOME",layout).finalize()
    event=window.read()
    window.close()
    return(event)
# welcome()
def frspng():
    sg.theme("Tan")
    col1 = [[sg.Button(enable_events=True,image_filename="2.png",key='b1'),
             sg.Button(enable_events=True,image_filename="3.png",key='b2'),
             sg.Button(enable_events=True,image_filename="4.png",key='b3'),
             sg.Button(enable_events=True,image_filename="5.png",key='b4'),
             sg.Button(enable_events=True,image_filename="6.png",key='b5'),
             ],[sg.Button("Exit")]]
    # col2=[[sg.Text("ADD Contact",font=("Arial 14"),background_color="white",text_color="black"),
    #        sg.Text("View Contact",font=("Arial 14"),background_color="white",text_color="black"),
    #        sg.Text("Search Contact",font=("Arial 14"),background_color="white",text_color="black"),
    #        sg.Text("Update Contact",font=("Arial 14"),background_color="white",text_color="black"),
    #        sg.Text("Delete Contact",font=("Arial 14"),background_color="white",text_color="black")]]
    layout = [[sg.Column(col1,element_justification='c')]]
    window = sg.Window('Welcome',layout).finalize()
    events,values = window.read()
    window.close()
    return (events ,values)
# frspng()
def AddContact():
    sg.theme("Tan")
    col1=[[sg.Text("Contact Details",font=("Arial 14"),background_color="white",text_color="black")],
             [sg.Input("First Name")],
             [sg.Input("Sur Name")],
             [sg.Input("Phone Nuber")],
             [sg.Button("Add"),sg.Button("Back")]]
    layout=[[sg.Column(col1)]]
    window=sg.Window("Admin Login",layout).finalize()
    event,values=window.read()

    print(event, values[0],values[1]) 
    window.close()
    return(event,values)

def ViewContact():
    sg.theme("Tan")
    col1=   [[sg.Text("SIGN UP",font=("Arial 14"),background_color="white",text_color="black")],
             [sg.Input("user ID")],
             [sg.Input("User Name")],
             [sg.Input("Password")],
             [sg.Input("Identification No.(Max 3 numbers)")],
             [sg.Button("Sign Up"),sg.Button('Cancel')]]
   
    layout=[[sg.Column(col1)]]
    window=sg.Window("View Contact",layout).finalize()
    event,values=window.read()
    print(event, values[0]) 
    window.close()
    return(event,values)

def searchContact():
    sg.theme("Tan")
    col1=[[sg.Text("Search Phone number",font=("Arial 14"))],
          [sg.Combo(["Name","Phone Number"], size=(20, 20), default_value='-Select-')],
          [sg.Input("")],
          [sg.Button("Search"),sg.Button("Back")]]
    layout=[[sg.Column(col1)]]
    window=sg.Window("Search Details",layout).finalize()
    event,value=window.read()
    print(event) 
    window.close()
    return(event,value)
def UpdateContact_info():
    sg.theme("Tan")
    col1= [[sg.Text("Select the data to be Updated",font=("Arial 14"),background_color="white",text_color="black")],
            [sg.Combo(["Name","Phone Number"], size=(20, 20), default_value='-Select-')],
           [sg.Button("Next"),sg.Button("Back")]]
   
    layout=[[sg.Column(col1)]]
    window=sg.Window("Update Contact",layout).finalize()
    event,values=window.read()
    print(event, values[0]) 
    window.close()
    return(event,values)

def update_name():
     sg.theme("Tan")
     col1=[[sg.Text("Enter the phone_number")],
           [sg.Input("")],
           [sg.Text("Enter the new name")],
           [sg.Input("")],
          [sg.Button("Update"),sg.Button("Back")]]

     layout=[[sg.Column(col1)]]
     window=sg.Window("Update name",layout).finalize()
     event,values=window.read()
     print(event) 
     window.close()
     return(event,values)

def update_number():
     sg.theme("Tan")
     col1=[[sg.Text("Enter the name")],
           [sg.Input("")],
           [sg.Text("Enter the new phone number")],
           [sg.Input("")],
          [sg.Button("Update"),sg.Button("Back")]]

     layout=[[sg.Column(col1)]]
     window=sg.Window("Update phone number",layout).finalize()
     event,values=window.read()
     print(event) 
     window.close()
     return(event,values)

def delete():
    sg.theme("Tan")
    col1=[[sg.Input("Name")],
          [sg.Button("Delete"),sg.Button("Back")]]
    layout=[[sg.Column(col1)]]
    window=sg.Window("Delete Details",layout).finalize()
    event,values=window.read()
    print(event,values[0]) 
    window.close()
    return(event,values)

def exit():
    sg.theme("Tan")
    layout=[[sg.Text("Are you sure want to exit the app?")],
            [sg.Button("Yes"),sg.Button("No")]]
    window=sg.Window("Patients",layout).finalize()
    event,value=window.read()
    window.close()
    return(event,value)

