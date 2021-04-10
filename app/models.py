# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     age = db.Column(db.Integer())
#     category = db.Column(db.String())
#
#     def __init__(self, name, author, published):
#         self.name = name
#         self.age = author
#         self.category = published
#
#     def __repr__(self):
#         return '<id {}>'.format(self.id)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'author': self.age,
#             'published': self.category
#         }