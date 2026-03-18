---
name: user
version: 1.0.0
description: SAP 用户管理
parent: ../../../skill.md
tools:
- name: user_create
  description: SAP 用户管理 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: user_read
  description: SAP 用户管理 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: user_update
  description: SAP 用户管理 - update 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: user_delete
  description: SAP 用户管理 - delete 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
metadata:
  protocol: RFC
  category: RFC 工具
  complexity: medium
  requires_rfc: true
  source_file: tools/sapcli/sap/cli/user.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# User Skill

## 说明

SAP 用户管理

## 使用场景

### 场景1: create

**用户需求**: "执行 user 的 create"

**Skill 调用**:
```json
{
  "tool": "user_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| user_create | `sapcli user create <object_name>` |
| user_read | `sapcli user read <object_name>` |
| user_update | `sapcli user update <object_name>` |
| user_delete | `sapcli user delete <object_name>` |
