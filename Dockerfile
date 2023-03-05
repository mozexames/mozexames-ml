# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10
LABEL maintainer="Kishan Jadav <kishan_jadav@hotmail.com>"

WORKDIR /app

################################

# Update and Install system dependencies as root
RUN apt-get update -qq
RUN apt-get install -y tesseract-ocr libtesseract-dev wget curl poppler-utils

# Find the "tessdata" folder, and download the portuguese language data file to it.
# The data folder found should be located at: /usr/share/tesseract-ocr/4.00/tessdata
ENV TESSERACT_LANG_FILENAME="por.traineddata"
ENV TESSERACT_LANG_URL="https://github.com/tesseract-ocr/tessdata_best/raw/main/${TESSERACT_LANG_FILENAME}"
RUN wget -O $(find /usr -name tessdata)/$TESSERACT_LANG_FILENAME $TESSERACT_LANG_URL

################################

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Upgrade pip to its latest version and install Python dependencies using the version of pip installed in the venv
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY --chown=appuser:appuser . /app
