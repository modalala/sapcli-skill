---
name: strust
version: 1.0.0
description: SSL 证书管理 (信任管理器)
parent: ../../../skill.md
tools:
- name: strust_list
  description: SSL 证书管理 - list 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: strust_upload
  description: SSL 证书管理 - upload 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: strust_delete
  description: SSL 证书管理 - delete 操作
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
  complexity: complex
  requires_rfc: true
  source_file: tools/sapcli/sap/cli/strust.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Strust Skill

## 说明

SSL 证书管理 (信任管理器)

## 使用场景

### 场景1: list

**用户需求**: "执行 strust 的 list"

**Skill 调用**:
```json
{
  "tool": "strust_list",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| strust_list | `sapcli strust list <object_name>` |
| strust_upload | `sapcli strust upload <object_name>` |
| strust_delete | `sapcli strust delete <object_name>` |
