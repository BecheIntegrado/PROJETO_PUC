import tkinter as tk
import customtkinter
from tkinter import messagebox
from control.cControlFunc import *

class TelaTurno(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro de Funcionário")
        self.state("zoomed")

        self.label_titulo = tk.Label(self, text="Cadastro de Turno", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.frame_campos = tk.Frame(self)
        self.frame_campos.pack(padx=20, pady=10)

        self.label_qtAlmoco = tk.Label(self.frame_campos, text="Tempo Almoço (minutos):" , font=("Arial", 14))
        self.label_qtAlmoco.grid(row=1, column=0, pady=5)
        self.entry_qtAlmoco = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_qtAlmoco.grid(row=1, column=1, pady=5)

        self.label_turno = tk.Label(self.frame_campos, text="Inicio/Fim:", font=("Arial", 14))
        self.label_turno.grid(row=2, column=0, pady=5)
        self.entry_iniTurno = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_iniTurno.grid(row=2, column=1, pady=5)
        self.entry_fimTurno = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_fimTurno.grid(row=2, column=2, pady=5)

        self.btn_salvar = tk.Button(self.frame_campos, text="Salvar", command=self.cadastrar_turno)
        self.btn_salvar.grid(row=3, column=0, pady=5, padx=5, sticky="we")

        self.btn_voltar = tk.Button(self.frame_campos, text="Voltar", command=self.voltaMenu)
        self.btn_voltar.grid(row=3, column=1, pady=5, padx=5, sticky="we")


    def cadastrar_turno(self):
        qt_tempper = int(self.entry_qtAlmoco.get())
        hr_inicio = self.entry_iniTurno.get()
        hr_fim = self.entry_fimTurno.get()
        in_ativo = 'S'
        cd_turno = 0
        if not qt_tempper or not hr_inicio or not hr_fim:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        salvaTurno = cTurno(cd_turno = cd_turno, in_ativo = in_ativo, qt_tempper = qt_tempper, hr_inicio = hr_inicio, hr_fim = hr_fim)
        salvaTurno.setTurno()

        messagebox.showinfo("Sucesso", "Departamento cadastrado com sucesso!")

    def voltaMenu(self):
        self.destroy()
        self.master.deiconify()
        self.master.state("zoomed")
