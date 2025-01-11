import os
import tkinter as tk
from tkinter import ttk
from config.settings import BASE_DIR
from src.handlers import open_folder, list_directories

def run_app():
    def on_mouse_wheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    def update_list(*args):
        filter_text = search_var.get()
        list_directories(frame, BASE_DIR, filter_text)

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Lista de Repositórios")
    root.geometry("800x600")

    # Barra de pesquisa
    search_var = tk.StringVar()
    search_var.trace("w", update_list)
    search_entry = tk.Entry(root, textvariable=search_var, font=("Arial", 12), width=50)
    search_entry.pack(pady=10)

    # Configuração do frame com barra de rolagem
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Adiciona os widgets na janela principal
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Frame interno que conterá os botões
    frame = ttk.Frame(scrollable_frame)
    frame.pack()

    # Conecta o scroll do mouse à barra de rolagem
    root.bind_all("<MouseWheel>", on_mouse_wheel)

    # Lista inicial dos diretórios
    list_directories(frame, BASE_DIR)

    # Inicia o loop da aplicação
    root.mainloop()
