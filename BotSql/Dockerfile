FROM python:3.9
RUN mkdir ./BotSql/
COPY ./ ./BotSql/
RUN mkdir ./ProcurementsDB/
RUN apt update && apt install sqlite3
RUN python -m pip install -r ./BotSql/requirements.txt
WORKDIR ./BotSql/
CMD [ "python", "main.py" ]
