---
name: dataelement
version: 1.0.0
description: 管理数据元素 (Data Elements)
parent: ../../../skill.md
tools:
- name: dataelement_create
  description: 管理数据元素 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: dataelement_read
  description: 管理数据元素 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: dataelement_write
  description: 管理数据元素 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: dataelement_activate
  description: 管理数据元素 - activate 操作
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
  complexity: simple
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/dataelement.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Dataelement Skill

## 说明

管理数据元素 (Data Elements)

## 使用场景

### 场景1: create

**用户需求**: "执行 dataelement 的 create"

**Skill 调用**:
```json
{
  "tool": "dataelement_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| dataelement_create | `sapcli dataelement create <object_name>` |
| dataelement_read | `sapcli dataelement read <object_name>` |
| dataelement_write | `sapcli dataelement write <object_name>` |
| dataelement_activate | `sapcli dataelement activate <object_name>` |
