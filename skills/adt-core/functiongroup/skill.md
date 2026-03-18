---
name: functiongroup
version: 1.0.0
description: 管理 ABAP 函数组 (Function Groups)
parent: ../../../skill.md
tools:
- name: functiongroup_create
  description: 管理 ABAP 函数组 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: functiongroup_read
  description: 管理 ABAP 函数组 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: functiongroup_write
  description: 管理 ABAP 函数组 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: functiongroup_activate
  description: 管理 ABAP 函数组 - activate 操作
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
  complexity: medium
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/functiongroup.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Functiongroup Skill

## 说明

管理 ABAP 函数组 (Function Groups)

## 使用场景

### 场景1: create

**用户需求**: "执行 functiongroup 的 create"

**Skill 调用**:
```json
{
  "tool": "functiongroup_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| functiongroup_create | `sapcli functiongroup create <object_name>` |
| functiongroup_read | `sapcli functiongroup read <object_name>` |
| functiongroup_write | `sapcli functiongroup write <object_name>` |
| functiongroup_activate | `sapcli functiongroup activate <object_name>` |
