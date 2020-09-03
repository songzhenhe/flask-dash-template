# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint("dashboard", __name__, static_folder="../static")



@blueprint.route("/dash/app1")
@login_required
def dashapp1():
    return render_template("dashboard/app1.html")

@blueprint.route("/dash/app2")
@login_required
def dashapp2():
    return render_template("dashboard/app2.html")

@blueprint.route("/dash/app3")
@login_required
def dashapp3():
    return render_template("dashboard/app3.html")