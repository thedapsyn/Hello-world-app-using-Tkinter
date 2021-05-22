import tkinter as tk


def hello():
    """Output or display  user_input to the tkinter window."""
    
    user = input("Enter name: ")
    # the main window in Tkinter by convection is called root or you give it any variable name
    root = tk.Tk()

    root.title("HWAP | HELLO, WORLD APPS")

    # place a label on the root wind
    greeting = tk.Label(root, text=f"Hello, {user.upper()}\n You're welcome to Tkinter HWAP. ")

    # positions the Label on the main window called root
    greeting.pack()

    # keep the window displaying
    root.mainloop()
   
# call hello function 
hello()

