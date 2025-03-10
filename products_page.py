import customtkinter as ctk
import requests
from api_handler import get_products_from_api

def open_products_page(dashboard):
    products_window = ctk.CTkToplevel(dashboard)
    products_window.title("Products List")
    products_window.geometry("800x600")

    products = get_products_from_api()

    if products:
        products_label = ctk.CTkLabel(products_window, text="Products List", font=("Arial", 16))
        products_label.pack(pady=10)

        # Loop over the products and display them
        print(products)
        for product in products:
            product_name = product.get('name', 'No Name')
            product_label = ctk.CTkLabel(products_window, text=f"Name: {product_name}")
            product_label.pack(pady=5)
    else:
        # Show an error message if no products are found
        error_label = ctk.CTkLabel(products_window, text="Failed to load products.")
        error_label.pack(pady=10)