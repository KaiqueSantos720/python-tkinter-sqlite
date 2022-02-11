from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco_gravar_dados as bdd


def preencher_treeview():
    treeview.delete(*treeview.get_children())  # Deletar registro do treeview
    for i in bdd.consulta("SELECT * FROM tb_times ORDER BY id_time"):
        treeview.insert("", "end", values=i)


def inserir():
    if entrada_nome.get() == '' or entrada_pais.get() == '' or entrada_cidade.get() == '' or entrada_liga.get() == '' or entrada_jogador.get() == '':
        messagebox.showinfo(title="ATENÇÃO", message="Preencha os campos")
    try:
        query_sql = "INSERT INTO tb_times (nome_time, pais_time, cidade_time, liga, jogador_destaque) VALUES ('" + entrada_nome.get() + "', '" + entrada_pais.get() + "', '" + entrada_cidade.get() + "', '" + entrada_liga.get() + "', '" + entrada_jogador.get() + "')"
        bdd.query(query_sql)
    except:
        messagebox.showerror(title='ERRO', message="ERRO AO INSERIR")
    preencher_treeview()
    entrada_nome.delete(0, END)
    entrada_pais.delete(0, END)
    entrada_cidade.delete(0, END)
    entrada_liga.delete(0, END)
    entrada_jogador.delete(0, END)


def deletar():
    try:
        query_sql = "DELETE FROM tb_times WHERE id_time="+id_deletar.get()
        bdd.query(query_sql)
    except:
        messagebox.showerror(title="ERRO", message="ERRO AO DELETAR")
    preencher_treeview()
    id_deletar.delete(0, END)


def pesquisar():
    treeview.delete(*treeview.get_children())
    query_sql = "SELECT * FROM tb_times WHERE nome_time LIKE '%"+vnomepesquisar.get()+"%'"
    for i in bdd.consulta(query_sql):
        treeview.insert("", "end", values=i)
    vnomepesquisar.delete(0, END)


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

quadrogrid = LabelFrame(programa, text="Times")
quadrogrid.pack(fill="both", expand="yes", padx=10, pady=10)

treeview = ttk.Treeview(quadrogrid, columns=('id', 'nome', 'pais', 'cidade', 'liga', 'jogador'), show='headings')
treeview.column('id', minwidth=0, width=50)
treeview.column('nome', minwidth=0, width=150)
treeview.column('pais', minwidth=0, width=100)
treeview.column('cidade', minwidth=0, width=100)
treeview.column('liga', minwidth=0, width=100)
treeview.column('jogador', minwidth=0, width=250)

treeview.heading('id', text='ID', anchor='w')
treeview.heading('nome', text='Nome', anchor='w')
treeview.heading('pais', text='País', anchor='w')
treeview.heading('cidade', text='Cidade', anchor='w')
treeview.heading('liga', text='Liga', anchor='w')
treeview.heading('jogador', text='Jogador de Destaque', anchor='w')
treeview.pack(fill="both", expand="yes")
preencher_treeview()

quadro_inserir = LabelFrame(programa, text="Inserir novos times")
quadro_inserir.pack(fill="both", expand="yes", padx=10, pady=10)

label1 = Label(quadro_inserir, text="Nome")
label1.pack(side="left")
entrada_nome = Entry(quadro_inserir)
entrada_nome.pack(side="left", padx=10)

label2 = Label(quadro_inserir, text="País")
label2.pack(side="left")
entrada_pais = Entry(quadro_inserir)
entrada_pais.pack(side="left", padx=10)

label3 = Label(quadro_inserir, text="Cidade")
label3.pack(side="left")
entrada_cidade = Entry(quadro_inserir)
entrada_cidade.pack(side="left", padx=10)

label4 = Label(quadro_inserir, text="Liga")
label4.pack(side="left")
entrada_liga = Entry(quadro_inserir)
entrada_liga.pack(side="left", padx=10)

label5 = Label(quadro_inserir, text="Jogador de Destaque")
label5.pack(side="left")
entrada_jogador = Entry(quadro_inserir)
entrada_jogador.pack(side="left", padx=10)

botao_inserir = Button(quadro_inserir, text="Inserir", command=inserir)
botao_inserir.pack(side="left", padx=10)


quadro_pesquisar = LabelFrame(programa, text="Pesquisar Times")
quadro_pesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

label_id = Label(quadro_pesquisar, text="Pesquisar por Nome")
label_id.pack(side="left")

vnomepesquisar = Entry(quadro_pesquisar)
vnomepesquisar.pack(side="left", padx=10)

botao_pesquisar = Button(quadro_pesquisar, text="Pesquisar", command=pesquisar)
botao_pesquisar.pack(side="left", padx=10)

botao_mostrar_todos = Button(quadro_pesquisar, text="Mostrar Todos", command=preencher_treeview)
botao_mostrar_todos.pack(side="left", padx=10)

quadro_deletar = LabelFrame(programa, text="Deletar Times")
quadro_deletar.pack(fill="both", expand="yes", padx=10, pady=10)

label_delete = Label(quadro_deletar, text="Deletar por ID")
label_delete.pack(side="left")

id_deletar = Entry(quadro_deletar)
id_deletar.pack(side="left", padx=10)

botao_deletar = Button(quadro_deletar, text="Deletar", command=deletar)
botao_deletar.pack(side="left", padx=10)


programa.mainloop()
