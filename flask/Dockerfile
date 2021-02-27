FROM python:3.6.4-slim-stretch

# bind python3 as python
RUN ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip

# install basic needs
RUN apt-get update && apt-get install -y \
    vim \
    git

# install pip requirements
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY entrypoint.sh /hidonash/entrypoint.sh
RUN chmod +x /hidonash/entrypoint.sh

WORKDIR /hidonash

EXPOSE 5000
ENV FLASK_APP=hidonash.py
ENV FLASK_ENV=development

ENTRYPOINT ["./entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]

