---
name: rap
version: 1.0.0
description: RAP 业务服务管理 (RESTful Application Programming)
parent: ../../../skill.md
tools:
- name: rap_manage
  description: RAP 业务服务管理 - manage 操作
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
  source_file: tools/sapcli/sap/cli/rap.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Rap Skill

## 说明

RAP 业务服务管理 (RESTful Application Programming)

## 使用场景

### 场景1: manage

**用户需求**: "执行 rap 的 manage"

**Skill 调用**:
```json
{
  "tool": "rap_manage",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| rap_manage | `sapcli rap manage <object_name>` |
