import os
import tkinter as tk

def open_folder(folder_path):
    """Abre o diretório no explorador de arquivos."""
    os.startfile(folder_path)

def list_directories(frame, base_path, filter_text=""):
    """Lista as pastas dentro do diretório especificado, filtrando pelo texto."""
    # Limpa os botões existentes
    for widget in frame.winfo_children():
        widget.destroy()

    # Filtra e cria botões para as pastas
    for i, folder in enumerate(os.listdir(base_path)):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path) and filter_text.lower() in folder.lower():
            btn = tk.Button(frame, text=folder, command=lambda p=folder_path: open_folder(p), 
                            font=("Arial", 10), height=5, width=10, relief="raised", bg="#d0e0f0")
            btn.grid(row=i // 5, column=i % 5, padx=10, pady=10)
