from flask import Flask, render_template, send_file, request
from weasyprint import HTML

app = Flask(__name__)

def extract_data(form, prefix, fields):
    data = {}
    for field in fields:
        data[field] = form.get(f'{prefix}_{field}')
    return data

def extract_list_data(form, prefix, fields):
    data_list = []
    i = 1
    while True:
        data = extract_data(form, f'{prefix}_{i}', fields)
        if not any(data.values()):
            break
        data_list.append(data)
        i += 1
    return data_list

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/resume')
def resume_tab():
    return render_template('resume_form.html')



@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    full_name = request.form.get('full_name')
    phone_number = request.form.get('phone_number')
    email_address = request.form.get('email_address')
    linkedin_profile = request.form.get('linkedin_profile')
    professional_website = request.form.get('professional_website')
    summary = request.form.get('summary')
    experiences = request.form.get('experiences')
    educations = request.form.get('educations')
    skills = request.form.getlist('skills')
    certifications = request.form.get('certifications')
    projects = request.form.get('projects')
    achievements_and_awards = request.form.get('achievements_and_awards')
    languages = request.form.get('languages')
    volunteer_work = request.form.get('volunteer_work')
    professional_memberships = request.form.getlist('professional_memberships')
    hobbies_and_interests = request.form.get('hobbies_and_interests')

    resume_template = render_template('resume_template.html',
                                      full_name=full_name,
                                      phone_number=phone_number,
                                      email_address=email_address,
                                      linkedin_profile=linkedin_profile,
                                      professional_website=professional_website,
                                      summary=summary,
                                      experiences=experiences,
                                      educations=educations,
                                      skills=skills,
                                      certifications=certifications,
                                      projects=projects,
                                      achievements_and_awards=achievements_and_awards,
                                      languages=languages,
                                      volunteer_work=volunteer_work,
                                      professional_memberships=professional_memberships,
                                      hobbies_and_interests=hobbies_and_interests)

    return render_template('result.html', resume=resume_template)

@app.route('/generate_cover_letter', methods=['POST'])
def generate_cover_letter():

    # Extract data for cover letter template
    your_full_name = request.form.get('your_full_name')
    your_address = request.form.get('your_address')
    city_state_zip = request.form.get('city_state_zip')
    your_email_address = request.form.get('your_email_address')
    your_phone_number = request.form.get('your_phone_number')
    current_date = request.form.get('current_date')
    hiring_manager_name = request.form.get('hiring_manager_name')
    company_address = request.form.get('company_address')
    position_applying_for = request.form.get('position_applying_for')
    company_name = request.form.get('company_name')
    relevant_qualifications = request.form.get('relevant_qualifications')
    specific_achievement = request.form.get('specific_achievement')
    previous_company = request.form.get('previous_company')
    relevant_skills = request.form.get('relevant_skills')
    specific_company_values = request.form.get('specific_company_values')
    recent_company_accomplishments = request.form.get('recent_company_accomplishments')
    additional_company_insights = request.form.get('additional_company_insights')

    # Render cover letter template
    cover_letter_template = render_template('cover_letter_template.html',
                                            your_full_name=your_full_name,
                                            your_address=your_address,
                                            city_state_zip=city_state_zip,
                                            your_email_address=your_email_address,
                                            your_phone_number=your_phone_number,
                                            current_date=current_date,
                                            hiring_manager_name=hiring_manager_name,
                                            company_address=company_address,
                                            position_applying_for=position_applying_for,
                                            company_name=company_name,
                                            relevant_qualifications=relevant_qualifications,
                                            specific_achievement=specific_achievement,
                                            previous_company=previous_company,
                                            relevant_skills=relevant_skills,
                                            specific_company_values=specific_company_values,
                                            recent_company_accomplishments=recent_company_accomplishments,
                                            additional_company_insights=additional_company_insights)

    # Save or display generated documents as needed

    return render_template('result.html',  cover_letter=cover_letter_template)

# Add routes for cover letter and template selection as needed

if __name__ == '__main__':
    app.run(debug=True)
