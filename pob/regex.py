import re


def validate_username(username):
    return re.fullmatch("[A-ZÆØÅ][A-ZÆØÅa-zæøå0-9_-]*", username) != None


def validate_password(password):
    return re.fullmatch(
        "[^ ]*[0-9][^ ]*[^0-9A-ZÆØÅa-zæøå ][^ ]*"
        "|[^ ]*[^0-9A-ZÆØÅa-zæøå ][^ ]*[0-9][^ ]*",
        password) != None
