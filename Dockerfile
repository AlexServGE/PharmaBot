FROM python:3.9
COPY ./ ./
RUN apt update && apt install sqlite3
RUN python -m pip install -r ./ParserSql/requirements.txt
CMD [ "python", "./ParserSql/main.py" ]