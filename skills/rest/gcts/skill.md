---
name: gcts
version: 1.0.0
description: Git 启用变更传输系统 (gCTS)
parent: ../../../skill.md
tools:
- name: gcts_repolist
  description: Git 启用变更传输系统 - repolist 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: gcts_clone
  description: Git 启用变更传输系统 - clone 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: gcts_checkout
  description: Git 启用变更传输系统 - checkout 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: gcts_log
  description: Git 启用变更传输系统 - log 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: gcts_pull
  description: Git 启用变更传输系统 - pull 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: gcts_commit
  description: Git 启用变更传输系统 - commit 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: gcts_delete
  description: Git 启用变更传输系统 - delete 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: gcts_config
  description: Git 启用变更传输系统 - config 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
metadata:
  protocol: ADT
  category: REST 命令
  complexity: complex
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/gcts.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Gcts Skill

## 说明

Git 启用变更传输系统 (gCTS)

## 使用场景

### 场景1: repolist

**用户需求**: "执行 gcts 的 repolist"

**Skill 调用**:
```json
{
  "tool": "gcts_repolist",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| gcts_repolist | `sapcli gcts repolist <object_name>` |
| gcts_clone | `sapcli gcts clone <object_name>` |
| gcts_checkout | `sapcli gcts checkout <object_name>` |
| gcts_log | `sapcli gcts log <object_name>` |
| gcts_pull | `sapcli gcts pull <object_name>` |
| gcts_commit | `sapcli gcts commit <object_name>` |
| gcts_delete | `sapcli gcts delete <object_name>` |
| gcts_config | `sapcli gcts config <object_name>` |
