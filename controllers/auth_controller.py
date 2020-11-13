from flask import Blueprint
from schemas.UserSchema import user_schema
from models.User import User

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
         return abort(400, description="Email already registered")

    user = User()
    user.email = user_fields["email"]
    user.password = user_fields["password"]

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))