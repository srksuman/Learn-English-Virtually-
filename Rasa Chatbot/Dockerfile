# FROM ubuntu:20.04
# ENTRYPOINT []
# RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==3.0.4
# ADD . /app/
# RUN chmod +x /app/start_services.sh
# CMD /app/start_services.sh

FROM ubuntu:20.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==3.0.4
WORKDIR /app
COPY . .
# RUN chmod +x /app/start_services.sh
# RUN rasa train nlu
# CMD /app/start_services.sh
# USER 1001
# ENTRYPOINT ['rasa']
# CMD ['run','--enable-api','--port','8080']