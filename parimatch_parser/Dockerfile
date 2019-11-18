FROM python:3.5-stretch
 ENV PYTHONUNBUFFERED 1
 RUN apt-get update && apt-get install -y \
     fonts-liberation \
     libappindicator3-1 \
     libasound2 \
     libatk-bridge2.0-0 \
     libatk1.0-0 \
     libcairo2 \
     libcups2 \
     libdbus-1-3 \
     libgdk-pixbuf2.0-0 \
     libnspr4 \
     libnss3 \
     libx11-xcb1 \
     lsb-release \
     xdg-utils
 RUN mkdir /parser
 WORKDIR /parser
 COPY chromedriver /usr/local/bin/chromedriver
 COPY google-chrome-68.0.3440.84-1_amd64.deb /parser
 RUN dpkg -i google-chrome-68.0.3440.84-1_amd64.deb
 COPY requirements.txt /parser
 RUN pip install -r requirements.txt
 ENV DISPLAY=:99
 COPY html_parser.py \
      main.py /parser/

 CMD /usr/local/bin/python main.py