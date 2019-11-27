from .. import db
from app.main.model.mixin import BaseModelMixin, TimestampMixin



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

    def __repr__(self):
        return "<Proposal Zone '{}'>".format(self.name)


class Proposal(BaseModelMixin, TimestampMixin, db.Model):
    """
    Proposal
    """

    __tablename__ = 'proposal'

    zone_id = db.Column(db.Integer, db.ForeignKey('proposal_zone.id'))
    title = db.Column(db.String(200))
    amount = db.Column(db.DECIMAL)
    summary = db.Column(db.String(200))
    detail = db.Column(db.Text)
    status = db.Column(db.Integer)

    def __repr__(self):
        return "<Proposal '{}'>".format(self.title)