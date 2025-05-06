import customtkinter as CTk
import os

CTk.set_appearance_mode("light")
CTk.set_default_color_theme("dark-blue")

backup_pasta = "backup"
os.makedirs(backup_pasta, exist_ok=True)

arquivos = {}

def armazenar():
    nome = entry_arquivo.get()
    conteudo = box_conteudo.get("1.0", "end").strip()

    if not nome or not conteudo:
        info_label.configure(text="Preencha todos os campos.")
        return

    arquivos[nome] = conteudo

    caminho = os.path.join(backup_pasta, nome)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)

    info_label.configure(text=f"'{nome}' armazenado com sucesso.")

def recuperar():
    nome = entry_arquivo.get()

    conteudo = arquivos.get(nome)
    if conteudo is None:
        caminho = os.path.join(backup_pasta, nome)
        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()
                arquivos[nome] = conteudo
    if conteudo:
        box_conteudo.delete("1.0", "end")
        box_conteudo.insert("1.0", conteudo)
        info_label.configure(text=f"'{nome}' recuperado.")
    else:
        info_label.configure(text="Arquivo vazio ou corrompido.")

app = CTk.CTk()
app.title("Sistema de Arquivos")
app.geometry("400x500")

entry_arquivo = CTk.CTkEntry(app, placeholder_text="Nome do Arquivo")
entry_arquivo.pack(pady=10)

box_conteudo = CTk.CTkTextbox(app, width=300, height=200)
box_conteudo.pack(pady=10)

btn_armazenar = CTk.CTkButton(app, text="Armazenar Arquivo", command=armazenar)
btn_armazenar.pack(pady=5)

btn_recuperar = CTk.CTkButton(app, text="Recuperar Arquivo", command=recuperar)
btn_recuperar.pack(pady=5)

info_label = CTk.CTkLabel(app, text="")
info_label.pack(pady=10)

app.mainloop()
