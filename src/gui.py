import os
import tkinter as tk
from tkinter import ttk
from config.settings import BASE_DIR
from src.services import list_directories
from src.modals import open_action_modal, open_create_folder_modal

def run_app():
    def on_mouse_wheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    def update_list(*args):
        filter_text = search_var.get()
        list_directories(frame, BASE_DIR, filter_text, open_action_modal)

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Lista de Repositórios")
    root.geometry("1000x700")
    root.configure(bg="#f5f5f5")
    icon_path = os.path.join(os.path.dirname(__file__), "../assets/icon.ico")
    root.iconbitmap(icon_path) 

    # Frame para barra de pesquisa e lupa
    search_frame = tk.Frame(root, bg="#f5f5f5")
    search_frame.pack(pady=10)

    # Barra de pesquisa
    search_var = tk.StringVar()
    search_var.trace("w", update_list)
    search_entry = tk.Entry(search_frame, textvariable=search_var, font=("Arial", 12), width=50, relief="flat")
    search_entry.pack(side="left", padx=5, ipady=5)
    search_entry.configure(highlightbackground="#ddd", highlightthickness=1, bd=0)

    # Botão "Nova Pasta"
    btn_new_folder = tk.Button(
        root,
        text="Nova Pasta",
        command=lambda: open_create_folder_modal(root, BASE_DIR, update_list),
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2",
    )
    btn_new_folder.pack(pady=10)

    # Configuração do frame com barra de rolagem
    canvas = tk.Canvas(root, bg="#f5f5f5", highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Frame interno que conterá os botões
    frame = ttk.Frame(scrollable_frame, style="Custom.TFrame")
    frame.pack()

    # Conecta o scroll do mouse à barra de rolagem
    root.bind_all("<MouseWheel>", on_mouse_wheel)

    # Lista inicial dos diretórios
    list_directories(frame, BASE_DIR, open_action_modal=open_action_modal)

    root.mainloop()
