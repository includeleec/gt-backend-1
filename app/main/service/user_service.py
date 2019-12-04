import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main import qiniu_store
from app.main.service.util import save_changes


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def update_user_info(user, data):
    # if(data['avatar']):
    #     user.avatar = data['avatar']

    if(data['nickname']):
        user.nickname = data['nickname']

    if(data['sign']):
        user.sign = data['sign']

    # save to db
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'User info update success',
    }
    return response_object, 200



def update_user_avatar(id, avatar):
    user = User.query.filter_by(id=id).first()
    if user:
        user.avatar = avatar
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'User avatar update success',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User is not exit',
        }
        return response_object, 404

def get_all_users():
    return User.query.all()


def get_a_user(id):
    user = User.query.filter_by(id=id).first()
    return user

def get_a_user_by_auth_token(auth_token):
    resp = User.decode_auth_token(auth_token)
    if not isinstance(resp, str):
        return User.query.filter_by(id=resp).first()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


