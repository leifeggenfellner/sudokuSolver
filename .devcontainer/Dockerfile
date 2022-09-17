FROM ubuntu:latest

WORKDIR /app

COPY ../requirements.txt ./

RUN apt -y update && apt -y install python3-pip

RUN pip install -r requirements.txt

CMD ["pip", "show", "pygame"]
