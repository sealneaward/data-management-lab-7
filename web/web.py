from flask import Flask, render_template, redirect, jsonify, url_for, request, session
from flask_restful import Api
from flask_wtf import Form
from flask_wtf.csrf import CsrfProtect
from wtforms import SelectField
import db.helper as connection


# initalize server
app = Flask(__name__, template_folder='views', static_folder='public')
api = Api(app)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CsrfProtect(app)


# create connection object and get data for teams and players
db = connection.Connection()


@app.route('/', methods=['GET', 'POST'])
def index():
    class SelectTeamForm(Form):
        teams = db.get_teams()
        name = SelectField(coerce=int, choices=teams, default=1610612737L)

    form = SelectTeamForm()

    print(form.errors)

    # handle post request in form
    if form.validate_on_submit():
        session['TEAM_ID'] = form.name.data
        return redirect('/player')

    return render_template("index.html", form=form)


@app.route('/player', methods=['GET','POST'])
def player():
    class SelectPlayerForm(Form):
        team_id = session['TEAM_ID']
        players = db.get_players(team_id)
        name = SelectField(coerce=int, choices=players)

    form = SelectPlayerForm()

    # handle post request in form
    if form.validate_on_submit():
        session['PLAYER_ID'] = form.name.data
        return redirect('/stats')

    return render_template("player.html", form=form)


@app.route('/stats', methods=['POST', 'GET'])
def stats():
    player_id = session['PLAYER_ID']
    stats = db.get_stats(player_id)[0]

    return render_template("stats.html", name=stats[1], blocks=stats[9], drfgm=stats[11], drfga=stats[12], drfgpct=stats[13])

# create simple api that takes in id and response with stats of said player
# ex http://localhost:5000/api/201960
# TODO add query parameters like http://localhost:5000/api?id=201960
@app.route('/api/<id>', methods=['GET','POST'])
def api(id):
    player_id = id
    stats = db.get_stats(player_id)
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')

