FROM labpositiva/latex:3.6.1
MAINTAINER Luis Mayta <@slovacus>

COPY ./requirements/ /app/requirements/
COPY ./requirements.txt /app/requirements.txt

# set working directory to /usr/src/
WORKDIR /usr/src/

# Install sphinx dependences
RUN pip install -r /usr/src/requirements/docs.txt