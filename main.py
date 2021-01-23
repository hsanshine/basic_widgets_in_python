from tkinter import *

# creating a new window and configurations
window = Tk()
window.title('Widget Examples')
window.minsize(width=600, height=500)

# labels
label = Label(text='this is some old text')
label.config(text='this is some new text', fg='blue')
label.pack(side='left')


# Buttons
def action():
    print('do something')


# calls action() when pressed
button = Button(text='click me', command=action, fg='red')
button.pack()

# Entries
entry = Entry(width=30)
# add some text to begin with, the text will be there for the user to edit ,to add to or to delete
entry.insert(END, string='Some text to begin with')
# Gets text in the entry
print(entry.get())  # get whatever is in the entry box and prints it here when the line is executed..this wont be
# repeated because it is only executed once when the entry box is created and there is no way to call this line again
# by an interactivity from the window like with widgets such as the button that automatically give you this option
entry.pack()

# Text
text = Text(height=5, width=40)  # multi line text entry or input box
# puts the cursor in textbox
text.focus()
# add some text to begin with
text.insert(END, 'example of multiline text entry')
# gets the current value in textbox starting at line 1 and character zero
print(text.get('1.0', END))
text.pack()


# spin box
def spinbox_used():
    # gets the current value in the spin box
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)  # whenever you touch it it calls spin box used
spinbox.pack(side='right')


# scale
# called with current scale value if you attach it to any function, that function will recieve the scale value argument
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# check box
def checkbutton_used():
    # prints 1 if the on button is checked, otherwise zero
    print(checked_state.get())


# variable to hold on to checked state, 0 is off , 1 is on
checked_state = IntVar()  # function defined in tkinter to tell it that this only takes in integer values
check_botton = Checkbutton(text='Is On?', variable=checked_state,
                           command=checkbutton_used)  # we put in the text or the label on the check box
# we also put in the boolean variable that this check box can control
checked_state.get()  # the variable hold the value in the check button at any one point , you must provide it when
# you create a check button, this is where it store the yes or no.. and then use name.get() to read the contents of that
# var
check_botton.pack()


# radio buttons
def radio_used():
    print(radio_state.get())


# variable to hold on to which radio button value is checked
radio_state = IntVar()  # tying as many radio button to the same var makes them mutually exclusive
radiobutton1 = Radiobutton(text='option 1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='option 2', value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text='option 3', value=3, variable=radio_state, command=radio_used)
radiobutton4 = Radiobutton(text='option 4', value=4, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()


# list box
def listbox_used(event):
    # gets the current selection from the list box
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)  # means it can take upto 4 entries
fruits = ['apple', 'pear', 'orange', 'banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()

window.mainloop()
