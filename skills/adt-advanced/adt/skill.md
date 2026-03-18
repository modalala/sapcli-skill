---
name: adt
version: 1.0.0
description: ADT 元数据操作
parent: ../../../skill.md
tools:
- name: adt_collections
  description: ADT 元数据操作 - collections 操作
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
  source_file: tools/sapcli/sap/cli/adt.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Adt Skill

## 说明

ADT 元数据操作

## 使用场景

### 场景1: collections

**用户需求**: "执行 adt 的 collections"

**Skill 调用**:
```json
{
  "tool": "adt_collections",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| adt_collections | `sapcli adt collections <object_name>` |
