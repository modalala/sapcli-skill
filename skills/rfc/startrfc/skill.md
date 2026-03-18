---
name: startrfc
version: 1.0.0
description: 执行任意 RFC 函数模块，支持 JSON 参数传递、文件参数和 BAPI 返回结果检查
parent: ../../../skill.md

tools:
  - name: startrfc_execute
    description: 执行 RFC 函数模块
    parameters:
      type: object
      properties:
        function_name:
          type: string
          description: RFC 函数模块名称（如 STFC_CONNECTION）
        parameters:
          type: object
          description: RFC 输入参数（JSON 对象）
        output_format:
          type: string
          enum: [human, json]
          default: human
          description: 输出格式
        result_checker:
          type: string
          enum: [raw, bapi]
          default: raw
          description: 结果检查器类型
        response_file:
          type: string
          description: 保存完整响应的文件路径（可选）
      required: [function_name]

examples:
  - name: 测试连接
    description: 执行 STFC_CONNECTION 测试连接
    tool: startrfc_execute
    parameters:
      function_name: STFC_CONNECTION
      parameters:
        REQUTEXT: "Hello SAP"

  - name: 读取表数据
    description: 使用 RFC_READ_TABLE 读取表数据
    tool: startrfc_execute
    parameters:
      function_name: RFC_READ_TABLE
      parameters:
        QUERY_TABLE: "T001"
        FIELDS: ["BUKRS", "BUTXT"]
        ROWCOUNT: 10
      output_format: json

  - name: BAPI 调用
    description: 执行 BAPI 并检查结果
    tool: startrfc_execute
    parameters:
      function_name: BAPI_USER_GET_DETAIL
      parameters:
        USERNAME: "DEVELOPER"
      result_checker: bapi

error_handling:
  - code: RFC_COMMUNICATION_FAILURE
    description: RFC 通信失败
    solution: 检查 SAP 服务器地址和网络连接
  - code: RFC_INVALID_PARAMETER
    description: 参数无效
    solution: 检查参数名称和类型
  - code: RFC_ABAP_EXCEPTION
    description: ABAP 异常
    solution: 查看返回的异常信息
  - code: RFC_NOT_FOUND
    description: 函数模块不存在
    solution: 检查函数模块名称拼写

metadata:
  protocol: RFC
  category: RFC 工具
  complexity: medium
  requires_rfc: yes
  source_file: tools/sapcli/sap/cli/startrfc.py
  verified: yes
  verified_date: "2026-03-16"
---

# Startrfc Skill

## 说明

通过 RFC 协议直接调用 SAP 系统的函数模块。需要配置 SAPNWRFC_HOME 环境变量。

## 前置要求

1. 安装 PyRFC: `pip install pynwrfc`
2. 设置环境变量: `SAPNWRFC_HOME=E:\code\sapcli-skill\tools\sapSdk\nwrfcsdk\nwrfcsdk`
3. 将 `%SAPNWRFC_HOME%\lib` 添加到系统 PATH

## 使用场景

### 场景1: 测试连接

**用户需求**: "测试 SAP 连接"

**Skill 调用**:
```json
{
  "tool": "startrfc_execute",
  "parameters": {
    "function_name": "STFC_CONNECTION",
    "parameters": {
      "REQUTEXT": "Hello SAP"
    }
  }
}
```

### 场景2: 读取表数据

**用户需求**: "读取 T001 公司代码表的前10条"

**Skill 调用**:
```json
{
  "tool": "startrfc_execute",
  "parameters": {
    "function_name": "RFC_READ_TABLE",
    "parameters": {
      "QUERY_TABLE": "T001",
      "FIELDS": ["BUKRS", "BUTXT"],
      "ROWCOUNT": 10
    },
    "output_format": "json"
  }
}
```

### 场景3: 执行 BAPI

**用户需求**: "获取用户 DEVELOPER 的详细信息"

**Skill 调用**:
```json
{
  "tool": "startrfc_execute",
  "parameters": {
    "function_name": "BAPI_USER_GET_DETAIL",
    "parameters": {
      "USERNAME": "DEVELOPER"
    },
    "result_checker": "bapi"
  }
}
```

## 参数传递

### 简单参数
```json
{
  "function_name": "STFC_CONNECTION",
  "parameters": {
    "REQUTEXT": "Hello"
  }
}
```

### 结构参数
```json
{
  "parameters": {
    "COMPANYCODE": {
      "BUKRS": "1000",
      "BUTXT": "Company 1000"
    }
  }
}
```

### 表参数
```json
{
  "parameters": {
    "IT_DATA": [
      {"FIELD1": "value1", "FIELD2": "value2"},
      {"FIELD1": "value3", "FIELD2": "value4"}
    ]
  }
}
```

## CLI 命令对照

| Skill 调用 | CLI 命令 |
|-----------|---------|
| startrfc_execute (STFC_CONNECTION) | `sapcli startrfc STFC_CONNECTION '{"REQUTEXT":"Hello"}'` |
| startrfc_execute (JSON output) | `sapcli startrfc --output=json RFC_READ_TABLE '{...}'` |
| startrfc_execute (BAPI checker) | `sapcli startrfc --result-checker=bapi BAPI_USER_GET_DETAIL '{...}'` |

## 常用 RFC 函数

| 函数名 | 用途 |
|--------|------|
| STFC_CONNECTION | 测试连接 |
| RFC_READ_TABLE | 读取透明表 |
| RFC_GET_FUNCTION_INTERFACE | 获取函数接口 |
| BAPI_USER_GET_DETAIL | 获取用户详情 |
| BAPI_USER_CREATE | 创建用户 |
| BAPI_TRANSACTION_COMMIT | 提交事务 |
