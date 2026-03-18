---
name: abapgit
version: 1.0.0
description: ABAPGit 集成管理
parent: ../../../skill.md
tools:
- name: abapgit_link
  description: ABAPGit 集成管理 - link 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: abapgit_repo
  description: ABAPGit 集成管理 - repo 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
metadata:
  protocol: ADT
  category: 高级功能
  complexity: complex
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/abapgit.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Abapgit Skill

## 说明

ABAPGit 集成管理

## 使用场景

### 场景1: link

**用户需求**: "执行 abapgit 的 link"

**Skill 调用**:
```json
{
  "tool": "abapgit_link",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| abapgit_link | `sapcli abapgit link <object_name>` |
| abapgit_repo | `sapcli abapgit repo <object_name>` |
