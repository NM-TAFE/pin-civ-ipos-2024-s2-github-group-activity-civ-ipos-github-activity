from flask import Flask
from app_logic import AppLogic
import os

template_folder = os.path.join(os.path.dirname(__file__), '../templates')
static_folder = os.path.join(os.path.dirname(__file__), '../static')
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app_logic = AppLogic(app)
print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
