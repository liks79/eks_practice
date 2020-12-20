"""
    service/database/models.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    :description: Microservice for plus operation
    :copyright: © 2020 written by Sungshik Jou.
    :license: MIT, see LICENSE for more details.
"""


from sqlalchemy import DateTime, Integer, String
from datetime import datetime
from service import db


class DivideResult(db.Model):
    """
    Database Model class for plus_result table
    """
    __tablename__ = 'divide_result'

    id = db.Column(Integer, primary_key=True)
    operand_1 = db.Column(Integer)
    operand_2 = db.Column(Integer)
    operator = db.Column(String(1), default='/')
    result = db.Column(Integer)
    date = db.Column(DateTime, unique=False, default=datetime)

    def __init__(self, operand_1, operand_2):
        self.operand_1 = operand_1
        self.operand_2 = operand_2

    def __repr__(self):
        return '<%r %r %r>' % (self.__tablename__, self.operand_1, self.operand_2)

    def to_json(self):
        return {
            'id': self.id,
            'operand_1': self.operand_1,
            'operand_2': self.operand_2
        }
