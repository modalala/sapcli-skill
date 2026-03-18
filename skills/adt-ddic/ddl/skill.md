---
name: ddl
version: 1.0.0
description: 管理 CDS 数据定义 (Data Definition Language)
parent: ../../../skill.md
tools:
- name: ddl_create
  description: 管理 CDS 数据定义 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: ddl_read
  description: 管理 CDS 数据定义 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: ddl_write
  description: 管理 CDS 数据定义 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: ddl_activate
  description: 管理 CDS 数据定义 - activate 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
metadata:
  protocol: ADT
  category: 数据字典
  complexity: complex
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/ddl.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Ddl Skill

## 说明

管理 CDS 数据定义 (Data Definition Language)

## 使用场景

### 场景1: create

**用户需求**: "执行 ddl 的 create"

**Skill 调用**:
```json
{
  "tool": "ddl_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| ddl_create | `sapcli ddl create <object_name>` |
| ddl_read | `sapcli ddl read <object_name>` |
| ddl_write | `sapcli ddl write <object_name>` |
| ddl_activate | `sapcli ddl activate <object_name>` |
