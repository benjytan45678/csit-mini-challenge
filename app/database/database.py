from decouple import config
from flask import current_app, g
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy


def get_db():
    """Sets or returns the database instance.

    Returns:
        db: Database object
    """
    # g is the global context in Flask
    db = getattr(g, "_database", None)
    if db is None:
        # set it as an attribute under g if it hasn't been set
        db = g._database = PyMongo(
            current_app,
            uri=config("MONGO_URI"),
        ).db
    return db


# makes it so that we can simply refer to the global db instance
db = LocalProxy(get_db)
