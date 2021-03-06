# Configure
json 형태의 환경설정 파일을 불러올수 있는 모듈

- 파일 이름은 app.json으로 저장합니다.

```json
{
    "log_path":"C:\\Logs\\",
    "data":{
        "desc":"Hello world!",
        "type":3,
    }
}
```


-  불러올 폴더 지정 시 해당 위치에서 app.json 파일을 불러옵니다.
```json
CONFIG = python-utils.Configure(
    os.path.dirname(os.path.realpath(__file__))
)

print CONFIG.LOG_PATH
print CONFIG.DATA.DESC
print CONFIG.DATA.TYPE
```

# Logger
간단한 로깅을 할 수 있는 모듈

- 폴더를 지정하면 하위 폴더로 /logs/ 폴더 생성 후 로그를 기록 합니다.
```python
logger = python-utils.Logger(
    os.path.dirname(os.path.realpath(__file__))
)

logging.info('Hello world!')
```

# Archive
- Github.Issue 기능을 원격 저장소 처럼 사용 하며 기본적으로 0번 이슈를 사용하며 json 형태로 저장/불러온다.

```python
archive = python-utils.Archive(
    'Github-Access-Token',
    'Github-Repositery-Url'
)

MyData = archive.find('MyData')

# BlahBlahBlah...

archive.save()
```

# HtmlMaker
- jinja2를 이용하여 간단하게 HTML 결과를 변환합니다.

```html
<!-- ./template/index.html -->
<div>{{ name }}</div>
```

```python
python-utils.HtmlMaker(
    './template/index.html',
    context={'name':'kim'}
)
```
