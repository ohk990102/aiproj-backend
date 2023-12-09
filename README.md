# 2023 Hackathon (backend)

- Duration: 30h / Dec 09, 2023 (Sat) 09:30 ~ Dec 10, 2023 (Sun) 15:30

## How to Run

Linux(WSL) or macOS and Python 3.10+ is required to run.

```sh
$ python --version  # Check python version
Python 3.10.12
$ git clone <THIS_REPOSITORY_URL>
  ...
$ cd aiproj-backend
$ python -m venv venv       # Virtual enviroment 설치
$ source venv/bin/activate
$ pip install -r requirements.txt
  ...
$ python main.py --host localhost
...
INFO:     Started server process
...
```

Connect to `http://localhost:8000/docs` to see API documents.

## Formatting

Use ufmt. [PyPI](https://pypi.org/project/ufmt/)

```sh
$ pip install ufmt==2.3.0
```

If you are using VSCode, using extension is recommended. [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=omnilib.ufmt)
