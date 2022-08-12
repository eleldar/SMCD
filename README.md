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
│   ├── tempfiles
│   │   ├── src
│   │   └── tgt
│   └── tools
│       ├── models
│       │   └── ru
│       │       └── /
│       ├── recognitions.py
│       ├── handler.py
│       ├── manager.py
│       ├── postprocess.py
│       └── preprocess.py
├── tests
│   └── functional_test.py
├── README.md
├── venv 
│   └── /
└── requirements.txt
```
