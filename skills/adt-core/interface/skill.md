---
name: interface
version: 1.0.0
description: 管理 ABAP 接口 (Interfaces)
parent: ../../../skill.md
tools:
- name: interface_create
  description: 管理 ABAP 接口 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: interface_read
  description: 管理 ABAP 接口 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: interface_write
  description: 管理 ABAP 接口 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: interface_activate
  description: 管理 ABAP 接口 - activate 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
metadata:
  protocol: ADT
  category: 核心对象
  complexity: simple
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/interface.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Interface Skill

## 说明

管理 ABAP 接口 (Interfaces)

## 使用场景

### 场景1: create

**用户需求**: "执行 interface 的 create"

**Skill 调用**:
```json
{
  "tool": "interface_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| interface_create | `sapcli interface create <object_name>` |
| interface_read | `sapcli interface read <object_name>` |
| interface_write | `sapcli interface write <object_name>` |
| interface_activate | `sapcli interface activate <object_name>` |
