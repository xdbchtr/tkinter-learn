import customtkinter as ctk
from tkinter import messagebox
import requests

# Initialize the window
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

        # Replace 'http://your-api-url.com/login' with your actual API URL
    url = 'http://82.112.230.35:8082/login'
    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Login Successful!")
            root.withdraw()
            open_dashboard()
        else:
            messagebox.showerror("Error", "Login Failed. Please check your credentials.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to connect to the API: {e}")

def open_dashboard():
    dashboard = ctk.CTkToplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("400x400")

    welcome_label = ctk.CTkLabel(dashboard, text="Welcome to the Dashboard!")
    welcome_label.pack(pady=50)

    # Add a logout button to close the dashboard and show the login window again
    logout_button = ctk.CTkButton(dashboard, text="Logout", command=lambda: logout(dashboard))
    logout_button.pack(pady=20)

# Function to handle logout
def logout(dashboard):
    dashboard.destroy()  # Close the dashboard window
    root.deiconify()  # Show the login window again

# Create labels and entry fields
label_username = ctk.CTkLabel(root, text="Username:")
label_username.pack(pady=10)

entry_username = ctk.CTkEntry(root, width=200)
entry_username.pack(pady=10)

label_password = ctk.CTkLabel(root, text="Password:")
label_password.pack(pady=10)

entry_password = ctk.CTkEntry(root, width=200, show="*")  # Mask the password input
entry_password.pack(pady=10)

# Create login button
login_button = ctk.CTkButton(root, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
