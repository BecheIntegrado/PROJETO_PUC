import tkinter as tk
from tkinter import messagebox

class TelaDepartamento(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro de Departamento")
        self.state("zoomed")

        self.label = tk.Label(self, text="Cadastro de Departamento")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_nome = tk.Label(self, text="Nome:")
        self.label_nome.grid(row=1, column=0)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.grid(row=1, column=1)

        self.btnCadastrar = tk.Button(self, text="Salvar", command=self.cadastrar_departamento)
        self.btnCadastrar.grid(row=2, column=0, pady=10)

        self.btnRelatorio = tk.Button(self, text="Relatório", command=self.relatorio_departamento)
        self.btnRelatorio.grid(row=2, column=1, pady=10)

        self.btnCadVolta = tk.Button(self, text="Voltar", command=self.voltaMenu)
        self.btnCadVolta.grid(row=2, column=3, pady=10)

    def cadastrar_departamento(self):
        nm_dep = self.entry_nome.get()

        if not nm_dep:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        #departamento = Departamento(nm_dep=nm_dep)
        #return departamento

        messagebox.showinfo("Sucesso", "Departamento cadastrado com sucesso!")
        print("Nome:", nm_dep)

    def relatorio_departamento(self):
        pass

    def voltaMenu(self):
        self.destroy()
        self.master.deiconify()
