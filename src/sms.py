from tkinter import *
import time
import ttkthemes
from tkinter import ttk
from tkinter import messagebox, filedialog
import pandas
import pymysql 


#Funcationality part

def exit_button():
    confirm=messagebox.askyesno("Confirm", "Are you sure you want to exit?", parent=root)
    if confirm:
        root.destroy()
    else:
        return

def export_data():
    url= filedialog.asksaveasfilename(defaultextension='.csv')
    indexing= studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)
    else:
        pass
    
    tab=pandas.DataFrame(newlist, columns=['ID','Name','Mobile','Email','Address', 'Gender','DOB', 'Added Date', 'Added time'])
    print(tab)
    tab.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data exported successfully',parent=root)
           
def toplevel_data(title, button_text, command):
    global idEntry,nameEntry,mobileEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen   
    screen=Toplevel()
    screen.title(title)
    screen.resizable(False, False)
    idLabel=Label(screen, font=("times new roman", 15, "bold"), text=" ID")
    idLabel.grid(row=0,column=0,padx=10,pady=10,sticky='w')
    idEntry=Entry(screen, font=("times new roman", 15, "bold"), bd=5, width=20)
    idEntry.grid(row=0,column=1,padx=10,pady=10)

    nameLabel=Label(screen, font=("times new roman", 15, "bold"), text="Name")
    nameLabel.grid(row=1,column=0,padx=10,pady=10,sticky='w')
    nameEntry=Entry(screen, font=("times new roman", 15, "bold"), bd=5, width=20)
    nameEntry.grid(row=1,column=1,padx=10,pady=10)

    mobileLabel=Label(screen, font=("times new roman", 15, "bold"), text="Mobile")
    mobileLabel.grid(row=2,column=0,padx=10,pady=10,sticky='w')
    mobileEntry=Entry(screen, font=("times new roman", 15, "bold"), bd=5, width=20)
    mobileEntry.grid(row=2,column=1,padx=10,pady=10)

    emailLabel=Label(screen, font=("times new roman", 15, "bold"), text="Email")
    emailLabel.grid(row=3,column=0,padx=10,pady=10,sticky='w')
    emailEntry=Entry(screen, font=("times new roman", 15, "bold"), bd=5, width=20)
    emailEntry.grid(row=3,column=1,padx=10,pady=10)

    addressLabel=Label(screen, font=("times new roman", 15, "bold"), text="Address")
    addressLabel.grid(row=4,column=0,padx=10,pady=10,sticky='w')
    addressEntry=Entry(screen, font=("times new roman", 15, "bold"), bd=5, width=20)
    addressEntry.grid(row=4,column=1,padx=10,pady=10)

    genderLabel=Label(screen, font=("times new roman", 15, "bold"), text="Gender")
    genderLabel.grid(row=5,column=0,padx=10,pady=10,sticky='w')
    genderEntry=Entry(screen, font=("times new roman", 15, "bold"), bd=5, width=20)
    genderEntry.grid(row=5,column=1,padx=10,pady=10)

    dobLabel=Label(screen, font=("times new roman", 15, "bold"), text="D.O.B")
    dobLabel.grid(row=6,column=0,padx=10,pady=10,sticky='w')
    dobEntry=Entry(screen, font=("times new roman", 15, "bold"), bd=5, width=20)
    dobEntry.grid(row=6,column=1,padx=10,pady=10)

    updateButton=ttk.Button(screen, text=button_text, command=command)
    updateButton.grid(row=7,columnspan=2,pady=10)

    if title=='Update Student':
        indexing=studentTable.focus()  # Get the selected row
        content=studentTable.item(indexing)
        listdata=content['values']  # Get the values of the selected student
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0,listdata[1])
        mobileEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
        genderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])
    else:
        pass

    screen.grab_set()

#Update student function
def update_data():
    query='update student set Name=%s,Mobile=%s,Email=%s, Address=%s,Gender=%s,dob=%s, date=%s,time=%s where ID=%s'
    mycursor.execute(query, (nameEntry.get(),mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get(), time.strftime("%d/%m/%Y"), time.strftime("%I:%M:%S"), idEntry.get()))
    con.commit()
    messagebox.showinfo('Success', 'Data updated successfully', parent=screen)


    query= 'select* from student'
    mycursor.execute(query)
    fethced_date = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fethced_date:
        datalist=list(data)
        studentTable.insert('',END, values=datalist)
        screen.destroy()
    else:   
        return
    

#show student fuction
def showstudent_data():
    query= 'select* from student'
    mycursor.execute(query)
    fethced_date = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fethced_date:
        datalist=list(data)
        studentTable.insert('',END, values=datalist)

