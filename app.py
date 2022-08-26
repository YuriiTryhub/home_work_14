import sqlite3
from flask import Flask, jsonify

from dao.utils import get_movies_by_title, get_value_in_range, get_sort_by_rating, get_sort_by_genre

app = Flask(__name__)


@app.route('/movie/<title>/')
def view_by_title(title):
    result = get_movies_by_title(title)
    return jsonify(result)

@app.route('/movie/<int:year1>/to/<int:year2>/')
def view_in_range(year1, year2):
    result = get_value_in_range(year1, year2)
    return jsonify(result)

@app.route('/rating/family/')
def view_by_children():
    rating = ('G', 'PG', 'PG-13')
    result = get_sort_by_rating(rating)
    return jsonify(result)

@app.route('/rating/children/')
def view_by_family():
    rating = ('G', '')
    result = get_sort_by_rating(rating)
    return jsonify(result)

@app.route('/rating/adult/')
def view_by_adult():
    rating = ('NC-17', 'R')
    result = get_sort_by_rating(rating)
    return jsonify(result)

@app.route('/genre/<genre>/')
def view_by_genre(genre):
    result = get_sort_by_genre(genre)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
