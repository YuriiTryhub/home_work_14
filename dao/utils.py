import sqlite3


def connection_to_db(sql):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()
        return result


def get_movies_by_title(title):
    sql = f"""SELECT title, country, release_year, listed_in as genre, description  
                FROM netflix
                WHERE title = '{title}'
                ORDER BY release_year DESC
    """
    result = connection_to_db(sql)
    for item in result:
        return dict(item)


def get_value_in_range(year_1, year_2):
    sql = f"""SELECT title, description 
                FROM netflix
                WHERE release_year BETWEEN {year_1} AND {year_2}
                LIMIT 100
    """
    result = connection_to_db(sql)
    list_result = []
    for item in result:
        list_result.append(dict(item))
    return list_result


def get_sort_by_rating(r):
    sql = f"""SELECT title, rating, description 
                FROM netflix
                WHERE rating in {r}

    """
    result = connection_to_db(sql)
    list_result = []
    for item in result:
        list_result.append(dict(item))
    return list_result

def get_sort_by_genre(genre):
    sql = f"""SELECT title, description, listed_in 
                FROM netflix 
                WHERE listed_in LIKE '%{genre}%'
                ORDER by release_year DESC
                LIMIT 10
"""

    result = connection_to_db(sql)
    list_result = []
    for item in result:
        list_result.append(dict(item))
    return list_result