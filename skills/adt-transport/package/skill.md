---
name: package
version: 1.0.0
description: 管理开发包 (Packages)
parent: ../../../skill.md
tools:
- name: package_create
  description: 管理开发包 - create 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: package_list
  description: 管理开发包 - list 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: package_stats
  description: 管理开发包 - stats 操作
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
  complexity: simple
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/package.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Package Skill

## 说明

管理开发包 (Packages)

## 使用场景

### 场景1: create

**用户需求**: "执行 package 的 create"

**Skill 调用**:
```json
{
  "tool": "package_create",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| package_create | `sapcli package create <object_name>` |
| package_list | `sapcli package list <object_name>` |
| package_stats | `sapcli package stats <object_name>` |
