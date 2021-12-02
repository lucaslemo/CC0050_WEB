FROM python:3.9
RUN apt-get update
RUN apt-get install -y g++ build-essential
RUN pip install --upgrade pip
RUN pip install numpy scipy pandas sympy matplotlib werkzeug Flask lxml unidecode requests Flask-HTTPAuth Flask-Mail pdfkit waitress bs4 sqlalchemy
RUN pip install semantic-version Pillow
RUN pip install Flask-WTF
RUN pip install wtforms[email]
RUN pip install Flask-SQLAlchemy
RUN pip install bootstrap-flask
RUN pip install flask-security
RUN pip install Flask-Migrate
RUN pip install Flask-Reuploaded
RUN apt-get update
RUN pip install pyTelegramBotAPI
RUN pip install semantic_version
RUN pip install Flask-Session
RUN pip install --upgrade wtforms==2.3.3
EXPOSE 80
CMD python /flask/app.py