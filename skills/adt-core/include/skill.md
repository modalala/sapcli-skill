---
name: include
version: 1.0.0
description: 管理 ABAP 包含文件 (Include Programs)
parent: ../../../skill.md
tools:
- name: include_create
  description: 管理 ABAP 包含文件 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: include_read
  description: 管理 ABAP 包含文件 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: include_write
  description: 管理 ABAP 包含文件 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: include_activate
  description: 管理 ABAP 包含文件 - activate 操作
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
  source_file: tools/sapcli/sap/cli/include.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Include Skill

## 说明

管理 ABAP 包含文件 (Include Programs)

## 使用场景

### 场景1: create

**用户需求**: "执行 include 的 create"

**Skill 调用**:
```json
{
  "tool": "include_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| include_create | `sapcli include create <object_name>` |
| include_read | `sapcli include read <object_name>` |
| include_write | `sapcli include write <object_name>` |
| include_activate | `sapcli include activate <object_name>` |
