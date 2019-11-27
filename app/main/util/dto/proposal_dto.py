from flask_restplus import Namespace, fields
import app.main.util.dto.currency_dto as currency_dto
import app.main.util.dto.proposal_zone_dto as proposal_zone_dto
import app.main.util.dto.user_dto as user_dto

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
    'updated': fields.DateTime(description='updated timestamp'),
    'tag': fields.String(description='tag'),
    'zone': fields.Nested(proposal_zone_dto.proposal_zone),
    # 'creator': fields.Nested(user_dto.user_get),
    'currency_unit': fields.Nested(currency_dto.currency),
})
 

proposal_post = api.model('proposal', {
    'zone_id': fields.String(required=True, description='proposal zone id'),
    'title': fields.String(required=True, description='proposal title'),
    'summary': fields.String(description='summary'),
    'detail': fields.String(description='detail'),
    'amount': fields.String(description='proposal amount'),
    'status': fields.String(description='proposal status'),
})


