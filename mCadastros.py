from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import NUMERIC, VARCHAR, DATE
from sqlalchemy import Sequence
import cx_Oracle

lib_dir = "C:\Oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)
USER = 'C##BANCO'
PASSWD = '123'
HOST = 'localhost'
PORT = 1521
SID = "xe"
sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"
engine = create_engine(url=instance, echo=True, max_identifier_length=30)
session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))

response = session.execute(text('SELECT * FROM CADASTRO_FUNCIONARIO'))
for o in response:
    print(o)

class Base(DeclarativeBase):
    pass

class Cadastro_funcionario(Base):
    __tablename__ = "CADASTRO_FUNCIONARIO"
    cd_cadfunc = mapped_column(NUMERIC(9), Sequence('SQ_CADASTRO_FUNCIONARIO'), nullable=False, primary_key=True)
    cd_func = mapped_column(NUMERIC(9), nullable=False)
    cd_cargo = mapped_column(NUMERIC(9), nullable=False)
    cd_salario = mapped_column(NUMERIC(9), nullable=False)
    dt_inivig = mapped_column(DATE, nullable=False)
    dt_fimvig = mapped_column(DATE, nullable=False)

    def __str__(self) -> str:
        return super().__str__()

class Departamento(Base):
    __tablename__ = "DEPARTAMENTO"
    cd_dep = mapped_column(NUMERIC(9), Sequence('SQ_DEPARTAMENTO'), nullable=False, primary_key=True)
    cd_func = mapped_column(NUMERIC(9), nullable=True)
    nm_dep = mapped_column(VARCHAR(60), nullable=False)

#def criaFuncionario(cpf, nome, email, telefone, data_nasc):
#    pessoa = Pessoa(cpf=cpf, nome=nome, email=email, telefone=telefone, data_nasc=datetime.strptime(data_nasc, '%d-%m-%Y'))
#    return pessoa

#response = session.query(func.count(cadastro_funcionario.cd_cadfunc)).all()
#print(response)

#response = session.query(cadastro_funcionario).first()
#response = session.query(Pessoa).order_by(Pessoa.nome)

# Clausulas
#response: list[tuple[Pessoa, Usuario]] = session.query(Pessoa, Usuario).join(Usuario, Usuario.codigo == Pessoa.codigo).all()

#result = session.query(Pessoa.nome, Usuario.carteirinha, Emprestimo).join(Usuario, Usuario.codigo == Pessoa.codigo).join(Emprestimo, Emprestimo.codigo_usuario == Usuario.codigo, isouter=True).order_by(Pessoa.nome).all()

#result = session.query(Pessoa.codigo, Pessoa.nome, func.count(distinct(LivrosCategorias.codigo_categoria)).label('Numero de Categorias')).join(Usuario, Usuario.codigo == Pessoa.codigo).join(Emprestimo, Emprestimo.codigo_usuario == Usuario.codigo, isouter=True).join(EmprestimosLivros, EmprestimosLivros.codigo_emprestimo == Emprestimo.codigo, isouter=True).join(Livro, Livro.isbn == EmprestimosLivros.isbn_livro, isouter=True).join(LivrosCategorias, LivrosCategorias.isbn_livro == Livro.isbn, isouter=True).group_by(Pessoa.codigo, Pessoa.nome).having(func.count(distinct(LivrosCategorias.codigo_categoria)) >= 1).all()

#print(result)


