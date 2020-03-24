FROM python:3.7-stretch

RUN apt-get update -y

RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.5' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

WORKDIR /usr/src/app/flask-tutorial

#RUN mkdir -p /home/user/flask-tutorial

COPY . .

RUN pip3 install -r requirements.txt

#RUN pip install pygobject wxPython wxPython-common
#RUN python3 manage.py db init && python3 manage.py db migrate

ENV PYTHONPATH /usr/src/app/flask-tutorial/app

ENTRYPOINT [ "python3" ]

CMD [ "run.py" ]

EXPOSE 5005

