FROM python:3.6

WORKDIR /root

RUN \
     apt-get update -q \
  && apt-get install -yq \
       unzip \
       curl \
       build-essential \
       libssl-dev \
       xvfb

# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

ADD deploy/configs/xvfb_init /etc/init.d/xvfb
RUN chmod a+x /etc/init.d/xvfb

ADD deploy/configs/xvfb-daemon-run /usr/bin/xvfb-daemon-run
RUN chmod a+x /usr/bin/xvfb-daemon-run

RUN mkdir -p /root/www/imhio

WORKDIR www/imhio

COPY requirements.txt /root/www/imhio/requirements.txt

RUN pip install -r requirements.txt

COPY . /root/www/imhio

CMD ["./docker-entrypoint.sh"]
