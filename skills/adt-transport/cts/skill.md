---
name: cts
version: 1.0.0
description: 管理变更传输系统 (Change Transport System)
parent: ../../../skill.md
tools:
- name: cts_list
  description: 管理变更传输系统 - list 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: cts_create
  description: 管理变更传输系统 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: cts_release
  description: 管理变更传输系统 - release 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
metadata:
  protocol: ADT
  category: 传输部署
  complexity: medium
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/cts.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Cts Skill

## 说明

管理变更传输系统 (Change Transport System)

## 使用场景

### 场景1: list

**用户需求**: "执行 cts 的 list"

**Skill 调用**:
```json
{
  "tool": "cts_list",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| cts_list | `sapcli cts list <object_name>` |
| cts_create | `sapcli cts create <object_name>` |
| cts_release | `sapcli cts release <object_name>` |
