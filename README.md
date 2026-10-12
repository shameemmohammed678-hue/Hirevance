# Hirevance – AI-Powered Interview Preparation Platform

Hirevance is a full-stack interview preparation platform designed to help students and job seekers prepare for technical and HR interviews. It provides mock tests, question practice, resume analysis, progress tracking, and an AI-powered assistant in one place.

## 🚀 Live Demo

**Live Application:** https://hirevance.vercel.app/

## ✨ Features

### 🔐 User Authentication
- User registration and login.
- Secure, password-based authentication.
- Personalized access to dashboard features.

### 📝 Mock Tests
- Python, SQL, Java, Web Technologies, and HR mock tests.
- Timed assessments with question navigation.
- Automatic and manual submission.
- Score calculation and result summaries.
- Review answers and explanations.
- Track completed tests and performance.

### 📚 Question Practice
- Practice interview questions.
- Explore questions by category and difficulty.
- Review answers and explanations.

### 📊 Personalized Dashboard
- View completed tests and average scores.
- Track questions practised.
- Visualize weekly and monthly activity.
- Review recent test attempts.
- Access personalized profile information.

### 📄 Resume Management
- Upload and manage resumes.
- View, download, replace, and delete uploaded resumes.
- Extract resume text for analysis.
- Identify skills and important resume sections.
- Generate an ATS-style score and improvement suggestions.

### 🤖 AI-Powered Assistant
- Ask interview preparation questions.
- Receive AI-generated responses.
- Save conversation history for later reference.

### 👤 Profile Management
- Create and update a student profile.
- Upload a profile picture.
- Maintain college, graduation year, and skills information.

### ☁️ Cloud Storage
- Store profile pictures and resumes using Cloudinary.
- Access uploaded files through cloud storage.

### 📱 Responsive Design
- Responsive layouts for desktop, tablet, and mobile devices.
- Dedicated dashboard interface.
- Consistent navigation and styling.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Frontend | HTML, CSS, JavaScript |
| Database | MySQL (TiDB Cloud) |
| Database Connector | PyMySQL |
| AI Integration | OpenRouter API |
| Cloud File Storage | Cloudinary |
| PDF Processing | pypdf |
| Deployment | Vercel |
| Version Control | Git, GitHub |

## 🏗️ Architecture

Hirevance uses Django to handle application logic, authentication, database operations, and server-side rendering.

- **Frontend:** HTML, CSS, and JavaScript provide the user interface.
- **Backend:** Django handles requests, business logic, authentication, and application features.
- **Database:** TiDB Cloud provides MySQL-compatible database storage.
- **AI Integration:** OpenRouter API connects the application to AI models.
- **File Storage:** Cloudinary stores uploaded resumes and profile pictures.
- **Deployment:** Vercel hosts the deployed application.

## ⚙️ Local Installation

### Prerequisites

Ensure you have the following installed:

- Python
- Git
- A MySQL-compatible database, such as MySQL or TiDB Cloud
- A Cloudinary account for cloud file storage
- An OpenRouter API key for the AI assistant

### 1. Clone the Repository

```bash
git clone https://github.com/shameemmohammed678-hue/Hirevance.git
```

### 2. Navigate to the Project Directory

```bash
cd Hirevance
```

If `manage.py` is inside a nested `hirevance` directory, navigate into that directory before running Django commands.

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

Activate it on Windows:

```bash
myenv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the directory containing `manage.py`.

Add the following configuration, replacing the example values with your own credentials:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SECURE_SSL_REDIRECT=False

DB_NAME=your_database_name
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=4000
CA_PATH=isrgrootx1.pem

CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret

OPENROUTER_API_KEY=your_openrouter_api_key
```

**Important:**
- Replace all example values with valid credentials.
- Configure the database connection and TLS certificate according to your database provider.
- Place the required CA certificate at the path specified by `CA_PATH`.
- Keep `.env` out of Git and never commit API keys, database passwords, or Django secrets.
- Use `DEBUG=False` and appropriate production security settings when deploying.

### 6. Apply Database Migrations

If you are setting up a new database:

```bash
python manage.py migrate
```

If you are connecting to an existing database, check its schema and Django migration state before applying migrations.

### 7. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the local application at:

http://127.0.0.1:8000/

## 🔑 Environment Variables

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Django application security |
| `DEBUG` | Controls Django debug mode |
| `ALLOWED_HOSTS` | Specifies permitted hostnames |
| `SECURE_SSL_REDIRECT` | Controls HTTPS redirection |
| `DB_NAME` | Database name |
| `DB_USER` | Database username |
| `DB_PASSWORD` | Database password |
| `DB_HOST` | Database server hostname |
| `DB_PORT` | Database server port |
| `CA_PATH` | Path to the database TLS CA certificate |
| `CLOUDINARY_CLOUD_NAME` | Cloudinary cloud identifier |
| `CLOUDINARY_API_KEY` | Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Cloudinary API secret |
| `OPENROUTER_API_KEY` | OpenRouter API authentication |

## 🚀 Deployment

Hirevance is deployed using Vercel.

The production environment requires the appropriate Django settings, database credentials, TLS certificate configuration, Cloudinary credentials, and OpenRouter API key.

Configure environment variables in the Vercel project settings rather than committing secrets to the repository.

**Live Application:** https://hirevance.vercel.app/

## 🎯 Project Objectives

- Provide an accessible platform for interview preparation.
- Help users assess their technical and HR interview readiness.
- Track mock-test performance and learning progress.
- Help users improve resumes through structured analysis.
- Provide AI-assisted interview preparation.
- Demonstrate full-stack web development, database integration, cloud storage, API integration, and deployment.

## 🔮 Future Improvements

- Expand the interview question database.
- Add more mock-test categories.
- Improve resume analysis and feedback.
- Introduce additional performance analytics.
- Enhance AI-assisted interview practice.
- Add more personalized learning recommendations.

## 👨‍💻 Developer

**Mohammed Shameem**

BSc Computer Science Graduate | Python & Django Full-Stack Developer

GitHub: https://github.com/shameemmohammed678-hue

---

⭐ If you find Hirevance useful, consider starring the repository!
