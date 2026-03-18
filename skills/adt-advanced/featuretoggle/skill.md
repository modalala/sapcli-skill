---
name: featuretoggle
version: 1.0.0
description: 管理功能开关 (Feature Toggles)
parent: ../../../skill.md
tools:
- name: featuretoggle_list
  description: 管理功能开关 - list 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: featuretoggle_enable
  description: 管理功能开关 - enable 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: featuretoggle_disable
  description: 管理功能开关 - disable 操作
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
  source_file: tools/sapcli/sap/cli/featuretoggle.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Featuretoggle Skill

## 说明

管理功能开关 (Feature Toggles)

## 使用场景

### 场景1: list

**用户需求**: "执行 featuretoggle 的 list"

**Skill 调用**:
```json
{
  "tool": "featuretoggle_list",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| featuretoggle_list | `sapcli featuretoggle list <object_name>` |
| featuretoggle_enable | `sapcli featuretoggle enable <object_name>` |
| featuretoggle_disable | `sapcli featuretoggle disable <object_name>` |
