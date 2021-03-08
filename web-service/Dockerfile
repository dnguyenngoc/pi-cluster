FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

LABEL maintainer="Duy Nguyen <duyngunyenngoc@hotmail.com>"

COPY ./app /app

COPY requirements.txt requirements.txt

WORKDIR /app

RUN apk add --no-cache --virtual .build-deps gcc g++ make libffi-dev openssl-dev python-dev \
    && pip3 install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

EXPOSE 8080