#Delete button Function
def delete_student():
    indexing= studentTable.focus()  # Get the selected row
    content= studentTable.item(indexing)
    content_id = content['values'][0]  # Get the ID of the selected student
    confirm=messagebox.askyesno('Confirm', f'Are you sure you want to delete the student with ID:{content_id}?')
    if confirm is False:
        return

    query='delete from student where Id=%s'
    mycursor.execute(query,(content_id))
    con.commit()
    messagebox.showinfo('Success', f'The ID:{content_id} has been deleted successfully')
    query= 'select *from student'
    mycursor.execute(query)
    fetched_data= mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        datalist=list(data)
        studentTable.insert('',END, values=datalist)

#clock function
def clock():
    global date, time
    date= time.strftime("%d/%m/%Y")
    time1 = time.strftime("%I:%M:%S")  # 12-hour format with AM/PM
    datetimeLabel.config(text=f'   Date:{date}\nTime:{time1}')
    datetimeLabel.after(1000,clock)  # Update every second

#Heading slider function
count=0
text = ""
def slider():
    global text,count
    if count ==len(s):
        count = 0
        text = ''
    text = text+s[count]
    sliderLabel.config(text=text)
    count +=1
    sliderLabel.after(300,slider)  # Update every 300 milliseconds

#search student function

def search_data():
    query= 'select * from student where Id=%s or Name=%s or Mobile=%s or Email=%s or Address=%s or Gender=%s or DOB=%s'
    mycursor.execute(query, (idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get()))
        
    studentTable.delete(*studentTable.get_children())
    fetched_data= mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)
    if not fetched_data:
        messagebox.showinfo("info", "No data found for the given ID", parent=screen)
    else:
        pass
            
    screen.grab_set()

#add_student function

def add_data():
    try:
        if idEntry.get() == "" or nameEntry.get() == "" or mobileEntry.get() == "" or emailEntry.get() == "" or addressEntry.get() == "" or genderEntry.get() == "" or dobEntry.get() == "":
            messagebox.showerror("Error", "All fields are required!",parent=screen)
        
        else:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get(), time.strftime("%d/%m/%Y"), time.strftime("%I:%M:%S")))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
        if result:
            idEntry.delete(0, END)
            nameEntry.delete(0, END)
            mobileEntry.delete(0,END)
            emailEntry.delete(0,END)
            addressEntry.delete(0,END)
            genderEntry.delete(0,END)
            dobEntry.delete(0,END)
        else:
            screen.destroy()
            return
    except:
        messagebox.showerror('Error', 'Id has been already used', parent=screen)
        return

    query= 'select *from student'
    mycursor.execute(query)
    fetched_data= mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data: 
            datalist=list(data)
            studentTable.insert('',END, values=datalist)
    else:
        pass

    screen.grab_set()

#Database connection function
def connect_database():
    def connect_mysql():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user= userEntry.get(),password= passwordEntry.get())
            mycursor=con.cursor()
            messagebox.showinfo("Success", "Connected to the database successfully!",parent=connectwindow)
        except:
            messagebox.showerror("Error", "Failed to connect to the database. Please check your credentials.",parent=connectwindow)
            return
        destory =connectwindow.destroy
        destory()
        try:
            query="Create database Student_managment_system"
            mycursor.execute(query)
            query="use Student_managment_system"
            mycursor.execute(query)
            query="create table Student(Id int not null primary key, Name varchar(30), Mobile varchar(10),Email varchar(30), Address varchar(100),Gender varchar(20), DOB varchar(20), Date varchar(50),Time varchar(50))"
            mycursor.execute(query)
        except:
            query="use Student_managment_system"
            mycursor.execute(query)
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportdataButton.config(state=NORMAL)

    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry("470x280+730+230")
    connectwindow.title("Connect Database")
    connectwindow.resizable(False, False)

    hostnameLabel=Label(connectwindow, text="Host Name", font=("times new roman", 15, "bold"))
    hostnameLabel.grid(row=5,column=0, padx=10,pady=10)

    hostEntry=Entry(connectwindow, font=("times new roman", 15, "bold"), bd=5)
    hostEntry.grid(row=5,column=1, padx=40,pady=20)

    usernameLabel=Label(connectwindow, text="User Name", font=("times new roman", 15, "bold"))
    usernameLabel.grid(row=10,column=0, padx=10,pady=10)
    
    userEntry=Entry(connectwindow, font=("times new roman", 15, "bold"), bd=5)
    userEntry.grid(row=10,column=1, padx=40,pady=20)

    passwordLabel=Label(connectwindow, text="Password", font=("times new roman", 15, "bold"))
    passwordLabel.grid(row=15,column=0, padx=10,pady=10)

    passwordEntry=Entry(connectwindow, font=("times new roman", 15, "bold"), bd=5)
    passwordEntry.grid(row=15,column=1, padx=40,pady=20)
    passwordEntry.config(show='*')  # Hide password input

    connectButton = ttk.Button(connectwindow, text="Connect", command=connect_mysql)
    connectButton.grid(row=20,column=1,padx=40,)

    
