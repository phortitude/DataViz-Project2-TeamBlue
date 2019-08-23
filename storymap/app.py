# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'Project-2',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)


class Job(db.Model):
    __tablename__ = 'completenycjobs'

    index = db.Column(db.Integer, primary_key=True)
    businesstitle = db.Column(db.VARCHAR(255))
    newlat = db.Column(db.Float)
    newlong = db.Column(db.Float)
    borough = db.Column(db.VARCHAR(255))
    salaryrangeto = db.Column(db.Float)
    salaryrangefrom = db.Column(db.Float)
    salaryfrequency = db.Column(db.VARCHAR(255))
    jobcatcondensed = db.Column(db.VARCHAR(255))

    def __repr__(self):
        return '<Job %r>' % (self.name)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results

@app.route("/api/jobs")
def jobs():
    results = db.session.query(Job.index, Job.businesstitle, Job.newlat, Job.newlong, Job.borough, Job.salaryrangefrom, Job.salaryrangeto, Job.salaryfrequency, Job.jobcatcondensed).all()

    joblist = []
    for result in results:
        title = result[1]
        lat = result[2]
        lon = result[3]
        borough = result[4]
        salaryFrom = result[5]
        salaryTo = result[6]
        salaryFrequency = result[7]
        jobCat = result[8]

        job_data = {
            "title": title,
            "lat": lat,
            "lon": lon,
            "borough": borough,
            "salaryFrom": salaryFrom,
            "salaryTo": salaryTo,
            "salaryFrequency": salaryFrequency,
            "jobCat": jobCat
        }
        joblist.append(job_data)
    return jsonify(joblist)


if __name__ == "__main__":
    app.run()
