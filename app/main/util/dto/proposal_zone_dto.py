from flask_restplus import Namespace, fields

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