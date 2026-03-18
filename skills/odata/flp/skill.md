---
name: flp
version: 1.0.0
description: 管理 Fiori 启动台 (Launchpad)
parent: ../../../skill.md
tools:
- name: flp_manage
  description: 管理 Fiori 启动台 - manage 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
metadata:
  protocol: ADT
  category: OData 命令
  complexity: complex
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/flp.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Flp Skill

## 说明

管理 Fiori 启动台 (Launchpad)

## 使用场景

### 场景1: manage

**用户需求**: "执行 flp 的 manage"

**Skill 调用**:
```json
{
  "tool": "flp_manage",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| flp_manage | `sapcli flp manage <object_name>` |
