import tkinter as tk
from tkinter.constants import X
from tkinter.font import Font 
from functools import partial
from tkinter import messagebox










def show(frame):
    frame.tkraise()


def call():
    e = entry.get()

    if e == '1':
        show(idvalid)
    if e == '2':
        show(mailvalid)
    if e == '3':
        show(passvalid)
    if e == '4':
        show(numbervalid)
    if e == '5':
        show(stringvalid)
    if e == '6':
        value = messagebox.askquestion('exit','Do You Really Want to Terminate The Program ?')
        if(value == 'yes'):
            exit()
        if(value == 'no'):
            messagebox.showinfo('Validation', 'Continue Validation Work')

    





def idvalidation():
    x = entry1.get()

    a = len(x)

    if a == 9 :
        if (x[0] == '0') and (x[1] == '1') and (x[2] == '1'):

            if (x[3] >='0' and x[3] <= '2') and (x[4] >='0' and x[3] <= '9'):

                if ( x[5] >= '1' and x[5] <= '3'):

                    if (x[6] >= '0' and x[6] <= '9') and (x[7] >= '0' and x[7] <= '9') and (x[8] >= '0' and x[8] <= '9'):

                        messagebox.showinfo('Validation', 'Congratulations !!!! Validation Successfull')

                    else:
                        messagebox.showerror('Error Message','Error: Roll can not excede 001-999')
                        
                else:
                    messagebox.showerror('Error Message','Error: Fifth Index Error 6th digit error')
                    

            else:
                messagebox.showerror('Error Message','Error: Third and Fourth Index Error')
        
        else:
            messagebox.showerror('Error Message','Error: First Three Index Error')


    else:
        messagebox.showerror('Error Message','Error: ID must be 9 digits number ')







def emailvalidation():
    x = entry2.get()


    j=0
    k=0
    m=0 #how many digits
    n=0
    p= len(x)
    str1 ='bscse'
    str2='bseee'
    str3='.uiu.ac.bd'
    a=0
    b=0
    c=0



    for index,value in enumerate(x):
        if ( value.isalpha() == True) :
            j = j + 1
        if ( value.isdigit() == True):
            k = index
            break
        if (value.isalpha() == False and value.isdigit() == False):
            messagebox.showerror('Error Message','Error: First characters can not be special characters')
            break

    if (j == k and j >= 5):
        
        for v in range(j,p):
            if ( x[v].isdigit() == True):
                m = m + 1

            if (x[v].isalpha() == True):
                n= index
                break


        if(m == 6):
            if(x[m+j] == '@'):
                for v in range(m+j+1,p):
                    if(x[v]=='.'):
                        break
                    if(x[v] == str1[a]):
                        a=a+1
                    if(x[v] == str2[b]):
                        b=b+1

            

                if ( a == len(str1)) or ( b == len(str2) ):

                    for z in range(v,p):
                        if(x[z] == str3[c]):
                            c=c+1
                    if( c == len(str3)):
                        messagebox.showinfo('Validation', 'Congratulations !!!! Email Validation Successfull')

                        

                    else:
                        messagebox.showerror('Error Message','Error: .uiu.ac.bd part not okay')
                       



                else:
                    messagebox.showerror('Error Message','Error: bscse or bseee is not included correctly')
                    

                

    



def passvalidation():
    x= entry3.get()

    a = len(x)
    u=0
    l=0
    d=0
    s=0

    if (a >= 8) and ( x[a-1]== 'P'):
        for i in x:
            if(i.isupper()==True):
                u=u+1
            if(i.islower()==True):
                l=l+1
            if(i.isdigit()==True):
                d=d+1

            if( i == '@' ) or ( i == '%' ) or ( i == '#' ) or ( i == '&' ):
                s=s+1

        if ( u > 0 ) and ( l > 0 ) and ( d > 0 ) and ( s > 0 ):
            messagebox.showinfo('Validation', 'Congratulations !!!! Password Validation Successfull')
        else:
            messagebox.showerror('Error Message','Error: Not valid')
    else:
        messagebox.showerror('Error Message','Error: Check Your password length or The last capital P ')




def numvalidation():
    x = entry4.get()

    a=len(x)
    dot=0
    plus=0
    minus=0
    dig =0

    if ( ( x[0] == '+') or ( x[0]== '-') or ( x[0]=='.') or (x[0].isdigit() == True) ) and (x[a-1] !='.' and x[a-1] != '+' and x[a-1] != '-'):
        if( x[1].isdigit() == True) or ( x[1]=='.') :
            for i in x:
                if(i == '.'):
                    dot =dot +1
                if(i == '+'):
                    plus = plus +1
                if(i == '-'):
                    minus = minus + 1
                if(i.isdigit() == False):
                    dig = dig + 1
        
            dig = dig - dot - plus - minus
        
            if( dot <= 1 ) and ( plus <= 1 ) and ( minus <=1 ) and (dig == 0 ):
                messagebox.showinfo('Validation', 'Congratulations !!!! Number Validation Successfull')
            else:
                messagebox.showerror('Error Message','Error: sign or decimal mistake or non digit input mistake')
        
        else:
            messagebox.showerror('Error Message','Error: second part cannot be a sign')
           
    else:
        messagebox.showerror('Error Message','Error: check last dot or first index')
        


