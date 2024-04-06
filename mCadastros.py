from sqlalchemy.orm import *
from sqlalchemy import *

import cx_Oracle

lib_dir = "C:\Oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)
USER = 'C##FUNC'
PASSWD = '123'
HOST = 'localhost'
PORT = 1521
SID = "xe"
sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"
engine = create_engine(url=instance, echo=True, max_identifier_length=30)
session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))

class Base(DeclarativeBase):
    pass

class mCargo(Base):
    __tablename__ = "CARGO"
    cd_cargo      = mapped_column(INTEGER, Sequence('SQ_CARGO'), nullable=False, primary_key=True)
    nm_cargo      = mapped_column(VARCHAR(60), nullable=False)

class mDepartamento(Base):
    __tablename__ = "DEPARTAMENTO"
    cd_dep        = mapped_column(INTEGER, Sequence('SQ_DEPARTAMENTO'), nullable=False, primary_key=True)
    nm_dep        = mapped_column(VARCHAR(60), nullable=False)

class mTurno(Base):
    __tablename__ = "TURNO"
    cd_turno        = mapped_column(INTEGER, Sequence('SQ_TURNO'), nullable=False, primary_key=True)
    in_ativo        = mapped_column(CHAR(1), nullable=False)
    qt_tempper      = mapped_column(INTEGER, nullable=False)
    hr_inicio       = mapped_column(CHAR(5), nullable=True)
    hr_fim          = mapped_column(CHAR(5), nullable=True)

class mSalario(Base):
    __tablename__ = "SALARIO"
    cd_salario  = mapped_column(INTEGER, Sequence('SQ_SALARIO'), nullable=False, primary_key=True)
    qt_salbruto = mapped_column(INTEGER , nullable=False)

class mFuncionario(Base):
    __tablename__ = "FUNCIONARIO"
    cd_func       = mapped_column(INTEGER, Sequence('SQ_FUNCIONARIO'), nullable=False, primary_key=True)
    cd_dep        = mapped_column(INTEGER, ForeignKey(mDepartamento.cd_dep))
    cd_turno      = mapped_column(INTEGER, ForeignKey(mTurno.cd_turno))
    nm_func       = mapped_column(VARCHAR(60), nullable=False)
    nm_sobrenome  = mapped_column(VARCHAR(60), nullable=False)
    dt_nasc       = mapped_column(DATE, nullable=False)
    dt_admissao   = mapped_column(DATE, nullable=False)
    dt_demissao   = mapped_column(DATE, nullable=True)
    in_sexo       = mapped_column(CHAR(1), nullable=False)

class mPonto(Base):
    __tablename__ = "PONTO"
    cd_ponto        = mapped_column(INTEGER, Sequence('SQ_PONTO'), nullable=False, primary_key=True)
    cd_func         = mapped_column(INTEGER, ForeignKey(mFuncionario.cd_func))
    dt_expediente   = mapped_column(DATE, nullable=True)
    dt_entrada      = mapped_column(DATE, nullable=True)
    dt_saida        = mapped_column(DATE, nullable=True)

class mContato(Base):
    __tablename__ = "CONTATO"
    cd_contato    = mapped_column(INTEGER, Sequence('SQ_CONTATO'), nullable=False, primary_key=True)
    cd_func       = mapped_column(INTEGER, ForeignKey(mFuncionario.cd_func))
    ds_email      = mapped_column(VARCHAR(100), nullable=True)
    ds_telefone   = mapped_column(VARCHAR(12), nullable=True)

class mEndereco(Base):
    __tablename__ = "ENDERECO"
    cd_ender      = mapped_column(INTEGER, Sequence('SQ_ENDERECO'), nullable=False, primary_key=True)
    cd_cep        = mapped_column(VARCHAR(10), nullable=False)
    cd_func       = mapped_column(INTEGER, ForeignKey(mFuncionario.cd_func))
    nm_cidade     = mapped_column(VARCHAR(60), nullable=False)
    nm_rua        = mapped_column(VARCHAR(60), nullable=False)
    nm_bairro     = mapped_column(VARCHAR(60), nullable=False)
    nr_casa       = mapped_column(INTEGER,  nullable=False)
    ds_compl      = mapped_column(VARCHAR(60), nullable=True)

class mCadastro_funcionario(Base):
    __tablename__ = "CADASTRO_FUNCIONARIO"
    cd_cadfunc    = mapped_column(INTEGER, Sequence('SQ_CADASTRO_FUNCIONARIO'), nullable=False, primary_key=True)
    cd_func       = mapped_column(INTEGER, ForeignKey(mFuncionario.cd_func))
    cd_cargo      = mapped_column(INTEGER, nullable=False)
    cd_salario    = mapped_column(INTEGER, nullable=False)
    dt_inivig     = mapped_column(DATE, nullable=False)
    dt_fimvig     = mapped_column(DATE, nullable=False)

    def __str__(self) -> str:
        return super().__str__()
