---
name: structure
version: 1.0.0
description: 管理结构体 (Structures)
parent: ../../../skill.md
tools:
- name: structure_create
  description: 管理结构体 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: structure_read
  description: 管理结构体 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: structure_write
  description: 管理结构体 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: structure_activate
  description: 管理结构体 - activate 操作
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
  source_file: tools/sapcli/sap/cli/structure.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Structure Skill

## 说明

管理结构体 (Structures)

## 使用场景

### 场景1: create

**用户需求**: "执行 structure 的 create"

**Skill 调用**:
```json
{
  "tool": "structure_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| structure_create | `sapcli structure create <object_name>` |
| structure_read | `sapcli structure read <object_name>` |
| structure_write | `sapcli structure write <object_name>` |
| structure_activate | `sapcli structure activate <object_name>` |
