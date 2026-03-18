---
name: atc
version: 1.0.0
description: 运行 ABAP 测试 Cockpit 代码检查
parent: ../../../skill.md
tools:
- name: atc_run
  description: 运行 ABAP 测试 Cockpit 代码检查 - run 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
metadata:
  protocol: ADT
  category: 测试质量
  complexity: medium
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/atc.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Atc Skill

## 说明

运行 ABAP 测试 Cockpit 代码检查

## 使用场景

### 场景1: run

**用户需求**: "执行 atc 的 run"

**Skill 调用**:
```json
{
  "tool": "atc_run",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| atc_run | `sapcli atc run <object_name>` |
