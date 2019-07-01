# Dockerfile

FROM python:3.7-stretch
MAINTAINER Yehonatan Buchnik <yon_b@cs.technion.ac.il>

ENV SPINNER_HOME /spinner

RUN mkdir -p ${SPINNER_HOME}

VOLUME /tmp/Spinner

ENV ID=0
ENV SPINNER_IP="127.0.0.1"
ENV SPINNER_PORT=8000
ENV CORE_IP="127.0.0.1"
ENV CORE_PORT=9876

COPY src $SPINNER_HOME
RUN  pip3 install protobuf \
        && pip3 install grpcio-tools \
        && pip3 install django \
        && pip3 install djangorestframework


ENTRYPOINT sed -i 's/CORE_IP =.*/CORE_IP = '${CORE_IP}'/g' ${SPINNER_HOME}/settings.py \
            &&  sed -i 's/CORE_RPCS_PORT =.*/CORE_RPCS_PORT = '${CORE_PORT}'/g' ${SPINNER_HOME}/settings.py \
            && python3 spinner/manage.py runserver ${SPINNER_IP}:${SPINNER_PORT}

STOPSIGNAL SIGTERM
