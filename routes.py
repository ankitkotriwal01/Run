# routes.py
from app import app, db
from flask import jsonify, request
from models import Recruiter, JobSeeker, JobPosting, JobApplication

# Recruiters Endpoints
@app.route('/recruiters', methods=['GET', 'POST'])
def recruiters():
    if request.method == 'GET':
        recruiters = Recruiter.query.all()
        recruiters_data = [{'id': recruiter.id, 'name': f"{recruiter.first_name} {recruiter.last_name}", 'email': recruiter.email, 'phone': recruiter.phone, 'company': recruiter.company_name, 'bio': recruiter.bio} for recruiter in recruiters]
        return jsonify(recruiters_data)
    elif request.method == 'POST':
        data = request.get_json()
        new_recruiter = Recruiter(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], phone=data['phone'], company_name=data['company_name'], bio=data['bio'])
        db.session.add(new_recruiter)
        db.session.commit()
        return jsonify({'message': 'Recruiter created successfully'})

# Job Seekers Endpoints
@app.route('/job_seekers', methods=['GET', 'POST'])
def job_seekers():
    if request.method == 'GET':
        job_seekers = JobSeeker.query.all()
        job_seekers_data = [{'id': job_seeker.id, 'name': f"{job_seeker.first_name} {job_seeker.last_name}", 'email': job_seeker.email, 'phone': job_seeker.phone, 'skills': job_seeker.skills, 'bio': job_seeker.bio} for job_seeker in job_seekers]
        return jsonify(job_seekers_data)
    elif request.method == 'POST':
        data = request.get_json()
        new_job_seeker = JobSeeker(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], phone=data['phone'], skills=data['skills'], bio=data['bio'])
        db.session.add(new_job_seeker)
        db.session.commit()
        return jsonify({'message': 'Job Seeker created successfully'})

# Job Postings Endpoints
@app.route('/job_postings', methods=['GET', 'POST'])
def job_postings():
    if request.method == 'GET':
        job_postings = JobPosting.query.all()
        job_postings_data = [{'id': job_posting.id, 'title': job_posting.title, 'description': job_posting.description, 'location': job_posting.location, 'salary': job_posting.salary, 'recruiter': job_posting.recruiter.first_name} for job_posting in job_postings]
        return jsonify(job_postings_data)
    elif request.method == 'POST':
        data = request.get_json()
        recruiter_id = data.get('recruiter_id')  # Assume the recruiter_id is provided in the request
        recruiter = Recruiter.query.get(recruiter_id)
        if not recruiter:
            return jsonify({'error': 'Recruiter not found'})
        new_job_posting = JobPosting(title=data['title'], description=data['description'], location=data['location'], salary=data['salary'], recruiter=recruiter)
        db.session.add(new_job_posting)
        db.session.commit()
        return jsonify({'message': 'Job Posting created successfully'})
