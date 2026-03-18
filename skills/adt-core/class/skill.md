---
name: class
version: 1.0.0
description: 管理 ABAP 类，支持创建、读取、写入、激活类代码，以及查看类属性和执行类的主方法
parent: ../../../skill.md

tools:
  - name: class_create
    description: 创建新的 ABAP 类
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 类名（以 ZCL_ 或 YCL_ 开头）
        package:
          type: string
          description: 开发包名称
          default: "$TMP"
        description:
          type: string
          description: 类描述
        corrnr:
          type: string
          description: 传输请求号（可选）
      required: [object_name]

  - name: class_read
    description: 读取 ABAP 类代码
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 类名
        type:
          type: string
          enum: [main, definitions, implementations, testclasses]
          default: main
        save_to:
          type: string
          description: 保存到本地文件路径（可选）
      required: [object_name]

  - name: class_write
    description: 写入/更新 ABAP 类代码
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 类名
        type:
          type: string
          enum: [main, definitions, implementations, testclasses]
          default: main
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

  - name: class_activate
    description: 激活 ABAP 类
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 类名
      required: [object_name]

  - name: class_attributes
    description: 查看类属性
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 类名
      required: [object_name]

  - name: class_execute
    description: 执行类的主方法（需要实现 if_oo_adt_classrun~main）
    parameters:
      type: object
      properties:
        object_name:
          type: string
          description: 类名
      required: [object_name]

examples:
  - name: 创建类
    description: 创建一个新的 ABAP 类
    tool: class_create
    parameters:
      object_name: ZCL_TEST
      package: ZDEV
      description: 测试类

  - name: 读取类代码
    description: 下载类的主代码
    tool: class_read
    parameters:
      object_name: ZCL_TEST
      type: main
      save_to: ./zcl_test.clas.abap

  - name: 上传并激活
    description: 上传类代码并激活
    tool: class_write
    parameters:
      object_name: ZCL_TEST
      file_path: ./zcl_test.clas.abap
      activate: true

  - name: 查看属性
    description: 查看类的属性和元数据
    tool: class_attributes
    parameters:
      object_name: ZCL_TEST

  - name: 执行类
    description: 运行类的主方法
    tool: class_execute
    parameters:
      object_name: ZCL_TEST

error_handling:
  - code: OBJECT_NOT_FOUND
    description: 类不存在
    solution: 检查类名或先创建
  - code: EXECUTE_ERROR
    description: 执行失败
    solution: 确认类实现 if_oo_adt_classrun~main 方法
  - code: AUTHORIZATION_ERROR
    description: 权限不足
    solution: 确认 S_DEVELOP 权限

metadata:
  protocol: ADT
  category: 核心对象
  complexity: medium
  source_file: tools/sapcli/sap/cli/abapclass.py
  verified: yes
  verified_date: "2026-03-16"
---

# Class Skill

## 说明

管理 ABAP 类，支持完整的面向对象开发工作流。

## 使用场景

### 场景1: 创建类

**用户需求**: "创建类 ZCL_HELLO，描述'Hello World 类'"

**Skill 调用**:
```json
{
  "tool": "class_create",
  "parameters": {
    "object_name": "ZCL_HELLO",
    "package": "$TMP",
    "description": "Hello World 类"
  }
}
```

### 场景2: 读取类代码

**用户需求**: "下载 ZCL_HELLO 的主代码"

**Skill 调用**:
```json
{
  "tool": "class_read",
  "parameters": {
    "object_name": "ZCL_HELLO",
    "type": "main"
  }
}
```

### 场景3: 执行类

**用户需求**: "运行 ZCL_HELLO 类"

**Skill 调用**:
```json
{
  "tool": "class_execute",
  "parameters": {
    "object_name": "ZCL_HELLO"
  }
}
```

**注意**: execute 需类实现 `if_oo_adt_classrun~main` 方法

## 代码类型

| 类型 | 说明 | 文件后缀 |
|------|------|---------|
| main | 主代码 | .clas.abap |
| definitions | 定义部分 | .clas.locals_def.abap |
| implementations | 实现部分 | .clas.locals_imp.abap |
| testclasses | 测试类 | .clas.testclasses.abap |

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| class_create | `sapcli class create ZCL_TEST` |
| class_read | `sapcli class read ZCL_TEST --type main` |
| class_write | `sapcli class write ZCL_TEST ./code.abap` |
| class_activate | `sapcli class activate ZCL_TEST` |
| class_attributes | `sapcli class attributes ZCL_TEST` |
| class_execute | `sapcli class execute ZCL_TEST` |