#GUI part
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme("radiance")

root.geometry("1174x680+0+0")
root.title("Student Management System")
root.resizable(False, False)

#Creating Date and time
datetimeLabel=Label(root, font=("times new roman", 15, "bold"))
datetimeLabel.place(x=5,y=5)
clock()

#Creating slider heading
s= "Welcome to Student Management System"
sliderLabel= Label(root, font=("Times new roman", 20, "italic bold"), fg="black", width =30)
sliderLabel.place(x=380,y=20)
slider()

#Creating connect button
connectbutton=ttk.Button(root,text="Connect Database",command= connect_database)
connectbutton.place(x=1000,y=20)

#Creating Left Frame

leftFrame= Frame(root)
leftFrame.place(x=30,y=80,width=350,height=600)

#inster logo

logo_Image= PhotoImage(file="student.png")
logo_Label= Label( leftFrame, image=logo_Image)
logo_Label.grid(row=0, column=0)

#Add student button

addstudentButton= ttk.Button(leftFrame, text="Add Student", width =25,state=DISABLED, command=lambda:toplevel_data("Add Student", "Add", add_data))
addstudentButton.grid(row=1, column=0, pady=20) 


#search student
searchstudentButton= ttk.Button(leftFrame, text="Search Student", width =25,state=DISABLED, command= lambda :toplevel_data("Search Student", "Search", search_data))
searchstudentButton.grid(row=2, column=0, pady=20) 

#delete student
deletestudentButton= ttk.Button(leftFrame, text="Delete Student", width =25,state=DISABLED, command= delete_student)
deletestudentButton.grid(row=3, column=0, pady=20)

#Update Student
updatestudentButton= ttk.Button(leftFrame, text="Update Student", width =25,state=DISABLED, command=lambda :toplevel_data("Update Student", "Update", update_data))
updatestudentButton.grid(row=4, column=0, pady=20)

#show student
showstudentButton= ttk.Button(leftFrame, text="Show Student", width =25,state=DISABLED, command= showstudent_data)
showstudentButton.grid(row=5, column=0, pady=20)

#Export data
exportdataButton= ttk.Button(leftFrame, text="Export Data", width =25,state=DISABLED, command= export_data)
exportdataButton.grid(row=6, column=0, pady=20)

#Exit Button
exitButton= ttk.Button(leftFrame, text="Exit", width =25, command=exit_button)
exitButton.grid(row=7, column=0, pady=20)


#Creating Right Frame

rightFrame= Frame(root, bg ="light blue")
rightFrame.place(x=325,y=80,width=820,height=600)

#Creating scrollbar
scrollbarX= Scrollbar(rightFrame, orient=HORIZONTAL)
scrollbarX.pack(side=BOTTOM, fill=X)
scrollbarY= Scrollbar(rightFrame, orient=VERTICAL)
scrollbarY.pack(side=RIGHT, fill=Y)

#Creating treeview in the right frame
studentTable = ttk.Treeview(rightFrame, columns=("ID", "Name", "Mobile No","Email", "Address","Gender","D.O.B", "Added Date", "Added Time"), xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)

studentTable.pack(fill=BOTH, expand=1)


scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)

#Adding heading
studentTable.heading("ID", text='ID')
studentTable.heading("Name", text='Name')
studentTable.heading("Mobile No", text='Mobile No')
studentTable.heading("Email", text='Email')
studentTable.heading("Address", text='Address')
studentTable.heading("Gender", text='Gender')
studentTable.heading("D.O.B", text='D.O.B')
studentTable.heading("Added Date", text='Added Date')
studentTable.heading("Added Time", text='Added Time')

studentTable.config(show='headings')

#Setting column width
studentTable.column("ID", width=50, anchor=CENTER)
studentTable.column("Name", width=150, anchor=CENTER)
studentTable.column("Mobile No", width=150, anchor=CENTER)
studentTable.column("Email", width=250, anchor=CENTER)
studentTable.column("Address", width=300, anchor=CENTER)
studentTable.column("Gender", width=150, anchor=CENTER)
studentTable.column("D.O.B", width=150, anchor= CENTER)
studentTable.column("Added Date", width=150, anchor=CENTER)
studentTable.column("Added Time", width=150, anchor=CENTER)

#Configuring style for the treeview
style=ttk.Style()
style.configure('Treeview', rowheight=40, font=('Arial',12, 'bold'), foreground='black', background='light blue')
style.configure('Treeview.Heading', font=('Arial', 12, 'bold', 'underline'))


root.mainloop()
