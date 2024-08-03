from flask import Flask
from flask_mqtt import Mqtt
from database.config import db, uri
from models import Leitura
from models.dadosModel import Dados

# Inicialização do MQTT
mqtt_client = Mqtt()

# Lista de tópicos para inscrição
topicos_inscritos = [
    "bflnr/valorUmidade",
    "bflnr/valorTemperatura",
    "bflnr/valorGas",
]

def create_app():
    app = Flask(
        __name__,
        template_folder="./views/",
        static_folder="./static/", 
        root_path="./"
    )

    app.config['SECRET_KEY'] = 'secret-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    db.init_app(app)

    # Configurações do MQTT
    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_KEEPALIVE'] = 5000  # KeepAlive time in seconds

    # Inicializa o MQTT no contexto da aplicação
    mqtt_client.init_app(app)

    # Registra os blueprints
    from controllers.indexController import index_bp
    app.register_blueprint(index_bp, url_prefix='/')

    from controllers.loginController import login_bp
    app.register_blueprint(login_bp, url_prefix='/auth')

    # Define os callbacks do MQTT
    define_mqtt_callbacks(app)

    return app

def define_mqtt_callbacks(app):
    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Broker Conectado com sucesso')
            for topic in topicos_inscritos:
                mqtt_client.subscribe(topic)  # Se inscreve nos tópicos
        else:
            print('Bad connection. Code:', rc)

    @mqtt_client.on_disconnect()
    def handle_disconnect(client, userdata, rc):
        print("Broker desconectado")

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        with app.app_context():
            payload = message.payload.decode("utf-8")  # Decodifica o payload como string
            topic = str(message.topic)
            sensor = ""

            print("******* ", topic, payload)

            if topic == "bflnr/valorUmidade":
                Dados['umidade'] = float(payload)
                sensor = "Umidade"
            elif topic == "bflnr/valorTemperatura":
                Dados['temperatura'] = float(payload)
                sensor = "Temperatura"
            elif topic == "bflnr/valorGas":
                Dados['gas'] = float(payload)
                sensor = "Gás"
            else:
                return  # Ignora tópicos não reconhecidos

            nova_leitura = Leitura(sensor=sensor, medicao=payload)
            db.session.add(nova_leitura)
            db.session.commit()

def send_mqtt_message(topic, message):
    mqtt_client.publish(topic, message)
