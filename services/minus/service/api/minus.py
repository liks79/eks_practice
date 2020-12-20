"""
    service/api/minus.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    :description: Microservice for plus operation
    :copyright: © 2020 written by Sungshik Jou.
    :license: MIT, see LICENSE for more details.
"""

import socket
from service import db
from flask import jsonify
from flask import current_app as app
from flask import request, Blueprint, make_response
from flask_restx import Api, Resource, fields
from service.schemas import validate_operands
from jsonschema import ValidationError
from werkzeug.exceptions import BadRequest, InternalServerError
from datetime import datetime

minus_blueprint = Blueprint('plus', __name__)
api = Api(minus_blueprint, doc='/swagger/', title='plus',
          description='minus-operation: \n prefix url "/minus" is already exist.', version='0.1')

user_input = api.model('plus_operation', {
    'operand_1': fields.Float,
    'operand_2': fields.Float
})


@api.route('/ping', strict_slashes=False)
class Ping(Resource):
    @api.doc(responses={200: 'pong!'})
    def get(self):
        """Ping api"""
        app.logger.debug('success:ping pong!')
        return make_response({'ok': True, 'Message': 'pong'}, 200)


@api.route('/', strict_slashes=False)
class Run(Resource):
    @api.doc(responses={
        200: 'ok',
        400: 'Invalidate email/password',
        500: 'Internal server error'
    })
    @api.expect(user_input)
    def post(self):
        """ '+',plus api"""
        req_data = request.get_json()
        try:
            validated = validate_operands(req_data)
            input = validated['data']
            app.logger.debug(input)
            result = input['operand_1'] - input['operand_2']

            response = {
                'operand_1': input['operand_1'],
                'operation': '-',
                'operand_2': input['operand_2'],
                'result': result,
                'expression': '{0} - {1} = {2}'.format(
                    input['operand_1'], input['operand_2'], result),
                'from': get_ip_addr(),
                'date': datetime.now()
            }

            app.logger.debug(response)
            return make_response(response, 200)

        except ValidationError as e:
            app.logger.error('ERROR: {0}\n{1}'.format(e.message, req_data))
            raise BadRequest(e.message)


def get_ip_addr():
    return '{0}'.format(socket.gethostname())
