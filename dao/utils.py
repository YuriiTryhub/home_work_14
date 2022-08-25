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


print(get_movies_by_title('#Selfie 69'))