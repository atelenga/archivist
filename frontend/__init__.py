from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "archivist"}
app.config["SECRET_KEY"] = "K33pTh1sS3cr3t"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from frontend.views import issues
    app.register_blueprint(issues)


register_blueprints(app)

if __name__ == '__main__':
    app.run()
