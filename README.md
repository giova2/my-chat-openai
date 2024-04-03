At the moment we write this document the min version of Python used is 3.11

These are the steps to execute it locally

- To create the env

`python3 -m venv ./.venv`

- To use the env we just created:

`source DIRECTORY_PATH_TO_THE_ENV/.venv`

- Install the packages required:

`pip install --no-cache-dir --upgrade uvicorn fastapi openai`

Then, the command used to run the app:

`uvicorn main:app --port 8080 --reload`