import os
from tkinter import messagebox

def validate_folder_name(folder_name):
    """Valida o nome da nova pasta, garantindo que não tenha caracteres inválidos."""
    invalid_chars = '<>:"/\\|?*'
    if not folder_name:
        return False, "O nome da pasta não pode estar vazio."
    if any(char in folder_name for char in invalid_chars):
        return False, f"O nome da pasta não pode conter os seguintes caracteres: {invalid_chars}"
    return True, ""

def show_message(title, message, error=False):
    """Exibe uma mensagem ao usuário."""
    if error:
        messagebox.showerror(title, message)
    else:
        messagebox.showinfo(title, message)

def normalize_string(input_string):
    """Remove espaços extras e transforma a string para um formato padrão."""
    return " ".join(input_string.strip().split())
