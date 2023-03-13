FROM python:3.10-bullseye
LABEL maintainer="Kishan Jadav <kishan_jadav@hotmail.com>"

WORKDIR /app

################################

# Update and Install system dependencies as root
RUN apt-get update && \
    apt-get install -y apt-transport-https lsb-release && \
    echo "deb https://notesalexp.org/tesseract-ocr5/$(lsb_release -cs)/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/notesalexp.list > /dev/null && \
    apt-get update -oAcquire::AllowInsecureRepositories=true && apt-get install -y --allow-unauthenticated notesalexp-keyring -oAcquire::AllowInsecureRepositories=true && \
    apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev wget curl poppler-utils cmake ffmpeg libsm6 libxext6 && \
    apt-get clean all

# Find the "tessdata" folder, and download the portuguese language data file.
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
COPY requirements.in .
RUN pip install --upgrade pip
RUN pip install pip-tools && \
    python -m piptools compile requirements.in --resolver=backtracking && \
    python -m piptools sync requirements.txt --pip-args="--no-cache-dir --no-deps"

COPY --chown=appuser:appuser . /app
