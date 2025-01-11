import os
import subprocess
from tkinter import messagebox

def open_folder(folder_path):
    """Abre o diretório no explorador de arquivos."""
    os.startfile(folder_path)

def open_with_vscode(folder_path):
    """Abre o diretório no Visual Studio Code."""
    vscode_path = r"C:\Users\blubs\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    if not os.path.exists(vscode_path):
        messagebox.showerror("Erro", "VSCode não encontrado no caminho especificado.")
        return
    
    try:
        subprocess.run([vscode_path, folder_path], check=True)
    except subprocess.SubprocessError as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o VSCode: {str(e)}")
