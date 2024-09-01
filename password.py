from random import *
from guizero import *
from string import *

def generate_password():
    # Get the length from the TextBox
    length = int(p_len.value)
    
    if length <= 0:
        display.value = "Length should be greater than 0; Try again"
    else:
        chars = digits + ascii_lowercase + ascii_uppercase + punctuation
        password = ''.join(choices(chars, k=length))  # Generate the password
        display.value = password  # Display the generated password

# Set up the GUI
app = App('Password Generator')
text = Text(app, text="Enter the desired length of password: ")
p_len = TextBox(app)
btn = PushButton(app, text="Generate Password", command=generate_password)
display = Text(app, text="", size=18, color='red')

app.display()
