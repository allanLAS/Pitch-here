from flask import render_template
from . import main


@main.app_errorhandler(404)
def four_Ow_four(error):
    """"""
    title = '404 Page'
    return render_template('fourOwfour.html', title=title),404
