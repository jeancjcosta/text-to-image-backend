from flask import Flask
from flask_restx import Api


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0',
            title='Text To Image',
            description='An app to get images from input text.',
            doc='/docs'
        )

    def run(self) -> None:
        self.app.run(debug=True, host="0.0.0.0", port=8080)


server = Server()