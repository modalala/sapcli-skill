---
name: program
version: 1.0.0
description: 管理 ABAP 报表程序，支持创建、读取、写入、激活程序代码
parent: ../../../skill.md

tools:
  - name: program_create
    description: 创建新的 ABAP 报表程序
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 程序名称（1-30字符，以 Z 或 Y 开头）
        package:
          type: string
          description: 开发包名称
          default: "$TMP"
        description:
          type: string
          description: 程序描述
        corrnr:
          type: string
          description: 传输请求号（可选）
      required: [object_name]

  - name: program_read
    description: 读取 ABAP 报表程序源代码
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 程序名称
        save_to:
          type: string
          description: 保存到本地文件路径（可选）
      required: [object_name]

  - name: program_write
    description: 写入/更新 ABAP 报表程序源代码
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 程序名称
        file_path:
          type: string
          description: 源代码文件路径
        activate:
          type: boolean
          description: 是否立即激活
          default: false
        corrnr:
          type: string
          description: 传输请求号（可选）
      required: [object_name, file_path]

  - name: program_activate
    description: 激活 ABAP 报表程序
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 程序名称
      required: [object_name]

examples:
  - name: 创建程序
    description: 创建一个简单的 ABAP 程序
    tool: program_create
    parameters:
      object_name: ZTEST001
      package: ZDEV
      description: 测试程序

  - name: 读取程序代码
    description: 下载程序源代码到本地
    tool: program_read
    parameters:
      object_name: ZTEST001
      save_to: ./ZTEST001.abap

  - name: 上传并激活
    description: 上传修改后的代码并激活
    tool: program_write
    parameters:
      object_name: ZTEST001
      file_path: ./ZTEST001.abap
      activate: true

error_handling:
  - code: OBJECT_NOT_FOUND
    description: 程序不存在
    solution: 检查程序名称是否正确，或先创建程序
  - code: ACTIVATION_ERROR
    description: 激活失败
    solution: 检查代码语法错误
  - code: AUTHORIZATION_ERROR
    description: 权限不足
    solution: 确认用户有 S_DEVELOP 权限

metadata:
  protocol: ADT
  category: 核心对象
  complexity: simple
  source_file: tools/sapcli/sap/cli/program.py
  verified: yes
  verified_date: "2026-03-16"
---

# Program Skill

## 说明

管理 ABAP 报表程序，支持完整的开发生命周期：创建、读取、修改、激活。

## 使用场景

### 场景1: 创建新程序

**用户需求**: "创建一个叫做 ZHELLO_WORLD 的程序"

**Skill 调用**:
```json
{
  "tool": "program_create",
  "parameters": {
    "object_name": "ZHELLO_WORLD",
    "package": "$TMP",
    "description": "Hello World 程序"
  }
}
```

**执行流程**:
1. 调用 `sapcli program create` 创建程序框架
2. 返回创建成功信息

### 场景2: 下载程序代码

**用户需求**: "下载 ZHELLO_WORLD 程序到本地"

**Skill 调用**:
```json
{
  "tool": "program_read",
  "parameters": {
    "object_name": "ZHELLO_WORLD",
    "save_to": "./ZHELLO_WORLD.abap"
  }
}
```

### 场景3: 修改并激活程序

**用户需求**: "上传 ZHELLO_WORLD 的修改并激活"

**Skill 调用**:
```json
{
  "tool": "program_write",
  "parameters": {
    "object_name": "ZHELLO_WORLD",
    "file_path": "./ZHELLO_WORLD.abap",
    "activate": true
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| program_create | `sapcli program create ZHELLO_WORLD` |
| program_read | `sapcli program read ZHELLO_WORLD` |
| program_write | `sapcli program write ZHELLO_WORLD ./code.abap` |
| program_activate | `sapcli program activate ZHELLO_WORLD` |

## 注意事项

- 程序名必须以 Z 或 Y 开头（用户命名空间）
- 连接参数放在命令前面: `sapcli --ashost ... program create ...`
- 使用 `--no-ssl` 禁用 HTTPS
- 使用 `-v` 查看详细日志
