---
name: checkin
version: 1.0.0
description: 从本地签入源代码到 SAP
parent: ../../../skill.md
tools:
- name: checkin_execute
  description: 从本地签入源代码到 SAP - execute 操作
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
  complexity: medium
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/checkin.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Checkin Skill

## 说明

从本地签入源代码到 SAP

## 使用场景

### 场景1: execute

**用户需求**: "执行 checkin 的 execute"

**Skill 调用**:
```json
{
  "tool": "checkin_execute",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| checkin_execute | `sapcli checkin execute <object_name>` |
