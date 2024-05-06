echo 'Installing dependencies from "requirements.txt"'
python -m pip install -r requirements.txt

jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 exercises/1-create-cosmos-db.ipynb
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 exercises/2-create-azure-search.ipynb
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 exercises/3-create-connections.ipynb