---
name: datapreview
version: 1.0.0
description: 数据预览 - 执行 OSQL 查询
parent: ../../../skill.md
tools:
- name: datapreview_query
  description: 数据预览 - 执行 OSQL 查询 - query 操作
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
  complexity: simple
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/datapreview.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Datapreview Skill

## 说明

数据预览 - 执行 OSQL 查询

## 使用场景

### 场景1: query

**用户需求**: "执行 datapreview 的 query"

**Skill 调用**:
```json
{
  "tool": "datapreview_query",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| datapreview_query | `sapcli datapreview query <object_name>` |
