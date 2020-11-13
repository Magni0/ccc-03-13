from flask import Blueprint
from schemas.UserSchema import user_schema
from models.User import User

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    return "working"