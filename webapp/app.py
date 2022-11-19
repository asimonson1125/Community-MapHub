import flask
from init import app, db
from models import Vendors

@app.route('/')
def homepage():
    return flask.render_template('home.html')

@app.route('/form')
def formpage():
    return flask.render_template('form.html')

@app.route('/submit', methods = ['POST'])
def submission():
    name = flask.request.form['name']
    lat = flask.request.form['latitude']
    lng = flask.request.form['longitude']
    submission = Vendors(name, lat, lng)
    db.session.add(submission)
    db.session.commit()
    return flask.redirect('/')

@app.route('/geojson')
def makeGeoJson():
    vs = Vendors.query.all()
    features = []
    for i in vs:
        props = {}
        props['name'] = i.name
        info = {"geometry": {"coordinates": [i.longitude, i.latitude], "type": "Point"}, "properties": props, "type": "Feature"}
        features.append(info)
    out = {
        "features": features,
        "type": "FeatureCollection"
    }
    return out

@app.errorhandler(Exception)
def page404(e):
    eCode = 500
    message = "An unknown error occured!"
    try:
        app.log_exception(e)
        message = e.description
        eCode = e.code
    finally:
        return flask.render_template('error.html', error=eCode, message=message)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
