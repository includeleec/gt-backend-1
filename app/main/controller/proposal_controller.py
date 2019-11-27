from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from app.main.service.proposal_service import save_new_proposal_zone, get_all_proposal_zone, save_new_proposal, get_all_proposal, get_a_proposal, get_a_proposal_zone, get_all_currency
import app.main.util.dto.proposal_dto as proposal_dto
import app.main.util.dto.proposal_zone_dto as proposal_zone_dto
import app.main.util.dto.currency_dto as currency_dto

from ..service.user_service import get_a_user_by_auth_token

# proposal zone dto
api_proposal_zone = proposal_zone_dto.api
proposal_zone = proposal_zone_dto.proposal_zone

# proposal zone api
@api_proposal_zone.route('/')
class ProposalZoneAPI(Resource):
    """
        Proposal Zone Resource
    """
    @api_proposal_zone.doc('create new proposal zone')
    @api_proposal_zone.expect(proposal_zone, validate=False)
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

    @api_proposal_zone.doc('get all proposal zones')
    @api_proposal_zone.marshal_list_with(proposal_zone, envelope='data')
    def get(self):
        return get_all_proposal_zone()


# proposal dto
api_proposal = proposal_dto.api
proposal = proposal_dto.proposal
proposal_post = proposal_dto.proposal_post

# proposal api
@api_proposal.route('/')
class ProposalAPI(Resource):
    """
        Proposal Resource
    """
    @api_proposal.doc('create new proposal')
    @api_proposal.expect(proposal_post, validate=True)
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
            return save_new_proposal(data=post_data)

    @api_proposal.doc('get all proposal')
    @api_proposal.marshal_list_with(proposal, envelope='data')
    def get(self):

        return get_all_proposal()  

@api_proposal.route('/<id>')
@api_proposal.param('id', 'Proposal id')
@api_proposal.response(404, 'Proposal not found.')
class ProposalSingleAPI(Resource):
    @api_proposal.doc('get a proposal')
    @api_proposal.marshal_with(proposal, envelope='data')
    def get(self, id):
        """get a proposal given its id"""
        proposal = get_a_proposal(id)
        if not proposal:
            api_proposal.abort(404)
        else:
            return proposal


# currency dto
api_currency = currency_dto.api
currency = currency_dto.currency

# proposal api
@api_currency.route('/')
class CurrencyAPI(Resource):
    """
        Currency Resource
    """
    @api_currency.doc('get all currency')
    @api_currency.marshal_list_with(currency, envelope='data')
    def get(self):
        return get_all_currency()  
