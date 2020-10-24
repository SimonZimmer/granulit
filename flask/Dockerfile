FROM python:3.6.4-slim-stretch

# bind python3 as python
RUN ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip

# install flask
COPY requirements.txt /
RUN pip install -r /requirements.txt

# install application
RUN mkdir -p /hidonash
COPY app /hidonash/app
COPY hidonash.py /hidonash/hidonash.py

WORKDIR /hidonash

EXPOSE 5000
ENV FLASK_APP=hidonash.py
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0"]

