# app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment_app.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define models
class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    # Add other relevant fields

class JobSeeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    # Add other relevant fields

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    salary = db.Column(db.Float)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'), nullable=False)
    recruiter = db.relationship('Recruiter', backref=db.backref('job_postings', lazy=True))
    # Add other relevant fields

# Create database tables
db.create_all()

# Define API endpoints
@app.route('/recruiters', methods=['GET', 'POST'])
def recruiters():
    if request.method == 'GET':
        recruiters = Recruiter.query.all()
        recruiters_data = [{'id': recruiter.id, 'name': recruiter.name, 'email': recruiter.email, 'phone': recruiter.phone} for recruiter in recruiters]
        return jsonify(recruiters_data)
    elif request.method == 'POST':
        data = request.get_json()
        new_recruiter = Recruiter(name=data['name'], email=data['email'], phone=data['phone'])
        db.session.add(new_recruiter)
        db.session.commit()
        return jsonify({'message': 'Recruiter created successfully'})

# Similar endpoints for job seekers and job postings
# ...

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
