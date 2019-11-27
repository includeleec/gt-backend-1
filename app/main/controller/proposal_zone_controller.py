from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from app.main.service.proposal_service import save_new_proposal_zone, get_all_proposal_zone
from ..util.dto import ProposalZoneDto
from ..service.user_service import get_a_user_by_auth_token

api = ProposalZoneDto.api
proposal_zone = ProposalZoneDto.proposal_zone


@api.route('/')
class ProposalZoneAPI(Resource):
    """
        Proposal Zone Resource
    """
    @api.doc('create new proposal zone')
    # @api.expect(proposal_zone, validate=True)
    @token_required
    def post(self):
        # get the post data
        post_data = request.json
        # get auth token
        auth_token = request.headers.get('Authorization')
        user = get_a_user_by_auth_token(auth_token)

        print(user)
        
        if user:
            post_data['creator_id']=user.id
            return save_new_proposal_zone(data=post_data)

    @api.doc('get all proposal zones')
    @api.marshal_list_with(proposal_zone, envelope='data')
    def get(self):
        return get_all_proposal_zone()



