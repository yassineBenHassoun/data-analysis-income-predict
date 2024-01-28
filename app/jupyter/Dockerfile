FROM python:3.8

EXPOSE 8888

RUN pip install \
  numpy \
  pandas \
  notebook \
  mysqlclient \
  mysql-connector-python \
  matplotlib \
  scipy \
  seaborn \
  scikit-learn \
  chardet \
  requests \
  pycountry

RUN mkdir /app
COPY /resources /app
WORKDIR /app

ENTRYPOINT [ "jupyter" ]
CMD [ "notebook","--allow-root","--ip=0.0.0.0"]