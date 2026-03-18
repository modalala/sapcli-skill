---
name: functionmodule
version: 1.0.0
description: 管理 ABAP 函数模块 (Function Modules)
parent: ../../../skill.md
tools:
- name: functionmodule_create
  description: 管理 ABAP 函数模块 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: functionmodule_read
  description: 管理 ABAP 函数模块 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: functionmodule_write
  description: 管理 ABAP 函数模块 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: functionmodule_activate
  description: 管理 ABAP 函数模块 - activate 操作
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
  source_file: tools/sapcli/sap/cli/functionmodule.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Functionmodule Skill

## 说明

管理 ABAP 函数模块 (Function Modules)

## 使用场景

### 场景1: create

**用户需求**: "执行 functionmodule 的 create"

**Skill 调用**:
```json
{
  "tool": "functionmodule_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| functionmodule_create | `sapcli functionmodule create <object_name>` |
| functionmodule_read | `sapcli functionmodule read <object_name>` |
| functionmodule_write | `sapcli functionmodule write <object_name>` |
| functionmodule_activate | `sapcli functionmodule activate <object_name>` |
