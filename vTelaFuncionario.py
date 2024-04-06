import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from control.cControlFunc import *
from tkcalendar import DateEntry

class TelaCadFunc(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro de Funcionário")
        self.state("zoomed")

        self.label_titulo = tk.Label(self, text="Cadastro de Funcionário", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.frame_campos = tk.Frame(self)
        self.frame_campos.pack(padx=20, pady=10)

        self.label_nome = tk.Label(self.frame_campos, text="Nome:", font=("Arial", 14))
        self.label_nome.grid(row=1, column=0, pady=5, sticky="w")
        self.entry_nome = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_nome.grid(row=1, column=1, pady=5, sticky="w")

        self.label_sobrenome = tk.Label(self.frame_campos, text="Sobrenome:", font=("Arial", 14))
        self.label_sobrenome.grid(row=2, column=0, pady=5, sticky="w")
        self.entry_sobrenome = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_sobrenome.grid(row=2, column=1, pady=5, sticky="w")

        self.label_dt_nasc = tk.Label(self.frame_campos, text="Data de Nascimento:", font=("Arial", 14))
        self.label_dt_nasc.grid(row=3, column=0, pady=5, sticky="w")
        self.entry_dt_nasc = DateEntry(self.frame_campos, font=("Arial", 14), date_pattern='dd/mm/yyyy')
        self.entry_dt_nasc.grid(row=3, column=1, pady=5, sticky="w")

        self.label_sexo = tk.Label(self.frame_campos, text="Sexo:", font=("Arial", 14))
        self.label_sexo.grid(row=4, column=0, pady=5, sticky="w")
        self.sexo_value = tk.StringVar(value="Masculino")
        self.sexo_combobox = ttk.Combobox(self.frame_campos, font=("Arial", 14), textvariable=self.sexo_value, values=["Masculino", "Feminino"], state="readonly")
        self.sexo_combobox.grid(row=4, column=1, pady=5, sticky="w")

        self.label_cep = tk.Label(self.frame_campos, text="CEP:", font=("Arial", 14))
        self.label_cep.grid(row=5, column=0, pady=5, sticky="w")
        self.entry_cep = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_cep.grid(row=5, column=1, pady=5, sticky="w")

        self.label_cidade = tk.Label(self.frame_campos, text="Cidade:", font=("Arial", 14))
        self.label_cidade.grid(row=6, column=0, pady=5, sticky="w")
        self.entry_cidade = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_cidade.grid(row=6, column=1, pady=5, sticky="w")

        self.label_rua = tk.Label(self.frame_campos, text="Rua:", font=("Arial", 14))
        self.label_rua.grid(row=7, column=0, pady=5, sticky="w")
        self.entry_rua = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_rua.grid(row=7, column=1, pady=5, sticky="w")

        self.label_bairro = tk.Label(self.frame_campos, text="Bairro:", font=("Arial", 14))
        self.label_bairro.grid(row=8, column=0, pady=5, sticky="w")
        self.entry_bairro = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_bairro.grid(row=8, column=1, pady=5, sticky="w")

        self.label_nr_casa = tk.Label(self.frame_campos, text="Nr casa:", font=("Arial", 14))
        self.label_nr_casa.grid(row=9, column=0, pady=5, sticky="w")
        self.entry_nr_casa = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_nr_casa.grid(row=9, column=1, pady=5, sticky="w")

        self.label_complemento = tk.Label(self.frame_campos, text="Complemento:", font=("Arial", 14))
        self.label_complemento.grid(row=10, column=0, pady=5, sticky="w")
        self.entry_complemento = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_complemento.grid(row=10, column=1, pady=5, sticky="w")

        self.label_cd_dep = tk.Label(self.frame_campos, text="Departamento:", font=("Arial", 14))
        self.label_cd_dep.grid(row=11, column=0, pady=5, sticky="w")
        self.entry_cd_dep = tk.Entry(self.frame_campos, font=("Arial", 14), width=5)
        self.entry_cd_dep.bind("<KeyPress-Tab>", self.getNomeDep)
        self.entry_cd_dep.grid(row=11, column=1, pady=5, sticky="w")
        self.entry_nm_dep = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_nm_dep.grid(row=11, column=2, pady=5, sticky="w")
        self.entry_nm_dep.bind("<Key>", self.getNomeDep)

        self.label_cd_cargo = tk.Label(self.frame_campos, text="Cargo:", font=("Arial", 14))
        self.label_cd_cargo.grid(row=12, column=0, pady=5, sticky="w")
        self.entry_cd_cargo = tk.Entry(self.frame_campos, font=("Arial", 14), width=5)
        self.entry_cd_cargo.bind("<KeyPress-Tab>", self.getNomeCargo)
        self.entry_cd_cargo.grid(row=12, column=1, pady=5, sticky="w")
        self.entry_nm_cargo = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_nm_cargo.grid(row=12, column=2, pady=5, sticky="w")
        self.entry_nm_cargo.bind("<Key>", self.getNomeCargo)

        self.label_cd_turno = tk.Label(self.frame_campos, text="Turno:", font=("Arial", 14))
        self.label_cd_turno.grid(row=13, column=0, pady=5, sticky="w")
        self.entry_cd_turno = tk.Entry(self.frame_campos, font=("Arial", 14), width=5)
        self.entry_cd_turno.bind("<KeyPress-Tab>", self.getTurno)
        self.entry_cd_turno.grid(row=13, column=1, pady=5, sticky="w")
        self.entry_nm_turno = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_nm_turno.grid(row=13, column=2, pady=5, sticky="w")
        self.entry_nm_turno.bind("<Key>", self.getTurno)

        self.label_salario = tk.Label(self.frame_campos, text="Salario:", font=("Arial", 14))
        self.label_salario.grid(row=14, column=0, pady=5, sticky="w")
        self.entry_salario = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_salario.grid(row=14, column=1, pady=5, sticky="w")

        self.label_email = tk.Label(self.frame_campos, text="Email:", font=("Arial", 14))
        self.label_email.grid(row=15, column=0, pady=5, sticky="w")
        self.entry_email = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_email.grid(row=15, column=1, pady=5, sticky="w")

        self.label_telefone = tk.Label(self.frame_campos, text="Telefone:", font=("Arial", 14))
        self.label_telefone.grid(row=16, column=0, pady=5, sticky="w")
        self.entry_telefone = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_telefone.grid(row=16, column=1, pady=5, sticky="w")

        self.btn_salvar = tk.Button(self.frame_campos, text="Salvar", command=self.cadastrar_funcionario)
        self.btn_salvar.grid(row=17, column=0, pady=5, padx=5, sticky="we")

        self.btn_voltar = tk.Button(self.frame_campos, text="Voltar", command=self.voltaMenu)
        self.btn_voltar.grid(row=17, column=1, pady=5, padx=5, sticky="we")

    def getTurno(self, event):
        cd_turno = self.entry_cd_turno.get()
        if not cd_turno:
            messagebox.showerror("Erro", "Por favor, informe o código do turno.")
            return

        turno = cTurno(cd_turno = cd_turno, in_ativo = '', qt_tempper = '', hr_inicio = '', hr_fim = '')
        nomeTurno = turno.getTurno()

        if not nomeTurno:
            messagebox.showerror("Erro", "Departamento não encontrado.")
            return

        print(nomeTurno)
        self.entry_nm_turno.delete(0, tk.END)  # Limpa o campo de entrada do nome do departamento
        self.entry_nm_turno.insert(0, nomeTurno[0].hr_inicio + " - " + nomeTurno[0].hr_fim)  # Insere o nome do departamento no campo de entrada


        return nomeTurno

    def getNomeDep(self, event):
        cd_dep = self.entry_cd_dep.get()
        if not cd_dep:
            messagebox.showerror("Erro", "Por favor, informe o código do departamento.")
            return

        departamento = cDepartamento(nm_dep='', cd_dep=cd_dep)
        nomeDep = departamento.getNameDep()

        if not nomeDep:
            messagebox.showerror("Erro", "Departamento não encontrado.")
            return

        self.entry_nm_dep.delete(0, tk.END)  # Limpa o campo de entrada do nome do departamento
        self.entry_nm_dep.insert(0, nomeDep[0].nm_dep)  # Insere o nome do departamento no campo de entrada

        return nomeDep

    def getNomeCargo(self, event):
        cd_cargo = self.entry_cd_cargo.get()
        if not cd_cargo:
            messagebox.showerror("Erro", "Por favor, informe o código do cargo.")
            return

        buscaCargo = cCargo(cd_cargo=cd_cargo, nm_cargo='')
        nomeCargo  = buscaCargo.getNomeCargo()

        if not nomeCargo:
            messagebox.showerror("Erro", "Cargo não encontrado.")
            return

        self.entry_nm_cargo.delete(0, tk.END)  # Limpa o campo de entrada do nome do departamento
        self.entry_nm_cargo.insert(0, nomeCargo[0].nm_cargo)  # Insere o nome do departamento no campo de entrada

        return nomeCargo

    def cadastrar_funcionario(self):
        nm_func = self.entry_nome.get()
        nm_sobrenome = self.entry_sobrenome.get()
        dt_admissao = datetime.date.today()
        dt_nasc = self.entry_dt_nasc.get_date().strftime('%d/%m/%Y')
        combo_sexo = self.sexo_combobox.get()
        in_sexo = ''
        cd_dep = self.entry_cd_dep.get()
        cd_cargo = self.entry_cd_cargo.get()
        cd_cep = self.entry_cep.get()
        nm_cidade = self.entry_cidade.get()
        nm_rua = self.entry_rua.get()
        nm_bairro = self.entry_bairro.get()
        nr_casa = self.entry_nr_casa.get()
        ds_compl = self.entry_complemento.get()
        cd_turno = self.entry_cd_turno.get()
        ds_email = self.entry_email.get()
        ds_telefone = self.entry_telefone.get()
        qt_salbruto = self.entry_salario.get()
        dt_inivig = datetime.date.today()

        if not nm_func or not nm_sobrenome or not dt_nasc or not combo_sexo:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            dt_nasc = dt_nasc
        except ValueError:
            messagebox.showerror("Erro", "A idade deve ser um número inteiro.")
            return

        if combo_sexo == "Masculino":
            in_sexo = "M"
        else:
            in_sexo = "F"


        salvaFuncionario = cFuncionario(nm_func     = nm_func,     nm_sobrenome = nm_sobrenome,  dt_nasc = dt_nasc,
                                        dt_admissao = dt_admissao, in_sexo      = in_sexo,       cd_dep  = cd_dep,
                                        cd_turno    = cd_turno)

        cd_func = salvaFuncionario.setFuncionario()

        salvarEndereco = cEndereco(cd_func = cd_func, cd_cep   = cd_cep,  nm_cidade = nm_cidade, nm_rua = nm_rua, nm_bairro = nm_bairro,
                                   nr_casa = nr_casa,  ds_compl = ds_compl)

        salvaContato = cContato(cd_func = cd_func, ds_email = ds_email, ds_telefone = ds_telefone)

        salvaSalario = cSalario(qt_salbruto = qt_salbruto)

        try:
            salvarEndereco.setEndereco()
            salvaContato.setContato()
            salvaSalario.setSalario()

            cd_salario = salvaSalario.setSalario()

            print(cd_salario)

            salvaCadFunc = cCadFunc(cd_func = cd_func, cd_cargo = cd_cargo, cd_salario = cd_salario, dt_inivig = dt_inivig, dt_fimvig = '')

            salvaCadFunc.setCadFunc()

        except ValueError:
            session.rollback()
            messagebox.showerror("Erro", "Erro em salvar os registros.")
            return

        session.commit()

        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
        self.entry_nome.delete(0, tk.END)
        self.entry_sobrenome.delete(0, tk.END)
        self.entry_dt_nasc.delete(0, tk.END)
        self.sexo_combobox.set("Masculino")
        self.entry_cep.delete(0, tk.END)
        self.entry_cidade.delete(0, tk.END)
        self.entry_rua.delete(0, tk.END)
        self.entry_bairro.delete(0, tk.END)
        self.entry_nr_casa.delete(0, tk.END)
        self.entry_complemento.delete(0, tk.END)
        self.entry_cd_dep.delete(0, tk.END)
        self.entry_nm_dep.delete(0, tk.END)
        self.entry_cd_cargo.delete(0, tk.END)
        self.entry_nm_cargo.delete(0, tk.END)
        self.entry_cd_turno.delete(0, tk.END)
        self.entry_nm_turno.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_salario.delete(0, tk.END)

    def voltaMenu(self):
        self.destroy()
        self.master.deiconify()
        self.master.state("zoomed")
