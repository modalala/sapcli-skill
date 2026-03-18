---
name: aunit
version: 1.0.0
description: 运行 ABAP 单元测试 (AUnit)
parent: ../../../skill.md
tools:
- name: aunit_run
  description: 运行 ABAP 单元测试 - run 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: aunit_coverage
  description: 运行 ABAP 单元测试 - coverage 操作
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
  source_file: tools/sapcli/sap/cli/aunit.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Aunit Skill

## 说明

运行 ABAP 单元测试 (AUnit)

## 使用场景

### 场景1: run

**用户需求**: "执行 aunit 的 run"

**Skill 调用**:
```json
{
  "tool": "aunit_run",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| aunit_run | `sapcli aunit run <object_name>` |
| aunit_coverage | `sapcli aunit coverage <object_name>` |
