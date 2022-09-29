from flask import Blueprint, render_template, request

result = Blueprint('result', __name__)

@result.route('/', methods=['POST'])
def search_result():
    return render_template('result.html')


