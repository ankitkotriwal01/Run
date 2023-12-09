# models.py
from app import db

class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    company_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    job_postings = db.relationship('JobPosting', backref='recruiter', lazy=True)

    def __repr__(self):
        return f"Recruiter(id={self.id}, name={self.first_name} {self.last_name}, email={self.email}, company={self.company_name})"

class JobSeeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    skills = db.Column(db.String(200))
    bio = db.Column(db.Text)
    job_matches = db.relationship('JobPosting', secondary='job_match', backref='job_seekers', lazy='dynamic')

    def __repr__(self):
        return f"JobSeeker(id={self.id}, name={self.first_name} {self.last_name}, email={self.email}, skills={self.skills})"

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    salary = db.Column(db.Float)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'), nullable=False)
    applications = db.relationship('JobApplication', backref='job_posting', lazy=True)

    def __repr__(self):
        return f"JobPosting(id={self.id}, title={self.title}, location={self.location}, salary={self.salary})"

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_seeker_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'), nullable=False)
    job_posting_id = db.Column(db.Integer, db.ForeignKey('job_posting.id'), nullable=False)
    status = db.Column(db.String(20))  # 'applied', 'accepted', 'rejected', etc.

    def __repr__(self):
        return f"JobApplication(id={self.id}, status={self.status})"
