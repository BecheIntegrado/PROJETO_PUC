import tkinter as tk
from tkinter import messagebox

class TelaCadFunc(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro de Funcionário")
        self.configure(bg="#4F4F4F")
        self.state("zoomed")

        self.label = tk.Label(self, text="Cadastro de Funcionário")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_nome = tk.Label(self, text="Nome:" , bg="#4F4F4F", fg="white")
        self.label_nome.grid(row=1, column=0)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.grid(row=1, column=1)

        self.label_idade = tk.Label(self, text="Idade:", bg="#4F4F4F", fg="white")
        self.label_idade.grid(row=2, column=0)
        self.entry_idade = tk.Entry(self)
        self.entry_idade.grid(row=2, column=1)

        self.btnCadastrar = tk.Button(self, text="Salvar", command=self.cadastrar_funcionario)
        self.btnCadastrar.grid(row=3, column=1, pady=10, sticky="e")

        self.btnCadVolta = tk.Button(self, text="Voltar", command=self.voltaMenu)
        self.btnCadVolta.grid(row=3, column=0, pady=10)

    def cadastrar_funcionario(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()

        if not nome or not idade:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            idade = int(idade)
        except ValueError:
            messagebox.showerror("Erro", "A idade deve ser um número inteiro.")
            return

        # Aqui você pode adicionar código para salvar as informações em um banco de dados ou arquivo, etc.
        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
        print("Nome:", nome)
        print("Idade:", idade)

    def voltaMenu(self):
        self.destroy()
        self.master.deiconify()