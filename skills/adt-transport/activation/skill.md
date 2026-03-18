---
name: activation
version: 1.0.0
description: 激活 ABAP 对象
parent: ../../../skill.md
tools:
- name: activation_activate
  description: 激活 ABAP 对象 - activate 操作
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
  source_file: tools/sapcli/sap/cli/activation.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Activation Skill

## 说明

激活 ABAP 对象

## 使用场景

### 场景1: activate

**用户需求**: "执行 activation 的 activate"

**Skill 调用**:
```json
{
  "tool": "activation_activate",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| activation_activate | `sapcli activation activate <object_name>` |
