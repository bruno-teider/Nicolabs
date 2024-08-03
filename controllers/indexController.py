from flask import Blueprint, render_template, session, redirect, url_for, request
from database.config import db
from models import *
from controllers.appController import send_mqtt_message

index_bp = Blueprint("index", __name__)
@index_bp.route('/')
def index():

  if 'email' in session:
    led = Atuador.query.filter_by(apelido="LED").first()
    buzzer = Atuador.query.filter_by(apelido="Buzzer").first()
    
    return render_template("pages/home/index.html", temperatura=Dados['temperatura'], umidade=Dados['umidade'], gas=Dados['gas'], led=led, buzzer=buzzer)
  else:
    return redirect(url_for('login.login_index'))
  
# SENSORES ------------------------------------------------------------------------------------------------------------
@index_bp.route('/sensores')
def sensores():

  sensores = Sensor.query.all()
  total = len(sensores)

  sensores_ativos = Sensor.query.filter_by(ativo=True).all()
  totalAtivos = len(sensores_ativos)
  
  if session['admin'] != True and session['operador'] != True:
    return redirect(url_for('index.index'))
  else:
    return render_template("pages/sensores/sensores.html", sensores=sensores, total=total, totalAtivos=totalAtivos)

@index_bp.route('/criaSensor', methods=['POST'])
def criarSensor():

  nome = request.form['nomeAddSensor']
  medicao = request.form['medicaoAddSensor']
  ativo = request.form['ativoAddSensor'] == 'True'

  novo_sensor = Sensor(apelido=nome, medicao=medicao, ativo=ativo)
  db.session.add(novo_sensor)
  db.session.commit()

  return redirect(url_for('index.sensores'))

@index_bp.route('/editarSensor', methods=['POST'])
def editarSensor():

  nome = request.form['nomeEditarSensor']
  medicao = request.form['medicaoEditarSensor']
  ativo = request.form['ativoEditarSensor'] == 'True'
  _idSensor = request.form['idEditarSensor']

  sensor = Sensor.query.get(_idSensor)

  if sensor:
      sensor.apelido = nome
      sensor.medicao = medicao
      sensor.ativo = ativo
      db.session.commit()

  return redirect(url_for('index.sensores'))

@index_bp.route('/removerSensor/<_id>')
def removerSensor(_id):

  sensor = Sensor.query.get(_id)
  if sensor:
      db.session.delete(sensor)
      db.session.commit()
  
  return redirect(url_for('index.sensores'))

# ATUADORES --------------------------------------------------------------------------------------------------------------
@index_bp.route('/atuadores')
def atuadores():

  atuadores = Atuador.query.all()
  total = len(atuadores)

  atuadores_ativos = Atuador.query.filter_by(ativo=True).all()
  totalAtivos = len(atuadores_ativos)

  if session['admin'] != True and session['operador'] != True:
    return redirect(url_for('index.index'))
  else:
    return render_template("pages/atuadores/atuadores.html", atuadores=atuadores, total=total, totalAtivos=totalAtivos)
  
  

@index_bp.route('/criaAtuador', methods=['POST'])
def criarAtuador():

  nome = request.form['nomeAddAtuador']
  ativo = request.form['ativoAddAtuador'] == 'True'
  tipo = request.form['tipoAddAtuador']

  novo_atuador = Atuador(apelido=nome, ativo=ativo, tipo=tipo)
  db.session.add(novo_atuador)
  db.session.commit()

  return redirect(url_for('index.atuadores'))

@index_bp.route('/editarAtuador', methods=['POST'])
def editarAtuador():

  nome = request.form['nomeEditarAtuador']
  ativo = request.form['ativoEditarAtuador'] == 'True'
  _idAtuador = request.form['idEditarAtuador']

  atuador = Atuador.query.get(_idAtuador)

  if atuador:
      atuador.apelido = nome
      atuador.ativo = ativo
      db.session.commit()

  return redirect(url_for('index.atuadores'))

@index_bp.route('/removerAtuador/<_id>')
def removerAtuador(_id):

  atuador = Atuador.query.get(_id)
  if atuador:
    db.session.delete(atuador)
    db.session.commit()

  return redirect(url_for('index.atuadores'))

# USUÁRIOS --------------------------------------------------------------------------------------------------------------
@index_bp.route('/usuarios')
def usuarios():

  users = Users.query.all()
  total = len(users)

  users_admins = Users.query.filter_by(admin=True).all()
  totalAdmins = len(users_admins)
  
  if session['admin'] != True:
    return redirect(url_for('index.index'))
  else:
    return render_template("pages/usuarios/usuarios.html", users=users, total=total, totalAdmins=totalAdmins)


# LEITURAS --------------------------------------------------------------------------------------------------------------
@index_bp.route('/leituras')
def leituras():

  leituras = Leitura.query.all()

  # Formata a data para exibição
  for leitura in leituras:
      leitura.data = leitura.data.strftime("%H:%M %d/%m/%Y")
  
  if session['admin'] != True:
    return redirect(url_for('index.index'))
  else:
    return render_template("pages/leituras/leituras.html", leituras=leituras)

# CONTROLES REMOTOS ------------------------------------------------------------------------------------------------------
@index_bp.route('/acionaLed')
def acionaLed():

  valor = '0'
  atuador = Atuador.query.filter_by(apelido="LED").first()
  atuador.ativo = atuador.ativo != True # INVERTE O VALOR DO SENSOR
  db.session.commit()
  
  if atuador.ativo:
    valor = '1'
  else:
    valor = '0'
  
  send_mqtt_message('bflnr/valorLed', valor)

  return redirect(url_for('index.index'))

@index_bp.route('/acionaBuzzer')
def acionaBuzzer():

  send_mqtt_message('bflnr/valorBuzzer', '1')

  return '', 204

