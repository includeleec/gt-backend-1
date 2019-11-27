import uuid
import datetime
from app.main import db
from app.main.model.user import User
from app.main.model.proposal import ProposalZone, Proposal


# def detect_user_exist(func):
#     def wrapper(data):
#         user = User.query.filter_by(id=data['creator_id']).first()
#         if not user:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'ceator_id is not exists.',
#             }
#             return response_object, 404
#     return wrapper

# @detect_user_exist
def save_new_proposal_zone(data):

    proposal_zone = ProposalZone.query.filter_by(name=data['name']).first()
    if not proposal_zone:
        new_proposal_zone = ProposalZone(
            name=data['name'],
            title=data['title'],
            summary=data['summary'],
            vote_rule=data['vote_rule'],
            vote_addr_weight_json=data['vote_addr_weight_json'],
            creator_id=data['creator_id'],
        )
        save_changes(new_proposal_zone)
        response_object = {
            'status': 'success',
            'message': 'Successfully create a new proposal zone.',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Proposal zone name already exists.',
        }
        return response_object, 409

# @detect_user_exist
def save_new_proposal(data):

    proposal_zone = ProposalZone.query.filter_by(id=data['zone_id']).first()
    if not proposal_zone:
        response_object = {
            'status': 'fail',
            'message': 'relate zone_id is not exists.',
        }
        return response_object, 404

    try:
        new_proposal = Proposal(
            zone_id=data['zone_id'],
            title=data['title'],
            amount=data['amount'],
            summary=data['summary'],
            detail=data['detail'],
            creator_id=data['creator_id'],
        )

        save_changes(new_proposal)
        response_object = {
            'status': 'success',
            'message': 'Successfully create a new proposal.',
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'some error'
        }
        return response_object, 401


def get_all_proposal_zone():
    return ProposalZone.query.all()

def get_all_proposal():
    return Proposal.query.all()

def get_a_proposal_zone(id):
    return ProposalZone.query.filter_by(id=id).first()

def get_a_proposal(id):
    return Proposal.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

