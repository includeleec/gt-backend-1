from app.main.exts import db
from app.main.model.mixin import BaseModelMixin, TimestampMixin
from app.main.model.user import User
from app.main.model.currency import Currency
from app.main.model.comment import Comment

class ProposalZone(BaseModelMixin, TimestampMixin, db.Model):
    """
    Proposal Zone
    """
    __tablename__ = 'proposal_zone'

    name = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(100))
    summary = db.Column(db.String(200))
    vote_rule = db.Column(db.Text)
    vote_addr_weight_json = db.Column(db.Text)
    proposals = db.relationship('Proposal',
                                        foreign_keys='Proposal.zone_id',
                                        backref='zone', lazy='dynamic')

    def __repr__(self):
        return "<Proposal Zone '{}'>".format(self.name)


class Proposal(BaseModelMixin, TimestampMixin, db.Model):
    """
    Proposal
    """

    __tablename__ = 'proposal'

    zone_id = db.Column(db.Integer, db.ForeignKey('proposal_zone.id'))
    title = db.Column(db.String(200))
    tag = db.Column(db.String(200))
    amount = db.Column(db.DECIMAL)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'), nullable=True)
    summary = db.Column(db.String(200))
    detail = db.Column(db.Text)
    status = db.Column(db.Integer)

    # 注意，backref 不能跟 talename 重名
    comments = db.relationship('Comment',
                                    foreign_keys='Comment.proposal_id',
                                    backref='link_proposal', lazy='dynamic')

    def __repr__(self):
        return "<Proposal '{}'>".format(self.title)

    def zone(self):
        return ProposalZone.query.filter(zone=self).first()

    def creator(self):
        return User.query.filter(creator=self).first()

    def currency_unit(self):
        return Currency.query.filter(currency_unit=self).first()

