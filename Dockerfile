FROM python:3.7
WORKDIR /code/gt-backend

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

ENV FLASK_APP=manage:app
ENV DATABASE_URL=mysql+pymysql://leec:gt12345@47.103.15.202/gt
ENV GT_BACKEND_ENV=prod
ENV QINIU_ACCESS_KEY=Pco9XbjBbZdGPobBC-utKlu8E6LzQa6iGus1PJQ4
ENV QINIU_SECRET_KEY=J_nR-azh496Xv2TyoVX1Ru4awbVDu8CudDlx15LO
ENV QINIU_BUCKET_NAME=gotoken-test
ENV QINIU_BUCKET_DOMAIN=q1tvwz2mb.bkt.clouddn.com

CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py"]