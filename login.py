import customtkinter as ctk
from tkinter import messagebox
from api_handler import login_api
from dashboard import open_dashboard

# Initialize the main login window
root = ctk.CTk()
root.title("Login Form")
root.geometry("400x400")

# Function to handle login logic
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Invalid Input", "Username and Password cannot be empty")
        return

    success = login_api(username, password)  # Call the login API
    if success:
        messagebox.showinfo("Success", "Login Successful!")
        root.withdraw()  # Hide the login window
        open_dashboard(root)  # Open dashboard and pass the root window
    else:
        messagebox.showerror("Error", "Login Failed. Please check your credentials.")

# Create labels and entry fields
label_username = ctk.CTkLabel(root, text="Username:")
label_username.pack(pady=10)

entry_username = ctk.CTkEntry(root, width=200)
entry_username.pack()

label_password = ctk.CTkLabel(root, text="Password:")
label_password.pack(pady=10)

entry_password = ctk.CTkEntry(root, width=200, show="*")  # Mask the password input
entry_password.pack()

# Create login button
login_button = ctk.CTkButton(root, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
