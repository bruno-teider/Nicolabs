from controllers.appController import create_app
from utils.create_db import create_db

if __name__ == "__main__":
    app = create_app()
    #create_db(app)
    app.run(debug=True)