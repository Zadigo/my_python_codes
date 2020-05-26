FROM ubuntu:latest as builder

RUN mkdir /home/scrapper/

WORKDIR /home/scrapper/

COPY ./server.py .
COPY ./scrapper.py .


EXPOSE 4000

RUN pip3 install pipenv
RUN pipenv install --deploy --system

RUN [ "python", "-m", "server.py" ]



FROM ubuntu:latest

COPY --from=builder /home/scrapper/scrapper.py .
