FROM python:3.6.4-slim-stretch

# bind python3 as python
RUN ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip

# install python requirements
COPY requirements.txt hidonash/requirements.txt
RUN pip install -r hidonash/requirements.txt

#install application
RUN mkdir -p /hidonash
COPY app /hidonash/app
COPY hidonash.py /hidonash/hidonash.py
COPY config.py /hidonash/config.py
COPY migrations /hidonash/migrations 

COPY entrypoint.sh /hidonash/entrypoint.sh
RUN chmod +x /hidonash/entrypoint.sh

WORKDIR /hidonash

EXPOSE 5000
ENV FLASK_APP=hidonash.py
ENV FLASK_ENV=development

ENTRYPOINT ["./entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]

