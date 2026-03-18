---
name: dcl
version: 1.0.0
description: 管理 CDS 访问控制定义 (Access Control)
parent: ../../../skill.md
tools:
- name: dcl_create
  description: 管理 CDS 访问控制定义 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: dcl_read
  description: 管理 CDS 访问控制定义 - read 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: dcl_write
  description: 管理 CDS 访问控制定义 - write 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: dcl_activate
  description: 管理 CDS 访问控制定义 - activate 操作
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
  source_file: tools/sapcli/sap/cli/dcl.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Dcl Skill

## 说明

管理 CDS 访问控制定义 (Access Control)

## 使用场景

### 场景1: create

**用户需求**: "执行 dcl 的 create"

**Skill 调用**:
```json
{
  "tool": "dcl_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| dcl_create | `sapcli dcl create <object_name>` |
| dcl_read | `sapcli dcl read <object_name>` |
| dcl_write | `sapcli dcl write <object_name>` |
| dcl_activate | `sapcli dcl activate <object_name>` |
