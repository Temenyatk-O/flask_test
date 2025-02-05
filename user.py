from flask import Blueprint,request

bp=Blueprint("user",__name__,url_prefix="/users")

@bp.route("/",method=["POST"])
def register():
    pass
@bp.route("/login",method=["POST"])
def login():
    pass
