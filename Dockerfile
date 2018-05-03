# FROM python:3.6-alpine
ADD . /current_dir
WORKDIR /current_dir
RUN pip install -r requirements.txt
RUN python paint_python.py