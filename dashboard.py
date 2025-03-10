import customtkinter as ctk
import tkinter as tk
from PIL import Image
from products_page import open_products_page

# Function to open a new dashboard window after successful login
def open_dashboard(root):
    dashboard = ctk.CTkToplevel(root)  # Create a new window
    dashboard.title("Dashboard")
    dashboard.geometry("800x600")

    # Create a menubar
    menubar = tk.Menu(dashboard)

    # Create File menu and add options
    file_menu = tk.Menu(menubar, tearoff=0)
    # file_menu.add_separator()
    file_menu.add_command(label="Logout", command=lambda: logout(dashboard, root))
    menubar.add_cascade(label="File", menu=file_menu)

    # Add the menubar to the window
    dashboard.config(menu=menubar)

    # Welcome label in the dashboard
    welcome_label = ctk.CTkLabel(dashboard, text="WELCOME!", font=("Helvetica", 50))
    welcome_label.pack(pady=50)

    # Load icons using Pillow
    product_icon = ctk.CTkImage(Image.open("icons/dress.png"), size=(20, 20))
    category_icon = ctk.CTkImage(Image.open("icons/app.png"), size=(20, 20))
    collection_icon = ctk.CTkImage(Image.open("icons/collection.png"), size=(20, 20))

    # Create buttons for Products, Categories, and Collections with icons
    products_button = ctk.CTkButton(dashboard, fg_color="white", text_color="black", text="Products", font=("Arial", 16), image=product_icon, compound="right", command=lambda: open_products_page(dashboard), width=200, height=50, corner_radius=50)
    products_button.pack(pady=10)

    categories_button = ctk.CTkButton(dashboard, text="Categories", font=("Arial", 16), image=category_icon, compound="right", command=show_categories, width=200, height=50, corner_radius=50)
    categories_button.pack(pady=10)

    collections_button = ctk.CTkButton(dashboard, fg_color="yellow", text_color="black", text="Collections", font=("Arial", 16), image=collection_icon, compound="right", command=show_collections, width=200, height=50, corner_radius=50)
    collections_button.pack(pady=10)


# Function to handle logout
def logout(dashboard, root):
    dashboard.destroy()  # Close the dashboard window
    root.deiconify()  # Show the login window again

def show_products():
    print("Showing products page")

def show_categories():
    print("Showing categories page")

def show_collections():
    print("Showing collections page")
