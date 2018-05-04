FROM python:3.6-alpine
ADD . /current_dir
WORKDIR /current_dir
RUN apk add --update curl gcc g++
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install -r requirements.txt
RUN python paint_python.py