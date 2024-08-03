from flask import Blueprint, render_template, request, redirect, url_for, session
from database.config import db
from models import Users

login_bp = Blueprint("login", __name__)
@login_bp.route('/')
def login_index():
  return render_template("pages/login/login.html")

@login_bp.route('/postLogin', methods=['POST'])
def postLogin():
    
    email = request.form['emailLogin']
    senha = request.form['senhaLogin']

    autenticado = False

    user = Users.query.filter_by(email=email).first()

    if user:
      if user.senha == senha:
        session['email'] = user.email
        session['nome'] = user.name
        session['admin'] = user.admin
        session['operador'] = user.operador
        autenticado = True
         
    if autenticado:
      return redirect(url_for("index.index"))
    else:
      return render_template("pages/login/login.html", error='ERRO NA AUTENTICAÇÃO')

@login_bp.route('/criaUsuario', methods=['POST'])
def criarUsuario():

  email = request.form['emailAddUser']
  nome = request.form['nomeAddUser']
  senha = request.form['senhaAddUser']
  admin = request.form['adminAddUser'] == 'True'
  operador = request.form['operadorAddUser'] == 'True'

  novo_user = Users(name=nome, email=email, senha=senha, admin=admin, operador=operador)
  db.session.add(novo_user)
  db.session.commit()

  return redirect(url_for('index.usuarios'))

@login_bp.route('/editarUsuario', methods=['POST'])
def editarUsuario():

  email = request.form['emailEditarUser']
  nome = request.form['nomeEditarUser']
  senha = request.form['senhaEditarUser']
  admin = request.form['adminEditarUser'] == 'True'
  operador = request.form['operadorEditarUser'] == 'True'
  _id = request.form['idEditarUser']

  user = Users.query.get(_id)

  if user:
      user.name = nome
      user.senha = senha
      user.email = email
      user.admin = admin
      user.operador = operador
      db.session.commit()

  return redirect(url_for('index.usuarios'))

@login_bp.route('/removerUsuario/<_id>')
def removerUsuario(_id):

  user = Users.query.get(_id)
  if user and not user.admin:
    db.session.delete(user)
    db.session.commit()

  return redirect(url_for('index.usuarios'))


@login_bp.route('/logout')
def logout():
  
  session.clear()
  return redirect(url_for('login.login_index')) 