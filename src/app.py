from flask import Flask
from app_logic import AppLogic
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))
app_logic = AppLogic(app)
print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
