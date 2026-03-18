---
name: table
version: 1.0.0
description: 管理透明表 (Transparent Tables)
parent: ../../../skill.md
tools:
- name: table_create
  description: 管理透明表 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: table_read
  description: 管理透明表 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: table_write
  description: 管理透明表 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: table_activate
  description: 管理透明表 - activate 操作
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
  complexity: medium
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/table.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Table Skill

## 说明

管理透明表 (Transparent Tables)

## 使用场景

### 场景1: create

**用户需求**: "执行 table 的 create"

**Skill 调用**:
```json
{
  "tool": "table_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| table_create | `sapcli table create <object_name>` |
| table_read | `sapcli table read <object_name>` |
| table_write | `sapcli table write <object_name>` |
| table_activate | `sapcli table activate <object_name>` |
