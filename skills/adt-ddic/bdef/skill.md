---
name: bdef
version: 1.0.0
description: 管理 CDS 行为定义 (Behavior Definitions)
parent: ../../../skill.md
tools:
- name: bdef_create
  description: 管理 CDS 行为定义 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: bdef_read
  description: 管理 CDS 行为定义 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: bdef_write
  description: 管理 CDS 行为定义 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: bdef_activate
  description: 管理 CDS 行为定义 - activate 操作
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
  source_file: tools/sapcli/sap/cli/bdef.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Bdef Skill

## 说明

管理 CDS 行为定义 (Behavior Definitions)

## 使用场景

### 场景1: create

**用户需求**: "执行 bdef 的 create"

**Skill 调用**:
```json
{
  "tool": "bdef_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| bdef_create | `sapcli bdef create <object_name>` |
| bdef_read | `sapcli bdef read <object_name>` |
| bdef_write | `sapcli bdef write <object_name>` |
| bdef_activate | `sapcli bdef activate <object_name>` |
