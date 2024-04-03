from model.mCadastros import *
from sqlalchemy import create_engine, Column, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

class cDepartamento():
    def __init__(self, nm_dep, cd_dep):
        self.nm_dep = nm_dep
        self.cd_dep = cd_dep

    def setDepartamento(self):
        model = mDepartamento(nm_dep = self.nm_dep)
        session.add(model)
        session.commit()

    def getNameDep(self):
        response = session.query(mDepartamento.nm_dep).filter(mDepartamento.cd_dep == self.cd_dep)
        return response

    def getDepartamento():
        response = session.query(mFuncionario.nm_func, mDepartamento.nm_dep) \
            .join(mFuncionario, mFuncionario.cd_dep == mDepartamento.cd_dep)

        return response

class cFuncionario():
    def __init__(self, nm_func, nm_sobrenome, dt_nasc, dt_admissao, in_sexo, cd_dep, cd_turno):
        self.nm_func      = nm_func
        self.nm_sobrenome = nm_sobrenome
        self.dt_nasc      = dt_nasc
        self.in_sexo      = in_sexo
        self.dt_admissao  = dt_admissao
        self.cd_dep       = cd_dep
        self.cd_turno     = cd_turno

    def setFuncionario(self):
        model = mFuncionario(nm_func  = self.nm_func, nm_sobrenome = self.nm_sobrenome, dt_nasc = self.dt_nasc,
                             in_sexo  = self.in_sexo, dt_admissao  = self.dt_admissao,  cd_dep  = self.cd_dep,
                             cd_turno = self.cd_turno)
        session.add(model)
        session.flush()
        return model.cd_func

class cEndereco():
    def __init__(self, cd_func, cd_cep, nm_cidade, nm_rua, nm_bairro, nr_casa, ds_compl):
        self.cd_func = cd_func
        self.cd_cep = cd_cep
        self.nm_cidade = nm_cidade
        self.nm_rua = nm_rua
        self.nm_bairro = nm_bairro
        self.nr_casa = nr_casa
        self.ds_compl = ds_compl

    def setEndereco(self):
        model = mEndereco(cd_func   = self.cd_func,   cd_cep = self.cd_cep,  nm_cidade = self.nm_cidade, nm_rua = self.nm_rua,
                          nm_bairro = self.nm_bairro, nr_casa= self.nr_casa, ds_compl  = self.ds_compl)
        session.add(model)
        session.flush()

class cContato():
    def __init__(self, cd_func, ds_email, ds_telefone):
        self.cd_func = cd_func
        self.ds_email = ds_email
        self.ds_telefone = ds_telefone

    def setContato(self):
        model = mContato(cd_func = self.cd_func,ds_email = self.ds_email, ds_telefone = self.ds_telefone)
        session.add(model)
        session.flush()

class cTurno():
    def __init__(self, cd_turno, in_ativo, qt_tempper, hr_inicio, hr_fim):
        self.cd_turno = cd_turno
        self.qt_tempper = qt_tempper
        self.hr_inicio = hr_inicio
        self.hr_fim = hr_fim
        self.in_ativo = in_ativo

    def getTurno(self):
        response = session.query(mTurno.hr_inicio, mTurno.hr_fim).filter(mTurno.cd_turno == self.cd_turno)
        return response

    def setTurno(self):
        model = mTurno(in_ativo = self.in_ativo, qt_tempper = self.qt_tempper, hr_inicio = self.hr_inicio, hr_fim = self.hr_fim)
        session.add(model)
        session.commit()

class cCargo():
    def __init__(self, cd_cargo, nm_cargo):
        self.cd_cargo = cd_cargo
        self.nm_cargo = nm_cargo

    def setCargo(self):
        model = mCargo(nm_cargo = self.nm_cargo)
        session.add(model)
        session.commit()

    def getNomeCargo(self):
        response = session.query(mCargo.nm_cargo).filter(mCargo.cd_cargo == self.cd_cargo)


        return response

class cSalario():
    def __init__(self, qt_salbruto):
        self.qt_salbruto = qt_salbruto

    def setSalario(self):
        model = mSalario(qt_salbruto = self.qt_salbruto)
        session.add(model)
        session.flush()
        return model.cd_salario

class cCadastroFuncionario():
    def __init__(self, cd_func, cd_cargo, cd_salario, dt_inivig, dt_fimvig):
        self.cd_func = cd_func
        self.cd_cargo = cd_cargo
        self.cd_salario = cd_salario
        self.dt_inivig = dt_inivig
        self.dt_fimvig = dt_fimvig

    def setSalario(self):
        model = mSalario(cd_func = self.cd_func, cd_cargo = self.cd_cargo, cd_salario = self.cd_salario, dt_inivig = self.dt_inivig, dt_fimvig = self.dt_fimvig)
        session.add(model)
        session.flush()
