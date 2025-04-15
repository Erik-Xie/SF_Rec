from flask import Blueprint, render_template

feature_bp = Blueprint("feature", __name__)

@feature_bp.route("/feature")
def index():
    return render_template("feature.html")