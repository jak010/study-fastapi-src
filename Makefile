
# FastAPI Server Run
run.local:
	uvicorn main:create_app --factory --reload

run.deploy:
	gunicorn main:create_app --worker-class uvicorn.workers.UvicornWorker -w 4 --keep-alive 10 --preload

orm.model:
	#sqlacodegen --generator tables mysql+pymysql://root:1234@127.0.0.1:9901/fastapi

	sqlacodegen mysql+pymysql://root:1234@127.0.0.1:9901/fastapi

update.pkg:
	pip freeze > requirements.txt