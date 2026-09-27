from pypdf import PdfReader
import re


def extract_pdf_text(file):

    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text+"\n"

    return text





def detect_section(text):

    section_name = [
        'summary',
        'education',
         'technical skills',
         'soft skills',
         'internship',
         'projects',
         'experience',
         'achievements',
         'certifications',
         'activities',

    ]

    text_lower = text.lower()

    founded_section = []

    for section in section_name:
        if section in text_lower:
            founded_section.append(section.title())
    
    return founded_section


def detect_skills(text):

    skills_name = [
        'python',
        'ai',
        'java',
        'html',
        'javascript',
        'css',
        'react',
        'springboot',
        'django',
        'angular'
    ]

    text_lower = text.lower()

    founded_skills = []

    for skill in skills_name:
        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, text_lower):
            founded_skills.append(skill.title())

    return founded_skills


def analyze_resume(file):

    text = extract_pdf_text(file)

    sections = detect_section(text)

    skills = detect_skills(text)

    score = calculate_score(sections,skills)

    suggestions = generate_suggestions(sections,skills) 

    return {"text":text,"sections":sections,"skills":skills,"score":score,"suggestions":suggestions} 


def calculate_score(sections,skills):

    score = 0
    if sections:
        score+=10

    if 'Summary' in sections:
        score+=10

    if 'Education' in sections:
        score+=10

    if 'Technical Skills' in sections or 'Soft Skills' in sections:
        score+=10

    if 'Projects' in sections:
        score+=10

    if 'Experience' in sections or 'Internship' in sections:
        score+=10

    if 'Achievements' in sections:
        score+=10

    if 'Certifications' in sections:
        score+=10

    if len(skills)>=5:
        score+=20

    return score


def generate_suggestions(sections,skills):

    suggestions = []

    if 'Summary' not in sections:
        suggestions.append("Summary section is missing")


    if 'Education' not in sections:
        suggestions.append("Add Education details")

    if 'Projects' not in sections:
        suggestions.append('Add projects that showcase your skills')

    if 'Experience' not in sections and 'Internship' not in sections:
        suggestions.append("Add Your Experience to increase a score ")


    if 'Achievements' not in sections:
        suggestions.append("Add the Achievements that make feel you proud ")

    if len(skills) < 5:
        suggestions.append("Add more relevant technical skills")


    if not suggestions:
        suggestions.append(
            "Your resume contains all the important sections. "
            "Keep your resume updated and tailor it to the job description."
    )


    return suggestions