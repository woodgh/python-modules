# python-moudle
자주 사용하는 기능들을 모아서 묶음 형태로 만들었습니다.

## Configure
json 형태의 환경설정 파일을 불러올수 있는 모듈

- 환경설정 예제
파일 이름은 app.json으로 저장합니다.

```json
{
    "log_path":"C:\\Logs\\"
}
```


-  사용 예제
불러올 폴더 지정 시 해당 위치에서 app.json 파일을 불러옵니다.
```json
CONFIG = python-utils.Configure(
    os.path.dirname(os.path.realpath(__file__))
)

print CONFIG.LOG_PATH
```

## Logger
간단한 로깅을 할 수 있는 모듈

폴더를 지정하면 하위 폴더로 /logs/ 폴더 생성 후 로그를 기록 합니다.
```python
logger = python-utils.Logger(
    os.path.dirname(os.path.realpath(__file__))
)

logging.info('Hello world!')
```

## Archive
Github.Issue 기능을(0번 이슈 사용) 활용한 원격 저장소 모듈

```python
archive = python-utils.Archive(
    'Github-Access-Token',
    'Github-Repositery-Url'
)

MyData = archive.find('MyData')

# BlahBlahBlah...

archive.save()
```