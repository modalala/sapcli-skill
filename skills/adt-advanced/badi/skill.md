---
name: badi
version: 1.0.0
description: 管理 BAdI 增强 (Business Add-Ins)
parent: ../../../skill.md
tools:
- name: badi_list
  description: 管理 BAdI 增强 - list 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: badi_activate
  description: 管理 BAdI 增强 - activate 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: badi_deactivate
  description: 管理 BAdI 增强 - deactivate 操作
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
  complexity: medium
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/badi.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Badi Skill

## 说明

管理 BAdI 增强 (Business Add-Ins)

## 使用场景

### 场景1: list

**用户需求**: "执行 badi 的 list"

**Skill 调用**:
```json
{
  "tool": "badi_list",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| badi_list | `sapcli badi list <object_name>` |
| badi_activate | `sapcli badi activate <object_name>` |
| badi_deactivate | `sapcli badi deactivate <object_name>` |
