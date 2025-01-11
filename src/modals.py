import tkinter as tk
from src.handlers import open_folder, open_with_vscode
from src.services import create_new_folder

def open_action_modal(parent, folder_path):
    """Exibe um modal com opções para abrir o repositório."""
    modal = tk.Toplevel(parent)
    modal.title("Escolha uma ação")
    modal.geometry("300x150")
    modal.resizable(False, False)
    
    label = tk.Label(modal, text=f"O que deseja fazer com:\n{folder_path}", font=("Arial", 10))
    label.pack(pady=10)
    
    btn_vscode = tk.Button(modal, text="Abrir com VSCode", command=lambda: [open_with_vscode(folder_path), modal.destroy()])
    btn_vscode.pack(pady=5)

    btn_explorer = tk.Button(modal, text="Abrir no Explorador", command=lambda: [open_folder(folder_path), modal.destroy()])
    btn_explorer.pack(pady=5)

def open_create_folder_modal(parent, base_path, update_list):
    """Exibe um modal para criar uma nova pasta."""
    modal = tk.Toplevel(parent)
    modal.title("Criar Nova Pasta")
    modal.geometry("300x150")
    modal.resizable(False, False)
    
    label = tk.Label(modal, text="Digite o nome da nova pasta:", font=("Arial", 10))
    label.pack(pady=10)

    entry = tk.Entry(modal, font=("Arial", 12), width=30)
    entry.pack(pady=5)

    def create_folder():
        folder_name = entry.get().strip()
        if folder_name:
            create_new_folder(base_path, folder_name)
            update_list()
            modal.destroy()

    btn_create = tk.Button(modal, text="Criar", command=create_folder)
    btn_create.pack(pady=5)
