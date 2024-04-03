import tkinter as tk
import customtkinter
from tkinter import messagebox
from control.cControlFunc import *

class TelaDepartamento(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro de Departamento")
        self.state("zoomed")

        self.label_titulo = tk.Label(self, text="Cadastro de Departamento", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.frame_campos = tk.Frame(self)
        self.frame_campos.pack(padx=20, pady=10)

        self.label_nomeDep = tk.Label(self.frame_campos, text="Nome Departamento:", font=("Arial", 14))
        self.label_nomeDep.grid(row=1, column=0, pady=5)
        self.entry_nomeDep = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_nomeDep.grid(row=1, column=1, pady=5)

        self.btn_salvar = tk.Button(self.frame_campos, text="Salvar", command=self.cadastrar_departamento)
        self.btn_salvar.grid(row=3, column=0, pady=5, padx=5, sticky="we")

        self.btnRelatorio = tk.Button(self.frame_campos, text="Relatorio", command=self.relatorio_departamento)
        self.btnRelatorio.grid(row=3, column=1, pady=5, padx=5, sticky="we")

        self.btn_voltar = tk.Button(self.frame_campos, text="Voltar", command=self.voltaMenu)
        self.btn_voltar.grid(row=3, column=2, pady=5, padx=5, sticky="we")

    def cadastrar_departamento(self):
        nm_dep = self.entry_nomeDep.get()

        if not nm_dep:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        salvaDepartamento = cDepartamento(nm_dep=nm_dep, cd_dep = '')
        salvaDepartamento.setDepartamento()

        messagebox.showinfo("Sucesso", "Departamento cadastrado com sucesso!")

    def relatorio_departamento(self):
        relatorio = tk.Toplevel(self)
        relatorio.title("Relatório de Departamentos")
        relatorio.state("zoomed")

        lbl_titulo = tk.Label(relatorio, text="Departamentos Cadastrados", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=10)

        relDepartamento = cDepartamento.getDepartamento()

        if not relDepartamento:
            lbl_msg = tk.Label(relatorio, text="Nenhum departamento cadastrado.")
            lbl_msg.pack(pady=5)
        else:
            for departamento in relDepartamento:
                lbl_dep = tk.Label(relatorio, text=f"Funcionario: {departamento.nm_func}, Departamento: {departamento.nm_dep}")
                lbl_dep.pack(pady=2)

    def voltaMenu(self):
        self.destroy()
        self.master.deiconify()
        self.master.state("zoomed")
