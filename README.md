# SmarTool - Smart Util Tool for Python

## 简介

SmarTool是一个小而全的Python工具类库，类似Java的[Hutool][1]。

## 安装

`pip install SmarTool`
```commandline
>>> import SmarTool
>>> SmarTool.hello()
======= Hello, this is SmarTool! =======
 Author: Harpsichord
 Email: tliu1217@163.com
 Install: pip install SmarTool
 Github: https://github.com/Harpsichord1207/SmarTool
========================================
```

## 使用

### 1. Retry - 重试工具

```python
import random
import requests
from SmarTool import retry

# 默认重试5次，每次间隔2秒，所有异常都重试
@retry
def div1(a, b):
    return a / random.choice([0, 1, b])
div1(2, 1)

# 重试10次，每次间隔1秒，仅在出现ZeroDivisionError时重试
@retry(times=10, delay=1, catch_error=ZeroDivisionError)
def div2(a, b):
    return a / random.choice([0, 1, b])
div2(2, 1)

# 在出现TypeError时不重试直接抛出异常
@retry(ignore_error=TypeError)
def div3(a, b):
    return a / random.choice([0, 1, b])
div3(2)

# 出现指定的多个异常时重试
@retry(catch_error=[requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout])
def get():
    return requests.get("https://xxx.com").json()
get()
```

### 2. Timeout - 超时工具

```python
import time
from SmarTool import timeout

# 默认超时时间为5秒，函数执行时间超过5秒抛出TimeoutException
@timeout
def f1():
    time.sleep(6)
f1()

# 自定义超时时间为10秒
@timeout(seconds=10)
def f2():
    time.sleep(6)
f2()
```

### 3. DTUtil - 日期工具

```python
import datetime
from SmarTool import DTUtil

# 当前日期增加一个月
print(DTUtil.add_month().strftime("%Y-%m-%d"))  # Out: 2022-05-01

# 指定日期增加10个月
date = datetime.datetime.strptime("2022-04-01", "%Y-%m-%d")
print(DTUtil.add_month(date, months=10).strftime("%Y-%m-%d"))  # Out: 2023-02-01

# 获取某个日期当月第一天
date = datetime.datetime.strptime("2022-03-22", "%Y-%m-%d")
print(DTUtil.first_day_of_month(date).strftime("%Y-%m-%d"))  # Out: 2022-03-01

# 获取某个日期当月最后一天
print(DTUtil.last_day_of_month(date).strftime("%Y-%m-%d"))  # Out: 2022-03-31
```

### 4. Flatter - 数据打平工具

```python
from SmarTool import Flatter

# 打平list
data = [1, (2, [3, 4, (5, 6)])]
Flatter.flat_list(data)  # Out: [1, 2, 3, 4, 5, 6]

# 打平dict
data = {1: 2, 3: {4: 5, 6: [7, 8]}}
Flatter.flat_dict(data)  # Out: {1: 2, '3_4': 5, '3_6_0': 7, '3_6_1': 8}

# 打平复杂的dict
data = {
    'k1': 'v1',
    'k2_list': [
        {'v2': 'v3'},
        {'v4': 'v5'},
    ],
    'k3': {
        'k4': ['k5', {'k6': 'k7'}],
        'k8': 'k9'
    }
}
Flatter.flat_dict(data)
# Out: 
# {
#     'k1': 'v1',
#     'k2_list_0_v2': 'v3',
#     'k2_list_1_v4': 'v5',
#     'k3_k4_0': 'k5',
#     'k3_k4_1_k6': 'k7',
#     'k3_k8': 'k9'
# }
```

[1]: https://github.com/dromara/hutool
