from flask_restplus import Namespace, fields
import app.main.util.dto.proposal_dto as proposal_dto


api = Namespace('user', description='user related operations')
user = api.model('user', {
    'email': fields.String(required=True, description='user email address'),
    'username': fields.String(required=True, description='user username'),
    'password': fields.String(required=True, description='user password'),
    'public_id': fields.String(description='user Identifier')
})

proposals_created_fields = fields.List(fields.Nested(proposal_dto.proposal_created_item))

user_get = api.model('user', {
    'email': fields.String(required=True, description='user email address'),
    'username': fields.String(required=True, description='user username'),
    'avatar': fields.String(description='user avatar'),
    'public_id': fields.String(description='user public Identifier'),
    'id': fields.String(description='user Identifier'),
    'proposals_created': proposals_created_fields
})

user_get_all = api.model('user', {
    'email': fields.String(required=True, description='user email address'),
    'username': fields.String(required=True, description='user username'),
    'avatar': fields.String(description='user avatar'),
    'public_id': fields.String(description='user public Identifier'),
    'id': fields.String(description='user Identifier'),
})


