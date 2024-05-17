from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import get_chat_response
    # import sales prompty

    app.register_blueprint(get_chat_response.bp)


    return app
