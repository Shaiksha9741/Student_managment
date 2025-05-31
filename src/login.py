from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk as ImageTK
from getpass import getpass, getpass as getpass

 
    



def login():
    global  usernameEntry, passwordEntry
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("Error", "Fileds cannot be empty")
    elif usernameEntry.get()=="Shaiksha" and passwordEntry.get() == "Shaiksha@123":
        messagebox.showinfo("Success", "Login Successful")
        window.destroy()
        import sms
    else:
        messagebox.showerror("Error", "Invalid Username or Password")






window = Tk()
window.geometry("1080x700+0+0")
window.resizable(False, False)
window.title("Login Page of Student Management System")

#Background image
backgroundImage=ImageTK.PhotoImage(file= "bg1.jpg")
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0,y=0)

#Lagin frame
loginFrame = Frame(window,bg = "white")
loginFrame.place(x=325,y=250)

#Lago image
logoImage=PhotoImage(file="logo1.png")
logoLabel = Label(loginFrame, image=logoImage, bg = "white")
logoLabel.grid(row=0, column=0 ,columnspan=2, pady = 10)
usernameImage = PhotoImage(file = "user.png")
passwordImage = PhotoImage(file = "passlock.png")

#Username
usernameLabel = Label(loginFrame, image= usernameImage,text="Username", compound=LEFT, font=("Times new roman", 20, "bold"), bg="white", fg="black")
usernameLabel.grid(row=1,column=0, pady = 10,padx=20)

#Username Entry
usernameEntry=Entry(loginFrame, font=("Times new roman", 15,"bold"), bd = 5, fg = "royal blue")
usernameEntry.grid(row=1,column=1, pady = 10, padx=20)

#Password
passwordLabel = Label(loginFrame, image= passwordImage,text="Password", compound=LEFT, font=("Times new roman", 20, "bold"), bg="white", fg="black")
passwordLabel.grid(row=2,column=0, pady = 10,padx=20)

#Password Entry
passwordEntry=Entry(loginFrame, font=("Times new roman", 15,"bold"), bd = 5, fg = "royal blue")
passwordEntry.grid(row=2,column=1, pady = 10, padx=20)
passwordEntry.config(show='*')  # Hide password input

#Login Button
loginbutton = Button(loginFrame, text = "Login", font=("Times new roman", 14, "bold"), bg = "royal blue", fg = "White",width= 15, activebackground = "royal blue", activeforeground="white", cursor = "hand2", command = login)
loginbutton.grid(row=3, column = 0, pady = 15, columnspan= 2)





window.mainloop()

