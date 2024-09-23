FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash lms && chmod 777 /opt /run

WORKDIR /lms

RUN mkdir /lms/static && mkdir /lms/media && chown -R lms:lms /lms && chmod 755 /lms

COPY --chown=lms:lms . .

RUN pip install -r requirements.txt

# USER lms

CMD ["gunicorn","-b","0.0.0.0:8001","myproject.wsgi:application"]
