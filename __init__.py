from crypt import methods
from operator import contains
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbsistema'

mysql = MySQL(app)

#Cadastros CLIENTES#
@app.route('/addcliente')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clientes")
    data = cur.fetchall()
    cur.close()

    return render_template('addcliente.html', clientes=data)



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Dados inseridos com sucesso")
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        cep = request.form['cep']
        cidade = request.form['cidade']
        bairro = request.form['bairro']
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clientes (nome, telefone, email, cep, cidade, bairro, rua, numero, complemento) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s)", (nome, telefone, email, cep, cidade, bairro, rua, numero, complemento))
        mysql.connection.commit()
        return redirect(url_for('index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("O registro deletado com sucesso!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM clientes WHERE id=%s",(id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))



@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        cep = request.form['cep']
        cidade = request.form['cidade']
        bairro = request.form['bairro']
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE clientes SET nome=%s, telefone=%s, email=%s, cep=%s, cidade=%s, bairro=%s, rua=%s, numero=%s, complemento=%s
               WHERE id=%s """, (id_data, nome, telefone, email, cep, cidade, bairro, rua, numero, complemento))
        flash("Dados atualizados com sucesso")
        mysql.connection.commit()
        return redirect(url_for('index'))

# ----------------FIM CLIENTES---------------------------------#

#Cadastros PRODUTOS

# -------------------------------------------------#
@app.route('/addproduto')
def cadproduto():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos")
    data = cur.fetchall()
    cur.close()


    return render_template('addproduto.html', produtos=data )



@app.route('/addprd', methods = ['POST'])
def addprd():

    if request.method == "POST":
        flash("Dados inseridos com sucesso")
        produto = request.form['produto']
        valor = request.form['valor']
        tipo = request.form['tipo']
        info = request.form['info']
        
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO produtos (produto, valor, tipo, info) VALUES (%s, %s, %s,%s)", (produto, valor, tipo, info,))
        mysql.connection.commit()
        return redirect(url_for('cadproduto'))




@app.route('/deleteprd/<string:id_data>', methods = ['GET'])
def deleteprd(id_data):
    flash("O registro deletado com sucesso!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM produtos WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('cadproduto'))





@app.route('/updateprd',methods=['POST','GET'])
def updateprd():

    if request.method == 'POST':
        id_data = request.form['id']
        produto = request.form['produto']
        valor = request.form['valor']
        tipo = request.form['tipo']
        info = request.form['info']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE produtos
               SET produto=%s, valor=%s, tipo=%s, info=%s
               WHERE id=%s
            """, (id_data, produto, valor, tipo, info))
        flash("Dados atualizados com sucesso")
        mysql.connection.commit()
        return redirect(url_for('cadproduto'))

# ------------------FIM PRODUTOS-------------------------------#



#-------------------HISTORICO VENDA----------------------------#
#@app.route('/registrovenda/<string:id_data>', methods=['GET'])
#def registrovenda(id_data):
 #   cur = mysql.connection.cursor()
  #  cur.execute("SELECT * FROM %s compra WHERE %s id_cliente = id=%s", (id_data,))
   # data = cur.fetchall()
   
    #return render_template('registrovenda.html', compra=data)
    
        

if __name__ == "__main__":
  app.run(debug=True)