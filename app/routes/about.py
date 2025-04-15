from flask import Blueprint, render_template

about_bp = Blueprint("about", __name__)

@about_bp.route("/about")
def index():
    team = [
        {
            "name": "Xie Wu",
            "title": "Group Coordinator",
            "img": "pics/xie_wu.jpg",
            "linkedin": "https://www.linkedin.com/in/xie-wu-603333228/"
        },
        {
            "name": "Lucy Lin",
            "title": "Team member",
            "img": "pics/lucy_lin.jpg",
            "linkedin": "https://www.linkedin.com/in/lucylin2021/"
        },
        {
            "name": "Vivian Yeh",
            "title": "Team member",
            "img": "pics/vivian_yeh.jpg",
            "linkedin": "https://www.linkedin.com/in/vivian-yeh/"
        },
        {
            "name": "Yidan Ma",
            "title": "Team member",
            "img": "pics/yidan_ma.jpg",
            "linkedin": "https://www.linkedin.com/in/yidan-ma-ucb/"
        },
        {
            "name": "Jiayi Jiang",
            "title": "Team member",
            "img": "pics/jiayi_jiang.jpg",
            "linkedin": "https://www.linkedin.com/in/chloe-jiang-0235b12a6/"
        },
        {
            "name": "Yongkang Zhang",
            "title": "Group Data Liaison",
            "img": "pics/yongkang_zhang.jpg",
            "linkedin": "https://www.linkedin.com/in/yongkang-zhang-62774a340/"
        }
    ]

    return render_template("about.html", team=team)