import os
import tkinter as tk
from tkinter import messagebox
from src.utils import validate_folder_name, show_message

def list_directories(frame, base_path, filter_text="", open_action_modal=None):
    """Lista as pastas dentro do diretório especificado, filtrando pelo texto."""
    for widget in frame.winfo_children():
        widget.destroy()

    for i, folder in enumerate(os.listdir(base_path)):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path) and filter_text.lower() in folder.lower():
            btn = tk.Button(
                frame,
                text=folder,
                command=lambda p=folder_path: open_action_modal(frame, p) if open_action_modal else None,
                font=("Arial", 10, "bold"),
                height=2,
                width=20,
                relief="groove",
                bg="#e0f7fa",
                activebackground="#b2ebf2",
                cursor="hand2"
            )
            btn.grid(row=i // 5, column=i % 5, padx=10, pady=10)

def create_new_folder(base_path, folder_name):
    """Cria uma nova pasta no diretório especificado."""
    is_valid, error_message = validate_folder_name(folder_name)
    if not is_valid:
        show_message("Erro", error_message, error=True)
        return

    new_folder_path = os.path.join(base_path, folder_name)
    try:
        os.makedirs(new_folder_path, exist_ok=True)
        show_message("Sucesso", f"Pasta '{folder_name}' criada com sucesso!")
    except Exception as e:
        show_message("Erro", f"Não foi possível criar a pasta: {str(e)}", error=True)
