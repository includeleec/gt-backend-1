FROM python:3.7
WORKDIR /code/gt-backend

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

ENV FLASK_APP manage:app
ENV DATABASE_URL mysql+pymysql://leec:gt12345@47.103.15.202/gt
ENV GT_BACKEND_ENV prod

CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py"]