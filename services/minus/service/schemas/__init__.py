"""
    service/schemas/__init__.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: 12/19/20
    :description: Microservice for plus operation
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

operands_schema = {
    "type": "object",
    "properties": {
        "operand_1": {
            "type": "number"
        },
        "operand_2": {
            "type": "number"
        }
    },
    "required": ["operand_1", "operand_2"],
    "additionalProperties": False
}


def validate_operands(data):
    """
    Validate request json parameters
    :param data:
    :return:
    """
    try:
        validate(data, operands_schema)
        return {'ok': True, 'data': data}
    except ValidationError as e:
        raise e
    except SchemaError as e:
        raise e
    except Exception as e:
        raise e
