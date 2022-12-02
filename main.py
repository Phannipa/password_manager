from tkinter import*  # It means import all of the classes
from tkinter import messagebox # messagebox is a module not a classs
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10) # 8, 9, 10, number of letters
    nr_symbols = random.randint(2, 4) # number of symbols
    nr_numbers = random.randint(2, 4) # number of numbers

    # password_list = []

    # We use list comprehension---> new_list = [new_item for item in list]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_letter = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)] # We use list comprehension

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)] # We use list comprehension

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list) # Reorder list

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list) # Using join when it is a string.

    #print(f"Your password is: {password}")
    password_entry.insert(0, password) # To pop up the password on password entry after we generate it.

    # When we want to copy and paste that password to another place. This method help you to copy on clipboard and we do just only paste it.
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
# After we click add button, all of texts entry will save on data.txt and after that all of texts entry will delete from the particular entry.

def save():

    website = website_entry.get() # Get is the method to get the current entry text.
    email = email_entry.get()
    password = password_entry.get()

    # Create the message box and get the user to check the details that they have entered before write it on data.txt file.

    if len(website) == 0 or len(password) == 0: # In case that the users leave empty text.
        messagebox.showinfo(title="Oops", message="Please make sure you haven't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                               f"\nPassword: {password} \nIs it ok to save")

        if is_ok: # is_ok is True, write it on file
            with open("data.txt", "a") as data_file: # Or writing as : data_file  = open("data.txt", "a"). And "a" means append.
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END) # After write it on data.txt file, delete text entry from beginning character to the last character from the particular entry
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx =50, pady=50) # Add the padding

# sticky="EW" is the method to get perfect alignment without the need for pixel adjustment trial and error.
# Only one single absolute value for width is needed for the longest widget, (ie the Add button)
# and the other widgets will snap neatly in their positions. So for Entry don't have to add any width.
# So from searching Google on the "sticky" parameter, the EW part is the compass directions (E)ast and (W)est
# and the sticky basically "sticks" the widget to the edges of the column.
# So this instruction spans the widget to fill the whole width of the grid column/s.
# This means we don't need to experiment with absolute pixel values for the widgets except for the longest one (add)
# , which determines the size of the last column.

# Add image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) # Need our image to be the middle of canvas, we use half of size of width and height of image.
canvas.grid(column=1, row=0) # To specific the position of image and pack the canvas on to the screen. If we don't pack it, it won't shpw on screen. If we have more components, we use grid.


# Create website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry() # We don't have to add any width, we add only width of the longest widget
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus() # To create a cursor in entry.


# Create email/username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry() # We don't have to add any width, we add only width of the longest widget
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "maiphannipa2528@gmail.com") # Pop up automatic email that we always use in entry. Insert this piece of text at the first zero character. To replace the current text.
# Create Password
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_entry = Entry() # We don't have to add any width, we add only width of the longest widget
password_entry.grid(column=1, row=3, sticky="EW")

# Create generate password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

# Create add button

add_button = Button(text="Add", width=36, command=save) # We don't have to add any width, we add only width of the longest widget
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")








window.mainloop()