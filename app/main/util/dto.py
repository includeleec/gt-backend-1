from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class ProposalZoneDto:
    api = Namespace('proposal_zone', description='proposal zone related operations')
    proposal_zone = api.model('proposal_zone', {
        'id': fields.String(description='proposal zone id'),
        'name': fields.String(required=True, description='proposal zone name'),
        'title': fields.String(required=True, description='proposal zone title'),
        'summary': fields.String(description='summary'),
        'vote_rule': fields.String(description='vote rule'),
        'vote_addr_weight_json': fields.String(description='this zone vote address relate vote weight'),
        'creator_id': fields.String(description='creator user.id'),
        'created': fields.DateTime(description='created timestamp'),
        'updated': fields.DateTime(description='created timestamp'),
    })


class ProposalDto:
    api = Namespace('proposal', description='proposal related operations')
    proposal = api.model('proposal', {
        'id': fields.String(description='proposal id'),
        'title': fields.String(required=True, description='proposal title'),
        'summary': fields.String(description='summary'),
        'detail': fields.String(description='detail'),
        'amount': fields.String(description='proposal amount'),
        'status': fields.String(description='proposal status'),
        'creator_id': fields.String(description='creator user.id'),
        'created': fields.DateTime(description='created timestamp'),
        'updated': fields.DateTime(description='created timestamp'),
    })