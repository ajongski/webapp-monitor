FROM python:3.10-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk --no-cache add curl
RUN apk add --no-cache bash
COPY requirements.txt requirements.txt
#COPY healthcheck.sh healthcheck.sh
#COPY smtp.py smtp.py
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run", "--debug"]
#RUN ["chmod", "+x", "./healthcheck.sh"]
#ENTRYPOINT ["./healthcheck.sh"]