def stringvalidation():
    x = entry5.get()
    a= len(x)
    k=0
    l=0
    m=0
    c=0
    p=0
 

    for i,j in enumerate(x):

        if(j.islower() == True):
            l=l+1 #lower part number 

        if(j == 'U' or j.isupper() == True):
            k = i #index value
            break

    if(x[k]== 'U' and x[k+1] == 'I' and x[k+2] == 'U'):
        if( x[k+3].isdigit() == True):
            m = k+3
            for b in range(m+1,a):
                if( x[b] == x[c] ):
                    p=p+1
                    c=c+1
                else:
                    messagebox.showerror('Error Message','Error: No match first and last part ')
                    break
                    
     
            if(p==l):
                messagebox.showinfo('Validation', 'Congratulations !!!! String Validation Successful')
            else:
                messagebox.showerror('Error Message','Error: last and first part must be same ')
            
            
            
                
        else:
            messagebox.showerror('Error Message','Error: Digit mistake')

    else:
        messagebox.showerror('Error Message','Error: Not Valid')




root = tk.Tk()
root.state('zoomed')
root.title('Validation')
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)










startpage = tk.Frame(root,bg='#43cea2')
idvalid = tk.Frame(root,bg='green')
mailvalid = tk.Frame(root,bg='pink')
passvalid = tk.Frame(root,bg='blue')
numbervalid = tk.Frame(root,bg='orange')
stringvalid = tk.Frame(root,bg='purple')



for frame in (startpage,idvalid,mailvalid,passvalid,numbervalid,stringvalid):
    frame.grid(row=0,column=0,sticky='nsew')




show(startpage)







#first page .........................

startpage_title = tk.Label(startpage,text="Validation \n \n\n 1. Input '1' For ID VALIDATION \n\n2. Input '2' For email VALIDATION \n\n3. Input '3' For password VALIDATION \n\n4. Input '4' For number VALIDATION \n\n5. Input '5' For string VALIDATION \n\n6. Input '6' For Exit \n \n",font=('Algerian',20),bg="red")
startpage_title.pack(fill=X)


startpage_label = tk.Label(startpage,text="Enter Your Choice:",font=('Algerian',20))
startpage_label.pack(pady=30)
entry = tk.Entry(startpage,font=('Algerian',15))
entry.pack(ipady=10,ipadx=10)


startpage_submission = tk.Button(startpage,text="Submit",font=('Algerian',15),command=call )
startpage_submission.pack(pady=20)



#idpage....................

id_label = tk.Label(idvalid,text="Enter Your ID",font=('Algerian',20))
id_label.pack(padx=50,pady=50)

entry1 = tk.Entry(idvalid,font=('Algerian',15))
entry1.pack(ipady=10,ipadx=10)



idpage_submission = tk.Button(idvalid,text="Submit",font=('Algerian',15),command= idvalidation)
idpage_submission.pack(pady=20)

back = tk.Button(idvalid,text="back",font=('Algerian',15),bg='yellow',command= lambda:show(startpage))
back.pack(pady=20,fill=X)



#emailpage............................

mail_label = tk.Label(mailvalid,text="Enter Your Email",font=('Algerian',20))
mail_label.pack(padx=50,pady=50)

entry2 = tk.Entry(mailvalid,font=('Algerian',15))
entry2.pack(ipady=10,ipadx=80)


mailpage_submission = tk.Button(mailvalid,text="Submit",font=('Algerian',15),command= emailvalidation)
mailpage_submission.pack(pady=20)


back = tk.Button(mailvalid,text="back",font=('Algerian',15),bg='yellow',command= lambda:show(startpage))
back.pack(pady=20,fill=X)



#passpage............................

pass_label = tk.Label(passvalid,text="Enter Your Password",font=('Algerian',20))
pass_label.pack(padx=50,pady=50)

entry3 = tk.Entry(passvalid,font=('Arial',15))
entry3.pack(ipady=10,ipadx=80)


passpage_submission = tk.Button(passvalid,text="Submit",font=('Algerian',15),command= passvalidation)
passpage_submission.pack(pady=20)


back = tk.Button(passvalid,text="back",font=('Algerian',15),bg='yellow',command= lambda:show(startpage))
back.pack(pady=20,fill=X)


#numberpage............................

num_label = tk.Label(numbervalid,text="Enter Your Number",font=('Algerian',20))
num_label.pack(padx=50,pady=50)

entry4 = tk.Entry(numbervalid,font=('Algerian',15))
entry4.pack(ipady=10,ipadx=80)


numpage_submission = tk.Button(numbervalid,text="Submit",font=('Algerian',15),command= numvalidation)
numpage_submission.pack(pady=20)


back = tk.Button(numbervalid,text="back",font=('Algerian',15),bg='yellow',command= lambda:show(startpage))
back.pack(pady=20,fill=X)

#stringpage............................

str_label = tk.Label(stringvalid,text="Enter The String",font=('Algerian',20))
str_label.pack(padx=50,pady=50)

entry5 = tk.Entry(stringvalid,font=('Arial',15))
entry5.pack(ipady=10,ipadx=80)


strpage_submission = tk.Button(stringvalid,text="Submit",font=('Algerian',15),command= stringvalidation)
strpage_submission.pack(pady=20)


back = tk.Button(stringvalid,text="back",font=('Algerian',15),bg='yellow',command= lambda:show(startpage))
back.pack(pady=20,fill=X)


root.mainloop()

