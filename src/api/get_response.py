import random

from flask import Blueprint, jsonify, request
bp = Blueprint("names", __name__)
from contoso_chat.chat_request import get_response

# route to call sales prompty that takes in a customer id and a question
@bp.route("/get_chat_response")
def get_chat_response():
    customer_id = request.args.get("customer_id")
    question = request.args.get("question")
    chat_history = request.args.get("chat_history")
    result = get_response(customer_id, question, chat_history)
    return jsonify(result)
