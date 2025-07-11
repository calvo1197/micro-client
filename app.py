from flask import Flask
from data_source.db_session import engine
from entities.model import Base
from controller.routes import client_bp

app = Flask(__name__)

# create tables
Base.metadata.create_all(engine)

# Registry routes
app.register_blueprint(client_bp)

if __name__ == "__main__":
    app.run(debug=False, port=8082)