---
name: bsp
version: 1.0.0
description: 管理 BSP 应用 (Business Server Pages)
parent: ../../../skill.md
tools:
- name: bsp_upload
  description: 管理 BSP 应用 - upload 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: bsp_delete
  description: 管理 BSP 应用 - delete 操作
  parameters:
    type: object
    properties:
      object_name:
        type: string
        description: 对象名称
    required: []
- name: bsp_list
  description: 管理 BSP 应用 - list 操作
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
  complexity: medium
  requires_rfc: false
  source_file: tools/sapcli/sap/cli/bsp.py
  verified: 'yes'
  verified_date: '2026-03-16'
---

# Bsp Skill

## 说明

管理 BSP 应用 (Business Server Pages)

## 使用场景

### 场景1: upload

**用户需求**: "执行 bsp 的 upload"

**Skill 调用**:
```json
{
  "tool": "bsp_upload",
  "parameters": {
    "object_name": "EXAMPLE_OBJECT"
  }
}
```

## CLI 命令对照

| Skill 工具 | CLI 命令 |
|-----------|---------|
| bsp_upload | `sapcli bsp upload <object_name>` |
| bsp_delete | `sapcli bsp delete <object_name>` |
| bsp_list | `sapcli bsp list <object_name>` |
