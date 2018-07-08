# 准备环境
```bash
pyenv versions
pyenv local 3.6.1

pip install --upgrade google-api-python-client
pip install --upgrade oauth2client
```

# 使用python调用google calendar api
https://developers.google.com/calendar/quickstart/python

https://developers.google.com/calendar/create-events


# 使用代理访问API
refer https://medium.com/google-cloud/accessing-google-cloud-apis-though-a-proxy-fe46658b5f2a

```bash
# 只有带协议的版本是可以的
https_proxy=192.168.234.1:8123 python quickstart.py
https_proxy=http://192.168.234.1:8123 python quickstart.py

# 都可以
https_proxy=192.168.234.1:8123 curl https://www.google.com
https_proxy=http://192.168.234.1:8123 curl https://www.google.com
```
