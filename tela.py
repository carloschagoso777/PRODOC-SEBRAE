from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import sqlite3
from tkinter import messagebox

from PIL import ImageTk, Image

import datetime
from tkcalendar import Calendar, DateEntry
from datetime import date

now = datetime.datetime.now()
dataHoje = now.strftime('%Y-%m-%d')
#importando o main
class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('documento.db')
        self.c = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS documento( 
                       id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL,departamento TEXT NOT NULL,data TEXT NOT NULL, caixa TEXT NOT NULL, temporaridade TEXT NOT NULL, tipo TEXT NOT NULL ,descricao TEXT NOT NULL, data3 TEXT NOT NULL, data2 TEXT NOT NULL, estado TEXT NOT NULL,classe TEXT NOT NULL,pdf TEXT NOT NULL,op1 TEXT,op2 TEXT,op3 TEXT)''')
        
#'ID','Nome','Area','Origem','Acondicionamento','Temporaridade','Suporte','Descricao',"data3",data2,estado,classe,pdf

    def register_student(self,documento):
        self.c.execute("INSERT INTO documento(nome, departamento, data, caixa, temporaridade,tipo, descricao,data3,data2,estado,classe,pdf,op1,op2) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(documento))
        self.conn.commit()
#mostrando mensagem de sucesso
        messagebox.showinfo('registro com sucesso')

    def view_all_documents(self): 
        self.c.execute("SELECT id,nome,departamento,data,caixa,temporaridade,tipo,descricao,op1 FROM documento")
        dados = self.c.fetchall()
        #for i in dados:  
         #dad = [(i[0],i[1],i[2],i[3])]
         #return(dad)
     
        #print(dados)
        
          
        #return(dados) 
	   #da = ({dados[0]}|{dados[1]}|{dados[2]}|{dados[5]})
        return dados
 
         #return (f' Nome: {dados[1]} | Departamento:{dados[2]} | Data:{dados[3]} | PDF:{dados[4]} | Class:{dados[5]} | Descricao:{dados[6]} | data2:{dados[7]}')
         #print(dataHoje)

   
        



    def mostra_semelhante(self,nome):
         self.c.execute("SELECT  id,nome,departamento,data,caixa,temporaridade,tipo,descricao,op1 FROM documento WHERE nome LIKE ?",('%'+ nome + '%', ))
         dados = self.c.fetchall()

		 
         return dados
		
        # for nome in dados:
          #return dados
        #'ID','Nome','Area','Origem','Acondicionamento','Temporaridade','Suporte','Descricao'
          #print(f' Nome: {dados[1]} ')
         #print("nome: ",dados)

    

    def pesquisa_validade(self,op1):
         self.c.execute("SELECT  id,nome,departamento,data,caixa,temporaridade,tipo,descricao,op1 FROM documento WHERE op1 LIKE ?",('%'+ op1 + '%', ))
         dados = self.c.fetchall()

		 
         return dados
         #print(dados)
    

    def search_documents(self,nome):
       
       self.c.execute("SELECT * FROM documento WHERE nome LIKE ?", ( '%' + nome + '%',))
       dados = self.c.fetchone()
       return dados 

	    
        
       #print(f'ID:{dados[0]} | Nome: {dados[1]} ')

    def update_documents(self,nova_valor):
      query = "UPDATE documento SET nome=?, departamento=?, data=?, caixa=?, temporaridade=?,tipo=?, descricao=?,data3=?,data2=?,estado=?,classe=?,pdf=?,op2=? WHERE nome=?"
      self.c.execute(query,nova_valor)
      self.conn.commit()
      #mostrando mensagem de sucesso 

      messagebox.showinfo('sucesso',f'Documento com ID:{nova_valor[0]} foi atualizado!')


    def delete_documents(self,nome):

       self.c.execute("DELETE FROM documento WHERE nome=?",(nome,))
       self.conn.commit()

       #mostrando mensagem que foi deletado
       messagebox.showinfo('sucesso',f'Documento com nome: {nome} foi deletado')


   
   
    def view_data(self):
     self.c.execute("SELECT * FROM documento")
     dados = self.c.fetchall()
    
     
     for i in dados:  
        nome_documento = str(i[1])
        #nome_documento = str(e_nome.get()) 
        date = datetime.datetime.strptime(i[8],'%d/%m/%Y' )
        data2 = date.strftime('%Y-%m-%d') 
        if data2 < dataHoje:
          op1="Expirado"
        else:
          op1= "Vigente"
          
        lista = [op1,nome_documento]
          
        query = "UPDATE documento SET op1=?  WHERE nome=?"
        self.c.execute(query,lista)
        self.conn.commit()  
      
     #print(dados)
     #self.c.execute("SELECT * FROM documento")
      
      
     #dados = self.c.fetchall()
	  
     #for i in dados: 
      # date = datetime.datetime.strptime(i[8],'%d/%m/%Y' )
       #data2 = date.strftime('%Y-%m-%d') 
      
     
       #if data2 < dataHoje:
      #estado="vencido"
	      # nome=i[1]
      #dados = self.c.execute("INSERT INTO documento(op1) VALUES(?)",(estado,)) 
      #self.conn.commit() 
           #print(i[1])
       #else:
      #i[13]='Vigente'
        #print(i[2])
      
    
   
      
	      
	   


#criando uma instancia do sistema de registro


sistema_de_registro = SistemaDeRegistro()

#aluno = sistema_de_registro.search_documents("carlos")

#informações

#estudante = ('helena','diretoria','2023','pdf','0.001','teste de documento')

#sistema_de_registro.register_student(estudante)

todos_documentos = sistema_de_registro.view_data()

#todos_documentos = sistema_de_registro.view_all_documents()

#todos_documentos = sistema_de_registro.pesquisa_validade("Vencido")


#estudante = ('contadeagua','diretoria','2023','pdf',2)
#aluno = sistema_de_registro.update_documents(estudante)
#sistema_de_registro.delete_documents("teste")

#from main import *

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# criação da janela 

janela = Tk()
janela.title("")
janela.geometry("1150x535")
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

style = Style(janela)
style.theme_use("clam")

#criando frames

frame_logo = Frame(janela,width=1200, height=52, bg=co6)
frame_logo.grid(row = 0,column=0,pady=0,padx=0,sticky=NSEW,columnspan = 5)

frame_botoes = Frame(janela,width=100, height=200, bg=co1,relief = RAISED)
frame_botoes.grid(row = 1,column=0,pady=1,padx=0,sticky=NSEW)

frame_detalhes = Frame(janela,width=900, height=100, bg=co1,relief = SOLID)
frame_detalhes.grid(row = 1,column=1,pady=1,padx=10,sticky=NSEW)

frame_tabela = Frame(janela,width=900, height=100, bg=co1,relief = SOLID)
frame_tabela.grid(row = 3,column=0,pady=0,padx=10,sticky=NSEW,columnspan=5)

#colocando o frame logo

global imagem, imagem_string, l_imagem

#app_lg = Image.open('logo.png')
#app_lg = app_lg.resize((40,40))
#app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo,text="  Programa de Registro Documental", width=850, compound=LEFT, anchor=NW, font=('Loboto 15'), bg=co6,fg=co1)

app_logo.place(x=5,y=0)


# criando funçoes para crud


def teste():
	
	print ("teste")

   #função adicionar

def adicionar():
	nome = e_nome.get()
	departamento = c_departamento.get()
	data = e_data.get()
	pdf = a_pdf.get()
	classe = e_classe.get()
	descricao = e_descricao.get()
	vencimento = e_vencimento.get()
	origem = e_data3.get()
	tipo = c_tipo.get()
	estado = c_estado.get()
	temporaridade = c_tempo.get()
	caixa = e_caixa.get()
	op1 = '0'
	pagina = e_pag.get()
    
	list = [nome,departamento,data,caixa,temporaridade,tipo,descricao,vencimento,origem,estado,classe,pdf,op1,pagina]
	#'ID','Nome','Area','Origem','Acondicionamento','Temporaridade','Suporte','Descricao',"data3",data2,estado,classe,pdf

	for i in list :
		if i=='':
			messagebox.showerror("Aviso","Preencha todos os campos!")
			return
		else: ''
        
    #registrando valores
	sistema_de_registro.register_student(list)
    #limpando os campos de entrada	
	e_nome.delete(0,END)
	c_departamento.delete(0,END)
	e_data.delete(0,END)
	a_pdf.delete(0,END)
	e_classe.delete(0,END)
	e_descricao.delete(0,END)
	e_vencimento.delete(0,END)
	e_data3.delete(0,END)
	c_tipo.delete(0,END)
	c_estado.delete(0,END)
	c_tempo.delete(0,END)
	e_caixa.delete(0,END)
	e_pag.delete(0,END)
	#mostrando documentos 
	
    
#função procurar

	
    
    
      
#nome,departamento,data,pdf,classe,descricao,vencimento,origem,tipo,estado,temporaridade,caixa
#nome, departamento, data, caixa, temporaridade,tipo, descricao,data3=?,data2=?,estado=?,classe=?,pdf=?
# função atualizar
	
def atualizar():

	nome_documento = str(e_nome.get()) 
 
	

	nome = e_nome.get()
	departamento = c_departamento.get()
	data = e_data.get()
	caixa = e_caixa.get()
	temporaridade = c_tempo.get()
	tipo = c_tipo.get()
	descricao = e_descricao.get()
	origem = e_data3.get()
	vencimento = e_vencimento.get()
	estado = c_estado.get()
	classe = e_classe.get()
	pagina = e_pag.get()
	pdf = a_pdf.get()
	pagina = e_pag.get()
    
	list = [nome,departamento,data,caixa,temporaridade,tipo,descricao,vencimento,origem,estado,classe,pdf,pagina,nome_documento]
			#[nome,departamento,data,caixa,temporaridade,tipo,descricao,origem,vencimento,estado,classe,pdf]
	for i in list :
		if i=='':
			messagebox.showerror("Aviso","Preencha todos os campos!")
			return

    #registrando valores
		
	sistema_de_registro.update_documents(list)

    #limpando os campos de entrada	

	e_nome.delete(0,END)
	c_departamento.delete(0,END)
	e_data.delete(0,END)
	a_pdf.delete(0,END)
	e_classe.delete(0,END)
	e_descricao.delete(0,END)
	e_vencimento.delete(0,END)
	e_data3.delete(0,END)
	c_tipo.delete(0,END)
	c_estado.delete(0,END)
	c_tempo.delete(0,END)
	e_pag.delete(0,END)
	e_caixa.delete(0,END)
	e_pag.delete(0,END)

	#mostrando documentos:

	mostrar_alunos()

# função deletar
	
def deletar():
	
	nome_documento = str(e_nome.get()) 

	# deletando o aluno

	sistema_de_registro.delete_documents(nome_documento)

    #limpando os campos de entrada	

	e_nome.delete(0,END)
	c_departamento.delete(0,END)
	e_data.delete(0,END)
	a_pdf.delete(0,END)
	e_classe.delete(0,END)
	e_descricao.delete(0,END)
	e_vencimento.delete(0,END)
	e_data3.delete(0,END)
	c_tipo.delete(0,END)
	c_estado.delete(0,END)
	c_tempo.delete(0,END)
    

	e_procurar.delete(0,END)
	e_caixa.delete(0,END)
	mostrar_alunos()

	#mostrando documentos 



    

  #mostrar_alunos()

 




#campos de entrada

l_nome = Label(frame_detalhes,text="Nome:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_nome.place(x=4,y=10)
e_nome = Entry(frame_detalhes,width=30,justify='left', relief='solid')
e_nome.place(x=7,y=40)

l_departamento = Label(frame_detalhes,text="Área:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_departamento.place(x=4,y=70)
c_departamento = ttk.Combobox(frame_detalhes, width=25,font=('Ivy 8 bold'),justify='center')
c_departamento['values'] = ('Obras','Financeiro','Orçamento','Memorial','Comunicação e Marketing','Administração','Licitação','Jurídico','DITEC','Estratégias e diretrizes','DIREX','DISUP','DAF','Pessoal','CDE','Técnica','Auditoria')
c_departamento.place(x=7,y=100)
#l_departamento = Label(frame_detalhes,text="Departamento", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
#l_departamento.place(x=4,y=70)
#e_departamento = Entry(frame_detalhes,width=30,justify='left', relief='solid')
#e_departamento.place(x=7,y=100)

l_data = Label(frame_detalhes,text="Data:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_data.place(x=4,y=130)
e_data = DateEntry(frame_detalhes,width=18,justify='center', background='darkblue',foreground = 'white',borderwidth=2,year=2023,locale='pt_br')
e_data.place(x=7,y=160)

l_pdf = Label(frame_detalhes,text="PDF:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_pdf.place(x=250,y=10)
a_pdf = Entry(frame_detalhes,width="50" ,justify='left', relief='solid')
a_pdf.place(x=250,y=40)

l_classe = Label(frame_detalhes,text="Classe:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_classe.place(x=250,y=70)
e_classe = Entry(frame_detalhes,width="15"  ,justify='left', relief='solid')
e_classe.place(x=250,y=100)

l_descricao = Label(frame_detalhes,text="Descrição:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_descricao.place(x=250,y=130)
e_descricao = Entry(frame_detalhes,width="50",justify='left', relief='solid')
e_descricao.place(x=250,y=160)

l_id = Label(frame_detalhes,text="ID:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_id.place(x=570,y=10)
e_id = Entry(frame_detalhes,width="20",justify='left', relief='solid')
e_id.place(x=570,y=40)

l_vencimento = Label(frame_detalhes,text="Data de Vencimento:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_vencimento.place(x=570,y=70)
e_vencimento = DateEntry(frame_detalhes,width=18,justify='center', background='darkblue',foreground = 'white',borderwidth=2,year=2023,locale='pt_br')
e_vencimento.place(x=570,y=100)

l_data3 = Label(frame_detalhes,text="Data de Origem:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_data3.place(x=400,y=70)
e_data3 = DateEntry(frame_detalhes,width=18,justify='center', background='darkblue',foreground = 'white',borderwidth=2,year=2023,locale='pt_br')
e_data3.place(x=400,y=100)

l_tipo = Label(frame_detalhes,text="Suporte:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_tipo.place(x=570,y=130)
c_tipo = ttk.Combobox(frame_detalhes, width=15,font=('Ivy 8 bold'),justify='center')
c_tipo['values'] = ('Digital','Analógico-digital','Mídia','Analógico-peça')
c_tipo.place(x=570,y=160)

l_estado = Label(frame_detalhes,text="Estado:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_estado.place(x=720,y=130)
c_estado = ttk.Combobox(frame_detalhes, width=15,font=('Ivy 8 bold'),justify='center')
c_estado['values'] = ('Conservado','Danificado')
c_estado.place(x=720,y=160)

l_tempo = Label(frame_detalhes,text="Temporaridade:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_tempo.place(x=720,y=70)
c_tempo = ttk.Combobox(frame_detalhes, width=15,font=('Ivy 8 bold'),justify='center')
c_tempo['values'] = ('Corrente ','Intermediário','Permanente')
c_tempo.place(x=720,y=100)

l_caixa = Label(frame_detalhes,text="Acondicionamento:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_caixa.place(x=720,y=10)
e_caixa = Entry(frame_detalhes,width=15,justify='left', relief='solid')
e_caixa.place(x=720,y=40)

l_pag = Label(frame_detalhes,text="N° de pág:", anchor=NW, font=('Ivy 10'),bg=co1,fg=co4)
l_pag.place(x=840,y=10)
e_pag = Entry(frame_detalhes,width= 7,justify='left', relief='solid')
e_pag.place(x=840,y=40)

#nome=?, departamento=?, data=?, pdf=?, classe=?, descricao=?, data2=?, data3=?,tipo=?,estado=?,temporaridade=?
#tabela

def mostrar_alunos():

	#Expirados = sistema_de_registro.view_data()

	# creating a treeview with dual scrollbars
	list_header = ['ID','Nome','Area','Origem','Acondicionamento','Temporaridade','Suporte','Descricao','Validade']

	

	# view all students
	df_list = sistema_de_registro.view_all_documents()

	tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

	# vertical scrollbar
	vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
	# horizontal scrollbar
	hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

	tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
	tree_aluno.grid(column=0, row=1, sticky='nsew')
	vsb.grid(column=1, row=1, sticky='ns')
	hsb.grid(column=0, row=2, sticky='ew')
	frame_tabela.grid_rowconfigure(0, weight=12)

	hd=["nw","nw","nw","center","center","center","center","center","center","center"]
	h=[60,150,100,100,150,100,100,250,90]
	n=0

	for col in list_header:
		tree_aluno.heading(col, text=col.title(), anchor=NW)
		# adjust the column's width to the header string
		tree_aluno.column(col, width=h[n],anchor=hd[n])

		n+=1

	for item in df_list:
		tree_aluno.insert('', 'end', values=item)




def mostrar_pesquisa(nome_documento):

	# creating a treeview with dual scrollbars
	list_header = ['ID','Nome','Area','Origem','Acondicionamento','Temporaridade','Suporte','Descricao','vencimento']

	

	# view all students
	df_list = sistema_de_registro.mostra_semelhante(nome_documento)

	tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

	# vertical scrollbar

	vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)

	# horizontal scrollbar

	hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)



	tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
	tree_aluno.grid(column=0, row=1, sticky='nsew')
	vsb.grid(column=1, row=1, sticky='ns')
	hsb.grid(column=0, row=2, sticky='ew')
	frame_tabela.grid_rowconfigure(0, weight=12)

	hd=["nw","nw","nw","center","center","center","center","center","center"]
	h=[60,150,100,100,150,100,100,250,90]
	n=0

	for col in list_header:
		tree_aluno.heading(col, text=col.title(), anchor=NW)
		# adjust the column's width to the header string
		tree_aluno.column(col, width=h[n],anchor=hd[n])
		

		n+=1

	for item in df_list:
		tree_aluno.insert('', 'end', values=item)
  
  
  
def procurar():
	#obtendo o valor
	nome_documento = str(e_procurar.get())
	validade_documento = str(c_filtro.get())
	
	#print(nome_documento)
	#obtendo nome

	dados = sistema_de_registro.search_documents(nome_documento)

	#limpando os campos de entrada	
	e_id.delete(0, END)
	e_nome.delete(0,END)
	c_departamento.delete(0,END)
	e_data.delete(0,END)
	a_pdf.delete(0,END) 
	e_classe.delete(0,END)
	e_descricao.delete(0,END)
	e_id.delete(0,END)
	e_vencimento.delete(0,END)
	e_data3.delete(0,END)
	c_tipo.delete(0,END)
	c_estado.delete(0,END)
	c_tempo.delete(0,END)
	e_pag.delete(0,END)
	e_caixa.delete(0,END)
 
    

	#limpando os campos de entrada	
	e_id.insert(END, dados[0])
	e_nome.insert(END,dados[1])
	c_departamento.insert(END,dados[2])
	e_data.insert(END,dados[3])
	e_caixa.insert(END,dados[4])
	c_tempo.insert(END,dados[5])
	c_tipo.insert(END,dados[6])
	e_descricao.insert(END,dados[7])
	a_pdf.insert(END,dados[12])
	e_data3.insert(END,dados[9])
	e_vencimento.insert(END,dados[8])
	c_estado.insert(END,dados[10])
	e_classe.insert(END,dados[11])
	e_pag.insert(END,dados[14])
 
	if nome_documento=='':
                filtro_validade(validade_documento)
    
		
def filtro_validade(validade_documento):

	# creating a treeview with dual scrollbars
	list_header = ['ID','Nome','Area','Origem','Acondicionamento','Temporaridade','Suporte','Descricao','vencimento']

	

	# view all students
	df_list = sistema_de_registro.pesquisa_validade(validade_documento)

	tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

	# vertical scrollbar

	vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)

	# horizontal scrollbar

	hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)



	tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
	tree_aluno.grid(column=0, row=1, sticky='nsew')
	vsb.grid(column=1, row=1, sticky='ns')
	hsb.grid(column=0, row=2, sticky='ew')
	frame_tabela.grid_rowconfigure(0, weight=12)

	hd=["nw","nw","nw","center","center","center","center","center","center"]
	h=[60,150,100,100,150,100,100,250,90]
	n=0

	for col in list_header:
		tree_aluno.heading(col, text=col.title(), anchor=NW)
		# adjust the column's width to the header string
		tree_aluno.column(col, width=h[n],anchor=hd[n])
		

		n+=1

	for item in df_list:
		tree_aluno.insert('', 'end', values=item)



#procurar aluno

frame_procurar = Frame(frame_botoes,width=40, height=55, bg=co1,relief=RAISED)
frame_procurar.grid(row = 0,column=0,pady=0,padx=0,sticky=NSEW)

l_nome = Label(frame_procurar,text="Procurar Documento:", anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_nome.grid(row=0,column=0,pady=3,padx=0,sticky=NSEW)
e_procurar = Entry(frame_procurar,width=5,justify='center',relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1,column=0,pady=10,padx=3,sticky=NSEW)
botao_alterar = Button(frame_procurar,command=procurar,text='Procurar', width=9,anchor=CENTER,overrelief=RIDGE, font=('Ivy 7 bold'),bg=co1,fg=co0)
botao_alterar.grid(row=1,column=1,pady=10,padx=0,sticky=NSEW)


c_filtro = ttk.Combobox(frame_procurar, width=15,font=('Ivy 8 bold'),justify='center')
c_filtro['values'] = ('Expirado','Vigente')
c_filtro.grid(padx=10,pady=0)

#botao adicionar 
app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes,command=adicionar, image=app_img_adicionar,relief=GROOVE,text=' Adicionar',width=100,compound=LEFT,overrelief=RIDGE, font=('Ivy 11'),bg=co1,fg=co0)
app_adicionar.grid(row=1,column=0,pady=5,padx=10,sticky=NSEW)


#botao alterar
app_img_atualizar = Image.open('update.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes,command=atualizar, image=app_img_atualizar,relief=GROOVE,text=' Atualizar',width=100,compound=LEFT,overrelief=RIDGE, font=('Ivy 11'),bg=co1,fg=co0)
app_atualizar.grid(row=2,column=0,pady=5,padx=10,sticky=NSEW)

#botao deletar

app_img_deletar = Image.open('delete.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, command=deletar, image=app_img_deletar,relief=GROOVE,text=' Deletar',width=100,compound=LEFT,overrelief=RIDGE, font=('Ivy 11'),bg=co1,fg=co0)
app_deletar.grid(row=3,column=0,pady=5,padx=10,sticky=NSEW)

#linha separadora 
l_linha = Label(frame_botoes,relief=GROOVE,text='h', width=1,height=123,anchor=NW, font=('Ivy 1'),bg=co0,fg=co0)
l_linha.place(x=212,y=15)





#PRODOC 

#chamar a tabela

mostrar_alunos()

janela.mainloop()
