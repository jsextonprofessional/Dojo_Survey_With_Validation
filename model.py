from mysqlconnection import connectToMySQL
from flask import flash

class User():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results

    @staticmethod
    def registration_validation(data):
        is_valid = True
    # name - 1-255 characters
        if len(data['name']) < 1:
            flash('All fields required.')
            is_valid = False
    # comment - at least 1 character
        if len(data['comment']) < 1 or len(data['comment']) == 0:
            flash('All fields required.')
            is_valid = False

        return is_valid