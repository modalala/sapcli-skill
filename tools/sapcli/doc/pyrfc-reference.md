# PyRFC 功能参考文档

> 本文档为 sapcli 开发团队提供 PyRFC 库的完整功能参考
> 
> 版本: PyRFC 2.x/3.x | 更新日期: 2026-03-03

---

## 📋 目录

1. [概述](#概述)
2. [核心类与模块](#核心类与模块)
3. [Connection 类详解](#connection-类详解)
4. [数据类型映射](#数据类型映射)
5. [异常处理](#异常处理)
6. [高级功能](#高级功能)
7. [配置参数](#配置参数)
8. [使用示例](#使用示例)
9. [与 sapcli 集成](#与-sapcli-集成)

---

## 概述

**PyRFC** 是 SAP NW RFC SDK 的 Python 绑定库，提供了 Python 调用 SAP RFC 函数模块的能力。

### 安装

```bash
pip install pynwrfc
```

### 依赖

- SAP NW RFC SDK 7.50+
- Python 3.7+
- C/C++ 编译器（用于构建）

---

## 核心类与模块

### 1. 主要模块结构

```python
import pyrfc

# 核心类
pyrfc.Connection          # RFC 连接管理
pyrfc._exception          # 异常类模块

# 异常类型
pyrfc._exception.RFCLibError           # 基础 RFC 错误
pyrfc._exception.LogonError            # 登录错误
pyrfc._exception.CommunicationError    # 通信错误
pyrfc._exception.ABAPRuntimeError      # ABAP 运行时错误
pyrfc._exception.ABAPApplicationError  # ABAP 应用错误
```

### 2. 快速入门

```python
from pyrfc import Connection

# 建立连接
conn = Connection(
    ashost='your-sap-host',
    sysnr='00',
    client='000',
    user='your-username',
    passwd='your-password'
)

# 调用 RFC 函数
result = conn.call('STFC_CONNECTION', REQUTEXT='Hello SAP')
print(result)

# 关闭连接
conn.close()
```

---

## Connection 类详解

### 构造函数参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ashost` | str | 条件 | 应用服务器主机名/IP |
| `mshost` | str | 条件 | 消息服务器主机名（负载均衡）|
| `sysnr` | str | 否 | 系统编号，默认 '00' |
| `client` | str | 是 | SAP 客户端编号 |
| `user` | str | 是 | 用户名 |
| `passwd` | str | 是 | 密码 |
| `lang` | str | 否 | 登录语言，默认 'EN' |
| `trace` | str | 否 | 跟踪级别 (0-3) |

### 连接方式

#### 方式 1: 直接连接应用服务器

```python
conn = Connection(
    ashost='hostname',
    sysnr='00',
    client='000',
    user='username',
    passwd='password'
)
```

#### 方式 2: 通过消息服务器（负载均衡）

```python
conn = Connection(
    mshost='message_server_host',
    r3name='SID',
    group='PUBLIC',
    client='000',
    user='username',
    passwd='password'
)
```

#### 方式 3: 使用 sapnwrfc.ini 配置

```python
conn = Connection(dest='MYDEST')  # 使用 sapnwrfc.ini 中的配置
```

### 主要方法

#### `call(rfc_function, **kwargs)`

调用 RFC 函数模块。

```python
# 基本调用
result = conn.call('RFC_FUNCTION_NAME', 
                   PARAM1='value1',
                   PARAM2='value2')

# 带表参数
result = conn.call('RFC_READ_TABLE',
                   QUERY_TABLE='USR02',
                   DELIMITER='|',
                   FIELDS=[{'FIELDNAME': 'BNAME'}])
```

#### `ping()`

测试连接是否存活。

```python
if conn.ping():
    print("连接正常")
```

#### `get_attributes()`

获取连接属性。

```python
attrs = conn.get_attributes()
print(attrs['sysId'])      # 系统 ID
print(attrs['client'])     # 客户端
print(attrs['user'])       # 当前用户
print(attrs['isoLanguage']) # 语言
```

#### `get_function_description(func_name)`

获取函数模块的元数据描述。

```python
func_desc = conn.get_function_description('RFC_READ_TABLE')

# 查看参数信息
for param in func_desc.parameters:
    print(f"参数名: {param['name']}, 类型: {param['type']}")
```

#### `close()`

关闭连接。

```python
conn.close()
```

### 上下文管理器支持

```python
with Connection(ashost='...', client='...', user='...', passwd='...') as conn:
    result = conn.call('STFC_CONNECTION', REQUTEXT='Hello')
    # 连接会自动关闭
```

---

## 数据类型映射

### ABAP 到 Python 类型映射

| ABAP 类型 | Python 类型 | 示例 |
|-----------|-------------|------|
| `C` (CHAR) | `str` | `'Hello'` |
| `N` (NUM) | `str` | `'00123'` |
| `D` (DATE) | `str` (YYYYMMDD) | `'20240303'` |
| `T` (TIME) | `str` (HHMMSS) | `'143000'` |
| `I` (INT) | `int` | `123` |
| `INT8` | `int` | `123456789012` |
| `F` (FLOAT) | `float` | `123.45` |
| `P` (BCD) | `Decimal` | `Decimal('123.45')` |
| `X` (BYTE) | `bytes` | `b'\x01\x02'` |
| `STRING` | `str` | `'Long text'` |
| `XSTRING` | `bytes` | `b'\x00\x01\x02'` |
| `Structure` | `dict` | `{'FIELD1': 'val1', 'FIELD2': 'val2'}` |
| `Table` | `list[dict]` | `[{'COL1': 'val1'}, {'COL1': 'val2'}]` |

### 特殊类型处理

#### DECIMAL/BCD 类型

```python
from decimal import Decimal

# 输入 Decimal
result = conn.call('BAPI_SOMETHING',
                   AMOUNT=Decimal('123.45'),
                   CURRENCY='USD')

# 输出也是 Decimal
amount = result['RETURN']['AMOUNT']  # Decimal('123.45')
```

#### 日期和时间

```python
# 日期格式: YYYYMMDD
result = conn.call('BAPI_USER_GET_DETAIL',
                   USERNAME='DEVELOPER',
                   VALID_DATE='20240303')

# 时间格式: HHMMSS
result = conn.call('SOME_FUNCTION',
                   START_TIME='143000')
```

#### 二进制数据

```python
# XSTRING / BYTE 类型
with open('file.pdf', 'rb') as f:
    file_content = f.read()

result = conn.call('UPLOAD_DOCUMENT',
                   FILE_CONTENT=file_content,
                   FILE_NAME='document.pdf')
```

---

## 异常处理

### 异常类层次

```
RFCLibError (基类)
├── LogonError              # 登录失败
├── CommunicationError      # 通信错误
├── ABAPRuntimeError        # ABAP 运行时错误 (Short dump)
├── ABAPApplicationError    # ABAP 应用错误 (RAISE EXCEPTION)
└── ExternalRuntimeError    # 外部运行时错误
```

### 异常属性

| 属性 | 说明 |
|------|------|
| `message` | 错误消息 |
| `code` | 错误代码 |
| `key` | ABAP 异常键 |
| `msg_class` | 消息类 |
| `msg_type` | 消息类型 (E, W, I, S, A, X) |
| `msg_number` | 消息编号 |

### 异常处理示例

```python
from pyrfc import Connection
from pyrfc._exception import (
    LogonError,
    CommunicationError,
    ABAPRuntimeError,
    ABAPApplicationError
)

try:
    conn = Connection(ashost='...', client='...', user='...', passwd='...')
    result = conn.call('SOME_FUNCTION', PARAM='value')
    
except LogonError as e:
    print(f"登录失败: {e.message}")
    print(f"错误代码: {e.code}")
    
except CommunicationError as e:
    print(f"通信错误: {e.message}")
    
except ABAPRuntimeError as e:
    print(f"ABAP 运行时错误: {e.message}")
    print(f"Short dump 键: {e.key}")
    
except ABAPApplicationError as e:
    print(f"ABAP 应用错误: {e.message}")
    print(f"异常键: {e.key}")
```

---

## 高级功能

### 1. 批量处理 (Batch Processing)

```python
# 使用同一个连接执行多个调用
with Connection(...) as conn:
    for user in user_list:
        result = conn.call('BAPI_USER_GET_DETAIL', USERNAME=user)
        process_result(result)
```

### 2. 事务处理 (tRFC/qRFC/bgRFC)

```python
# 创建事务
transaction = conn.create_transaction()

# 添加调用到事务
transaction.add_call('BAPI_SOME', PARAM1='val1')
transaction.add_call('BAPI_OTHER', PARAM2='val2')

# 提交事务
transaction.submit()

# 确认事务
transaction.confirm()
```

### 3. 元数据查询

```python
# 获取函数描述
func_desc = conn.get_function_description('RFC_READ_TABLE')

# 参数信息
for param in func_desc.parameters:
    print(f"名称: {param['name']}")
    print(f"类型: {param['type']}")
    print(f"方向: {param['direction']}")  # IMPORT, EXPORT, CHANGING, TABLES
    print(f"可选: {param['optional']}")
    print(f"默认值: {param.get('defaultValue', '')}")

# 结构字段信息
for field in func_desc.parameters[0]['structure']:
    print(f"字段: {field['name']}, 类型: {field['type']}, 长度: {field['length']}")
```

### 4. 连接池

```python
from pyrfc import ConnectionPool

# 创建连接池
pool = ConnectionPool(
    ashost='...',
    client='...',
    user='...',
    passwd='...',
    pool_size=10,      # 池大小
    max_overflow=5,    # 最大溢出
    pool_timeout=30    # 获取连接超时
)

# 从池中获取连接
with pool.acquire() as conn:
    result = conn.call('STFC_CONNECTION', REQUTEXT='Hello')
```

### 5. 服务器端编程

```python
from pyrfc import Server

# 定义处理函数
def my_handler(request_context, **params):
    return {'RESULT': f"Received: {params.get('INPUT', '')}"}

# 创建服务器
server = Server(
    gwhost='gateway_host',
    gwserv='sapgw00',
    program_id='MY_SERVER',
    function_handlers={'Z_MY_FUNCTION': my_handler}
)

# 启动服务器
server.serve()
```

### 6. 通过 Router 连接

```python
conn = Connection(
    ashost='target_host',
    sysnr='00',
    client='000',
    user='username',
    passwd='password',
    saprouter='/H/saprouter_host/S/port/H/'
)
```

### 7. SNC 安全连接

```python
conn = Connection(
    mshost='message_server',
    r3name='SID',
    group='PUBLIC',
    client='000',
    snc_mode='1',
    snc_partnername='p:CN=SAP, O=Company, C=DE',
    snc_lib='/path/to/snc_library.so',
    snc_qop='9'  # 最高安全级别
)
```

---

## 配置参数

### 环境变量

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `SAPNWRFC_HOME` | NW RFC SDK 安装路径 | `/usr/sap/nwrfcsdk` |
| `LD_LIBRARY_PATH` | 库文件搜索路径 (Linux) | `$SAPNWRFC_HOME/lib` |
| `PATH` | 可执行文件搜索路径 (Windows) | `%SAPNWRFC_HOME%\lib` |

### 连接参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `trace` | 跟踪级别 (0-3) | 0 |
| `lang` | 登录语言 | EN |
| `timeout` | 连接超时(秒) | 无 |
| `codepage` | 代码页 | 系统默认 |
| `use_sapgui` | 使用 SAPGUI | 0 |

### sapnwrfc.ini 配置

```ini
DEFAULT
RFC_TRACE=2
RFC_TRACE_DIR=/var/log/rfc

DEST=PROD
ASHOST=prod-server
SYSNR=00
CLIENT=100
USER=username
PASSWD=password

DEST=DEV
MSHOST=dev-msg
R3NAME=DEV
GROUP=PUBLIC
CLIENT=200
USER=developer
PASSWD=password
```

---

## 使用示例

### 示例 1: 读取用户列表

```python
from pyrfc import Connection

conn = Connection(ashost='...', client='...', user='...', passwd='...')

# 调用 RFC_READ_TABLE
result = conn.call('RFC_READ_TABLE',
                   QUERY_TABLE='USR02',
                   DELIMITER='|',
                   FIELDS=[{'FIELDNAME': 'BNAME'},
                          {'FIELDNAME': 'GLTGV'},
                          {'FIELDNAME': 'GLTGB'}],
                   OPTIONS=[{'TEXT': "MANDT = '000'"}],
                   ROWCOUNT=100)

# 处理结果
for row in result['DATA']:
    fields = row['WA'].split('|')
    print(f"用户: {fields[0]}, 有效期从: {fields[1]}, 到: {fields[2]}")

conn.close()
```

### 示例 2: 创建用户 (BAPI)

```python
from pyrfc import Connection

conn = Connection(ashost='...', client='...', user='...', passwd='...')

# 准备地址数据
address = {
    'FIRSTNAME': 'John',
    'LASTNAME': 'Doe',
    'E_MAIL': 'john.doe@example.com'
}

# 准备登录数据
logondata = {
    'GLTGV': '20240301',
    'GLTGB': '99991231',
    'USTYP': 'A'  # 对话用户
}

# 调用 BAPI
result = conn.call('BAPI_USER_CREATE1',
                   USERNAME='JDOE',
                   ADDRESS=address,
                   LOGONDATA=logondata,
                   PASSWORD='Initial123!')

# 检查结果
if result['RETURN']['TYPE'] == 'S':
    print("用户创建成功")
    # 提交事务
    conn.call('BAPI_TRANSACTION_COMMIT', WAIT='X')
else:
    print(f"错误: {result['RETURN']['MESSAGE']}")
    conn.call('BAPI_TRANSACTION_ROLLBACK')

conn.close()
```

### 示例 3: 处理深度结构

```python
from pyrfc import Connection

conn = Connection(ashost='...', client='...', user='...', passwd='...')

# 嵌套结构示例
params = {
    'HEADER': {
        'DOC_TYPE': 'TA',
        'SALES_ORG': '1000',
        'DISTR_CHAN': '10',
        'DIVISION': '00'
    },
    'ITEMS': [
        {
            'ITM_NUMBER': '000010',
            'MATERIAL': 'MAT001',
            'TARGET_QTY': '10'
        },
        {
            'ITM_NUMBER': '000020',
            'MATERIAL': 'MAT002',
            'TARGET_QTY': '5'
        }
    ]
}

result = conn.call('BAPI_SALESORDER_CREATEFROMDAT2', **params)

# 处理返回的嵌套结构
order_number = result['SALESDOCUMENT']
for item in result['ORDER_ITEMS_OUT']:
    print(f"项目: {item['ITM_NUMBER']}, 物料: {item['MATERIAL']}")

conn.close()
```

---

## 与 sapcli 集成

### sapcli 中的 PyRFC 封装

```python
# sap/rfc/core.py
from sap.rfc.core import connect, rfc_is_available, try_pyrfc_exception_type

# 检查 RFC 是否可用
if rfc_is_available():
    print("RFC 功能可用")

# 建立连接
try:
    conn = connect(
        ashost='your-sap-host',
        sysnr='00',
        client='000',
        user='your-username',
        passwd='your-password'
    )
except RFCLoginError as e:
    print(f"登录失败: {e}")
except RFCCommunicationError as e:
    print(f"通信错误: {e}")

# 获取异常类型
pyrfc_exception = try_pyrfc_exception_type()
```

### startrfc 命令实现

```python
# sap/cli/startrfc.py
from sap.rfc.core import try_pyrfc_exception_type

def startrfc(connection, args):
    """执行任意 RFC 函数"""
    
    # 准备参数
    rfc_params = _get_call_rfc_params_from_args(args)
    
    # 获取 PyRFC 异常类型
    pyrfc_exception_type = try_pyrfc_exception_type()
    
    try:
        # 调用 RFC 函数
        resp = connection.call(
            args.RFC_FUNCTION_MODULE.upper(), 
            **rfc_params
        )
    except pyrfc_exception_type as ex:
        # 处理 PyRFC 异常
        console.printerr(f'{args.RFC_FUNCTION_MODULE} failed:')
        console.printerr(str(ex))
        return 1
    
    # 格式化输出
    response_formatted = FORMATTERS[args.output](resp)
    console.printout(response_formatted)
    return 0
```

### BAPI 返回处理

```python
# sap/rfc/bapi.py
class BAPIReturn:
    """处理 BAPI 返回结构"""
    
    def __init__(self, return_value):
        """
        return_value: BAPI 返回的结构或表
        """
        self._return = return_value
        self.is_error = self._check_error()
    
    def _check_error(self):
        """检查是否有错误"""
        if isinstance(self._return, list):
            return any(
                item.get('TYPE') in ('E', 'A', 'X') 
                for item in self._return
            )
        else:
            return self._return.get('TYPE') in ('E', 'A', 'X')
    
    def message_lines(self):
        """获取所有消息行"""
        messages = []
        items = self._return if isinstance(self._return, list) else [self._return]
        
        for item in items:
            msg = f"[{item.get('TYPE')}] {item.get('MESSAGE', '')}"
            messages.append(msg)
        
        return messages
```

---

## 故障排除

### 常见问题

#### 1. 导入错误

```python
# 错误: ImportError: No module named 'pyrfc'
# 解决: 安装 pynwrfc
pip install pynwrfc

# 错误: 找不到 SAP NW RFC SDK
# 解决: 设置环境变量
export SAPNWRFC_HOME=/usr/sap/nwrfcsdk
export LD_LIBRARY_PATH=$SAPNWRFC_HOME/lib:$LD_LIBRARY_PATH
```

#### 2. 连接错误

```python
# 错误: LogonError
# 原因: 用户名/密码错误，用户被锁定
# 解决: 检查凭据，解锁用户

# 错误: CommunicationError
# 原因: 网络问题，主机不可达
# 解决: 检查网络，防火墙设置
```

#### 3. 字符编码问题

```python
# 处理非 ASCII 字符
conn = Connection(
    ashost='...',
    client='...',
    user='用户',  # 中文字符
    passwd='密码',
    codepage='8400'  # 简体中文代码页
)
```

---

## 参考资源

- **官方文档**: https://sap.github.io/PyRFC/
- **GitHub**: https://github.com/SAP/PyRFC
- **SAP Note 2573953**: PyRFC 安装指南
- **SAP NW RFC SDK**: https://support.sap.com/nwrfcsdk

---

## 版本历史

| 版本 | 说明 |
|------|------|
| 3.x | 支持 Python 3.9+, 改进性能 |
| 2.x | 当前稳定版本，支持 Python 3.7+ |
| 1.x | 旧版本，已停止维护 |

---

## iFlow 使用 PyRFC 参考

### 概述

iFlow 平台使用 PyRFC 作为与 SAP 后端系统通信的核心组件，主要用于：
- 执行 RFC 函数模块
- 读取 SAP 数据
- 批量数据处理
- 与 ADT (ABAP Development Tools) 协同工作

### iFlow 配置结构

```
iFlow/
├── .env.sapcli              # SAP 连接配置
├── .iflow/
│   └── commands/            # iFlow 命令定义
├── openspec/
│   ├── changes/             # 变更管理
│   └── specs/               # OpenAPI 规范
└── src/                     # 源代码
```

### 环境配置

#### 1. 配置文件 (.env.sapcli)

```ini
# SAP 连接配置
SAP_ASHOST=your-sap-host
SAP_PORT=8000
SAP_CLIENT=000
SAP_USER=your-username
SAP_PASSWORD=your-password
SAP_SSL_VERIFY=no

# PyRFC 特定配置
SAP_CODEPAGE=8400
SAP_TRACE=0
SAP_TIMEOUT=300
```

#### 2. Python 配置加载

```python
# iFlow 配置加载示例
import os
from pyrfc import Connection

def load_sap_config():
    """从环境变量加载 SAP 配置"""
    return {
        'ashost': os.getenv('SAP_ASHOST'),
        'port': int(os.getenv('SAP_PORT', '443')),
        'client': os.getenv('SAP_CLIENT'),
        'user': os.getenv('SAP_USER'),
        'passwd': os.getenv('SAP_PASSWORD'),
        'ssl_verify': os.getenv('SAP_SSL_VERIFY', 'yes').lower() != 'no',
        'trace': int(os.getenv('SAP_TRACE', '0')),
        'codepage': os.getenv('SAP_CODEPAGE', '1100')
    }

def get_sap_connection():
    """获取 SAP 连接"""
    config = load_sap_config()
    return Connection(**config)
```

### iFlow 常用操作模式

#### 模式 1: 简单 RFC 调用

```python
# iflow/rfc/simple_call.py
from pyrfc import Connection
from contextlib import contextmanager

@contextmanager
def sap_connection():
    """上下文管理器管理连接"""
    conn = None
    try:
        conn = get_sap_connection()
        yield conn
    finally:
        if conn:
            conn.close()

def execute_rfc(function_name, **params):
    """执行 RFC 函数"""
    with sap_connection() as conn:
        result = conn.call(function_name, **params)
        return result

# 使用示例
result = execute_rfc(
    'RFC_READ_TABLE',
    QUERY_TABLE='USR02',
    DELIMITER='|',
    ROWCOUNT=10
)
```

#### 模式 2: 批量数据处理

```python
# iflow/rfc/batch_processor.py
from pyrfc import Connection
from typing import List, Dict, Any
import concurrent.futures

class BatchProcessor:
    """批量 RFC 处理器"""
    
    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.results = []
    
    def process_items(self, items: List[Dict], rfc_func: str, param_mapping: Dict):
        """
        批量处理项目
        
        Args:
            items: 要处理的数据项列表
            rfc_func: RFC 函数名
            param_mapping: 字段映射配置
        """
        with get_sap_connection() as conn:
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = []
                
                for item in items:
                    # 映射参数
                    params = self._map_params(item, param_mapping)
                    future = executor.submit(self._call_rfc, conn, rfc_func, params)
                    futures.append(future)
                
                # 收集结果
                for future in concurrent.futures.as_completed(futures):
                    try:
                        result = future.result()
                        self.results.append({'success': True, 'data': result})
                    except Exception as e:
                        self.results.append({'success': False, 'error': str(e)})
    
    def _map_params(self, item: Dict, mapping: Dict) -> Dict:
        """根据映射配置转换参数"""
        params = {}
        for target, source in mapping.items():
            if callable(source):
                params[target] = source(item)
            else:
                params[target] = item.get(source)
        return params
    
    def _call_rfc(self, conn, func_name, params):
        """执行 RFC 调用"""
        return conn.call(func_name, **params)

# 使用示例
processor = BatchProcessor(max_workers=3)
items = [
    {'material': 'MAT001', 'quantity': 10},
    {'material': 'MAT002', 'quantity': 20}
]
mapping = {
    'MATERIAL': 'material',
    'QUANTITY': 'quantity'
}
processor.process_items(items, 'BAPI_MATERIAL_GET_DETAIL', mapping)
```

#### 模式 3: BAPI 事务处理

```python
# iflow/rfc/bapi_transaction.py
from pyrfc import Connection
from typing import List, Dict

class BAPITransaction:
    """BAPI 事务管理器"""
    
    def __init__(self, conn: Connection):
        self.conn = conn
        self.operations = []
        self.has_error = False
    
    def add_operation(self, bapi_name: str, params: Dict):
        """添加 BAPI 操作"""
        self.operations.append({
            'bapi': bapi_name,
            'params': params
        })
    
    def execute(self) -> List[Dict]:
        """执行所有操作并提交/回滚"""
        results = []
        
        try:
            # 执行所有 BAPI 调用
            for op in self.operations:
                result = self.conn.call(op['bapi'], **op['params'])
                results.append(result)
                
                # 检查返回消息
                if self._has_error(result):
                    self.has_error = True
                    break
            
            # 提交或回滚
            if self.has_error:
                self.conn.call('BAPI_TRANSACTION_ROLLBACK')
            else:
                self.conn.call('BAPI_TRANSACTION_COMMIT', WAIT='X')
            
            return results
            
        except Exception as e:
            self.conn.call('BAPI_TRANSACTION_ROLLBACK')
            raise e
    
    def _has_error(self, result: Dict) -> bool:
        """检查 BAPI 返回是否有错误"""
        return_data = result.get('RETURN', {})
        
        if isinstance(return_data, list):
            return any(
                item.get('TYPE') in ('E', 'A', 'X')
                for item in return_data
            )
        else:
            return return_data.get('TYPE') in ('E', 'A', 'X')

# 使用示例
with get_sap_connection() as conn:
    tx = BAPITransaction(conn)
    
    # 添加创建操作
    tx.add_operation('BAPI_USER_CREATE1', {
        'USERNAME': 'NEWUSER',
        'ADDRESS': {'FIRSTNAME': 'John', 'LASTNAME': 'Doe'},
        'LOGONDATA': {'USTYP': 'A'},
        'PASSWORD': 'Initial123!'
    })
    
    # 添加分配角色操作
    tx.add_operation('BAPI_USER_ACTGROUPS_ASSIGN', {
        'USERNAME': 'NEWUSER',
        'ACTIVITYGROUPS': [{'AGR_NAME': 'SAP_ALL'}]
    })
    
    results = tx.execute()
```

#### 模式 4: 元数据缓存

```python
# iflow/rfc/metadata_cache.py
from pyrfc import Connection
import json
import os
from typing import Dict, Optional

class MetadataCache:
    """RFC 元数据缓存管理"""
    
    CACHE_DIR = '.iflow/cache/rfc'
    
    def __init__(self):
        os.makedirs(self.CACHE_DIR, exist_ok=True)
    
    def get_function_desc(self, conn: Connection, func_name: str) -> Dict:
        """获取函数描述（带缓存）"""
        cache_file = os.path.join(self.CACHE_DIR, f'{func_name}.json')
        
        # 尝试从缓存加载
        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # 从 SAP 获取
        func_desc = conn.get_function_description(func_name)
        
        # 转换为可序列化格式
        desc_dict = self._func_desc_to_dict(func_desc)
        
        # 保存到缓存
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(desc_dict, f, indent=2)
        
        return desc_dict
    
    def _func_desc_to_dict(self, func_desc) -> Dict:
        """转换函数描述为字典"""
        return {
            'name': func_desc.name,
            'parameters': [
                {
                    'name': p['name'],
                    'type': p['type'],
                    'direction': p['direction'],
                    'optional': p['optional']
                }
                for p in func_desc.parameters
            ]
        }
    
    def clear_cache(self):
        """清除缓存"""
        import shutil
        if os.path.exists(self.CACHE_DIR):
            shutil.rmtree(self.CACHE_DIR)
        os.makedirs(self.CACHE_DIR, exist_ok=True)

# 使用示例
cache = MetadataCache()
with get_sap_connection() as conn:
    desc = cache.get_function_desc(conn, 'RFC_READ_TABLE')
    print(f"函数名: {desc['name']}")
    print(f"参数数: {len(desc['parameters'])}")
```

#### 模式 5: 错误处理与重试

```python
# iflow/rfc/retry_handler.py
from pyrfc import Connection
from pyrfc._exception import CommunicationError, LogonError
import time
from functools import wraps
from typing import Callable, Any

class RetryHandler:
    """RFC 调用重试处理器"""
    
    def __init__(self, max_retries=3, delay=1, backoff=2):
        self.max_retries = max_retries
        self.delay = delay
        self.backoff = backoff
    
    def execute(self, func: Callable, *args, **kwargs) -> Any:
        """执行带重试的函数"""
        last_exception = None
        
        for attempt in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except CommunicationError as e:
                last_exception = e
                # 通信错误可以重试
                if attempt < self.max_retries - 1:
                    wait_time = self.delay * (self.backoff ** attempt)
                    print(f"通信错误，{wait_time}秒后重试...")
                    time.sleep(wait_time)
            except LogonError as e:
                # 登录错误不重试
                raise e
            except Exception as e:
                last_exception = e
                if attempt < self.max_retries - 1:
                    time.sleep(self.delay)
        
        raise last_exception

def with_retry(max_retries=3, delay=1):
    """装饰器：为 RFC 调用添加重试逻辑"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            handler = RetryHandler(max_retries, delay)
            return handler.execute(func, *args, **kwargs)
        return wrapper
    return decorator

# 使用示例
@with_retry(max_retries=3, delay=2)
def get_user_details(username: str):
    with get_sap_connection() as conn:
        return conn.call('BAPI_USER_GET_DETAIL', USERNAME=username)

# 调用
try:
    user_info = get_user_details('DEVELOPER')
except Exception as e:
    print(f"最终失败: {e}")
```

### iFlow 与 ADT 结合使用

```python
# iflow/adt_rfc_integration.py
from pyrfc import Connection
import xml.etree.ElementTree as ET

class ADTRFCIntegration:
    """ADT 与 RFC 集成"""
    
    def __init__(self, conn: Connection):
        self.conn = conn
    
    def get_object_source(self, object_type: str, object_name: str) -> str:
        """
        通过 RFC 获取对象源代码
        
        用于 ADT 无法直接访问的场景
        """
        if object_type == 'PROG':
            result = self.conn.call('RPY_PROGRAM_READ',
                                   PROGRAM_NAME=object_name)
            return '\n'.join(result.get('SOURCE', []))
        
        elif object_type == 'CLAS':
            result = self.conn.call('SEO_CLASS_GET_SOURCE',
                                   CLSKEY=object_name)
            return result.get('SOURCE', '')
        
        elif object_type == 'FUGR':
            result = self.conn.call('RPY_FUNCTIONMODULE_READ',
                                   FUNCTIONMODULE=object_name)
            return '\n'.join(result.get('SOURCE', []))
        
        else:
            raise ValueError(f"不支持的对象类型: {object_type}")
    
    def activate_object(self, object_type: str, object_name: str) -> bool:
        """激活对象"""
        result = self.conn.call('RS_TOOL_ACCESS',
                               OPERATION='ACTIVATE',
                               OBJECT_TYPE=object_type,
                               OBJECT_NAME=object_name)
        
        return result.get('RETURN_CODE') == 0

# 使用示例
with get_sap_connection() as conn:
    adt_rfc = ADTRFCIntegration(conn)
    
    # 获取程序源代码
    source = adt_rfc.get_object_source('PROG', 'ZTEST_PROGRAM')
    print(source)
    
    # 激活对象
    success = adt_rfc.activate_object('CLAS', 'ZCL_TEST_CLASS')
```

### iFlow 最佳实践

#### 1. 连接管理

```python
# 使用上下文管理器确保连接关闭
with get_sap_connection() as conn:
    # 执行操作
    pass

# 或使用 try-finally
conn = None
try:
    conn = get_sap_connection()
    # 执行操作
finally:
    if conn:
        conn.close()
```

#### 2. 参数验证

```python
def validate_rfc_params(func_name: str, params: dict):
    """验证 RFC 参数"""
    required_params = get_required_params(func_name)  # 从元数据获取
    
    missing = [p for p in required_params if p not in params]
    if missing:
        raise ValueError(f"缺少必需参数: {missing}")
    
    return True
```

#### 3. 日志记录

```python
import logging

logger = logging.getLogger('iflow.rfc')

def log_rfc_call(func_name: str, params: dict, result: dict):
    """记录 RFC 调用"""
    logger.info(f"RFC 调用: {func_name}")
    logger.debug(f"参数: {params}")
    logger.debug(f"结果: {result}")
```

#### 4. 性能监控

```python
import time
from contextlib import contextmanager

@contextmanager
def rfc_performance_monitor(func_name: str):
    """监控 RFC 调用性能"""
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"RFC {func_name} 耗时: {elapsed:.2f}秒")
```

### 故障排除

#### iFlow 常见问题

```python
# 问题 1: 连接超时
# 解决: 增加超时设置
conn = Connection(
    ashost='...',
    client='...',
    user='...',
    passwd='...',
    timeout=600  # 10分钟
)

# 问题 2: 字符编码错误
# 解决: 设置正确的代码页
conn = Connection(
    ashost='...',
    client='...',
    user='...',
    passwd='...',
    codepage='8400'  # 简体中文
)

# 问题 3: SSL 证书验证失败
# 解决: 开发环境可禁用验证
import os
os.environ['SAP_SSL_VERIFY'] = 'no'

# 或连接参数
conn = Connection(
    ashost='...',
    client='...',
    user='...',
    passwd='...',
    ssl_verify=False
)
```

---

> **注意**: 本文档基于 PyRFC 2.x/3.x 版本编写，具体 API 可能因版本而异。
> 建议始终参考官方最新文档。