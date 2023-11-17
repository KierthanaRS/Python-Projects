import template as tl
import pandas as pd
import PySimpleGUI as sg;
import matplotlib.pyplot as plt
import mysql.connector as mc

event=tl.welcome()

mydb=mc.connect(host="127.0.0.1",
                database= "contactmingle",
                user="root",
                password="");
def contact_page():       
    event,userInput=tl.frspng()
    if event=="b1":
        
            cursor=mydb.cursor()
            event1,userInput1=tl.AddContact()
            if event1 == 'Add':
                        cursor.execute("INSERT INTO contactInfo(first_name,sur_name,phone_number) VALUES (%s,%s,%s)",(userInput1[0], userInput1[1],userInput1[2]))
                        mydb.commit()
                        sg.popup('Succesfully Added')
                        contact_page()
            elif event1 == 'Back':
                contact_page()
    elif event=="b2":
            cursor=mydb.cursor()
            cursor.execute("SELECT first_name,sur_name,phone_number FROM contactInfo ORDER BY first_name,sur_name ASC")
            record = cursor.fetchall()
            if cursor.rowcount !=0:
                    df=pd.DataFrame(record,columns=list(cursor.column_names))
                    heading=list(df.columns)
                    data=df.values.tolist()
                    layout = [[sg.Table(values=data,
                    headings=heading,
                    max_col_width=25,
                    auto_size_columns=True,
                    justification='right',
                    alternating_row_color='lightblue',
                    num_rows=min(len(data), 20))],[sg.Button("Back")]]
                    window = sg.Window('Appointment Table', layout, grab_anywhere=False)
                    event= window.read()
                    if event=="Back":
                        contact_page()
                    window.close()
                    contact_page()
            else:
                    sg.popup("NO DATA FOUND")
                    contact_page()
    elif event=="b3":
            cursor=mydb.cursor()
            event1,userInput1=tl.searchContact()
            if event1 == 'Search':
                if userInput1[0]=='Name':
                    cursor.execute("SELECT first_name,sur_name,phone_number FROM contactInfo WHERE first_name LIKE %s OR sur_name LIKE %s", ('%' + userInput1[1] + '%', '%' + userInput1[1] + '%'))
                    record = cursor.fetchall()
                    if cursor.rowcount !=0:
                        df=pd.DataFrame(record,columns=list(cursor.column_names))
                        heading=list(df.columns)
                        data=df.values.tolist()
                        layout = [[sg.Table(values=data,
                        headings=heading,
                        max_col_width=25,
                        auto_size_columns=True,
                        justification='right',
                        alternating_row_color='lightblue',
                        num_rows=min(len(data), 20))],[sg.Button("Back")]]
                        window = sg.Window('Appointment Table', layout, grab_anywhere=False)
                        event= window.read()
                        if event=="Back":
                            contact_page()
                        window.close()
                        contact_page()
                    else:
                        sg.popup("NO DATA FOUND")
                        contact_page()
                if userInput1[0]=='Phone Number':
                    cursor.execute("SELECT first_name, sur_name, phone_number FROM contactInfo WHERE CONCAT(phone_number, '') LIKE %s", ('%' + userInput1[1] + '%',))
                    record = cursor.fetchall()
                    if cursor.rowcount !=0:
                        df=pd.DataFrame(record,columns=list(cursor.column_names))
                        heading=list(df.columns)
                        data=df.values.tolist()
                        layout = [[sg.Table(values=data,
                        headings=heading,
                        max_col_width=25,
                        auto_size_columns=True,
                        justification='right',
                        alternating_row_color='lightblue',
                        num_rows=min(len(data), 20))],[sg.Button("Back")]]
                        window = sg.Window('Appointment Table', layout, grab_anywhere=False)
                        event= window.read()
                        if event=="Back":
                            contact_page()
                        window.close()
                        contact_page()
                    else:
                        sg.popup("NO DATA FOUND")
                        contact_page()
            elif event1 == 'Back':
                    contact_page()
    elif event=="b4":
            cursor=mydb.cursor()
            event,userInput=tl.UpdateContact_info()
            if event == 'Next':
                if userInput[0]=='Name':
                    event1,userInput1=tl.update_name()
                    if event1=='Update':
                        cursor.execute("UPDATE contactInfo SET first_name=%s WHERE phone_number=%s",(userInput1[1],userInput1[0]))
                        mydb.commit()
                        sg.popup("UPDATED")
                        contact_page()
                    elif event1=='Back':
                        contact_page()
                if userInput[0]=='Phone Number':
                    event1,userInput1=tl.update_number()
                    if event1=='Update':
                        cursor.execute("UPDATE contactInfo SET phone_number=%s WHERE first_name=%s",(userInput1[1],userInput1[0]))
                        mydb.commit()
                        sg.popup("UPDATED")
                        contact_page()
                    elif event1=='Back':
                        contact_page()
            elif event == 'Back':
                    contact_page()
    elif event=="b5":
            cursor=mydb.cursor()
            event1,userInput1=tl.delete()
            if event1 == 'Delete':
                cursor.execute("DELETE FROM contactInfo WHERE first_name = %s", (userInput1[0],))
                mydb.commit()
                sg.popup("DELETED")
                contact_page()
            elif event1 == 'Back':
                    contact_page()
    if event == sg.WINDOW_CLOSED or event == "Exit":
            event1,value1 = tl.exit()
            if event1 == "Yes":
                sg.popup("Thank you for using our app")
            elif event1 == "No":
                contact_page()


contact_page()