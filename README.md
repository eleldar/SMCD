# Speech Message Crime Detection (SMCD)

## Environment
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
apt install ffmpeg (for Windows using exe-file)
...
to be continued ...!
```


## Models
```
cd api
mkdir models
cd models
wget "https://alphacephei.com/vosk/models/vosk-model-PASTE"
unzip vosk-model-PASTE.zip
mv vosk-model-PASTE ru
```

## Using
```
cd api
python main.py
```
from browser open adress 127.0.0.1:5000/api

## API methods
* start - загрузка аудио и получение id
* tasks - получение списка задач (сохраняются до явного удаления)
* удаление задачи по ID
* getstatus - получение статуса по ID:
  - "bad id" - нет такой задачи;
  - "on processing" - в процессе выполнения;
  - "done" - готовый результат.
* result - получение результата по ID (внимание на код HTTP):
  - 200 - распознанный текст
  - 404 - ошибка с уточнением результатв "bad id" или "on processing"


## Structure
```
.
├── api
│   ├── main.py
│   ├── __init__.py
│   ├── models
│   │   └── ru
│   │       ├── am
│   │       │   ├── final.mdl
│   │       │   └── tree
│   │       ├── conf
│   │       │   ├── mfcc.conf
│   │       │   └── model.conf
│   │       ├── graph
│   │       │   ├── disambig_tid.int
│   │       │   ├── Gr.fst
│   │       │   ├── HCLr.fst
│   │       │   ├── phones
│   │       │   │   └── word_boundary.int
│   │       │   ├── phones.txt
│   │       │   └── words.txt
│   │       ├── ivector
│   │       │   ├── final.dubm
│   │       │   ├── final.ie
│   │       │   ├── final.mat
│   │       │   ├── global_cmvn.stats
│   │       │   ├── online_cmvn.conf
│   │       │   └── splice.conf
│   │       └── README
│   ├── tempfiles
│   │   ├── src
│   │   └── tgt
│   └── tools
│       ├── recognitions.py
│       ├── handler.py
│       ├── manager.py
│       ├── postprocess.py
│       └── preprocess.py
├── tests
│   └── functional_test.py
├── README.md
└── requirements.txt
```
