---
name: checkout
version: 1.0.0
description: 从 SAP 检出源代码到本地
parent: ../../../skill.md
tools:
- name: checkout_execute
  description: 从 SAP 检出源代码到本地 - execute 操作
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
  source_file: tools/sapcli/sap/cli/checkout.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Checkout Skill

## 说明

从 SAP 检出源代码到本地

## 使用场景

### 场景1: execute

**用户需求**: "执行 checkout 的 execute"

**Skill 调用**:
```json
{
  "tool": "checkout_execute",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| checkout_execute | `sapcli checkout execute <object_name>` |
