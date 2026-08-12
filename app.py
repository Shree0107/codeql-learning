from flask import request

def search():
    username = request.args["username"]

    query = "SELECT * FROM users WHERE name = '" + username + "'"

    database.execute(query)