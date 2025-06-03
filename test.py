import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        messagebox.showinfo("Formulario enviado", f"Nombre: {name}\nEmail: {email}")
    else:
        messagebox.showwarning("Error", "Por favor, completa todos los campos.")

# Crear ventana principal
root = tk.Tk()
root.title("Formulario")

# Etiquetas y campos de entrada
tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

# Botón de envío
submit_button = tk.Button(root, text="Enviar", command=submit_form)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()