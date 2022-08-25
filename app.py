import sqlite3
from flask import Flask, jsonify

from dao.utils import get_movies_by_title

app = Flask(__name__)


@app.route('/movie/<title>/')
def view_by_title(title):
    result = get_movies_by_title(title)
    return jsonify(result)

@app.route('/movie/<int:year1>/to/<int:year2>')
def view_in_range(year1, year2):
    result = get_value_in_range(year1, year2)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
