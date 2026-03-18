# SubAgent 初始化模式设计文档

## 概述

本文档定义了 Skill → SubAgent → 文件创建的初始化架构，适用于需要通过交互式对话收集配置的场景。

这种模式的核心理念是：
- **主 Agent (skill.md)**: 负责编排流程、调用工具、执行文件操作
- **SubAgent (xxx-init-agent.md)**: 负责与用户进行多轮对话，收集配置信息
- **验证脚本**: 负责验证配置的有效性

## 架构图

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  User Input │────▶│   Main Agent     │────▶│   SubAgent      │
│ (初始化命令)│     │   (skill.md)     │     │ (-init-agent.md)│
└─────────────┘     └──────────────────┘     └─────────────────┘
                           │                           │
                           │ 2. 调用 task              │ 3. 多轮对话
                           │    (general-purpose)      │    收集配置
                           ▼                           ▼
                    ┌──────────────────┐     ┌─────────────────┐
                    │ 1. glob 检测环境 │     │ 返回 JSON 结果  │
                    └──────────────────┘     └─────────────────┘
                           │                           │
                           └──────────┬────────────────┘
                                      │
                                      ▼
                           ┌──────────────────┐
                           │ 4. write_file    │
                           │ 创建 .env 文件   │
                           └──────────────────┘
                                      │
                                      ▼
                           ┌──────────────────┐
                           │ 5. run_shell     │
                           │ 验证配置         │
                           └──────────────────┘
                                      │
                                      ▼
                           ┌──────────────────┐
                           │ 6. 报告结果      │
                           │ 给用户           │
                           └──────────────────┘
```

## 组件职责

| 组件 | 职责 | 输入 | 输出 |
|------|------|------|------|
| Main Agent | 编排流程、调用工具 | 用户初始化指令 | .env 文件 + 验证报告 |
| SubAgent | 交互对话、收集配置 | prompt 参数 (existing_envs, default_env_name) | JSON 格式配置 |
| validate.py | 验证配置有效性 | .env 文件路径 | 验证结果 |

## 工具调用链

### Step 1: 环境预检
```yaml
tool: glob
arguments:
  pattern: "**/.env*"
  path: "{{project_root}}"
output:
  - ".env.erp-test"
  - ".env.crm-dev"
```

### Step 2: 调用 SubAgent
```yaml
tool: task
arguments:
  subagent_type: "general-purpose"
  prompt: |
    你是 {{skill_name}}-init-agent。
    
    ## 输入参数
    - existing_envs: {{existing_envs}}
    - default_env_name: {{default_env_name}}
    
    ## 任务
    执行交互式配置收集流程，返回 JSON 格式结果。
    
    ## 输出格式
    {
      "status": "success|cancelled|incomplete",
      "env_name": "环境名",
      "config": { ... },
      "user_confirmation": true|false
    }
output: |
  {"status":"success","env_name":"erp-dev",...}
```

### Step 3: 创建配置文件
```yaml
tool: write_file
arguments:
  absolute_path: "{{project_root}}/.env.{{env_name}}"
  content: |
    # 配置文件内容
    KEY1=value1
    KEY2=value2
```

### Step 4: 验证配置
```yaml
tool: run_shell_command
arguments:
  command: "python scripts/validate.py -e {{env_name}}"
  description: "验证配置"
```

## JSON 契约

### SubAgent 输入参数
```json
{
  "existing_envs": ["erp-test", "crm-dev"],
  "default_env_name": "erp-dev"
}
```

### SubAgent 输出格式
```json
{
  "status": "success|cancelled|incomplete",
  "env_name": "erp-dev",
  "config": {
    "SAP_ASHOST": "127.0.0.1",
    "SAP_CLIENT": "112",
    "SAP_USER": "DEVELOPER",
    "SAP_PASSWORD": "password123"
  },
  "user_confirmation": true
}
```

#### 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| status | string | `success` - 完成配置，`cancelled` - 用户取消，`incomplete` - 未完成 |
| env_name | string | 环境名称，用于创建 .env.{env_name} 文件 |
| config | object | 配置键值对，将写入 .env 文件 |
| user_confirmation | boolean | 用户是否确认配置正确 |

## 在 skill.md 中的配置

### system_prompt 章节

```yaml
system_prompt: |
  ## 🚨 初始化规范（强制性）

  ### ❌ 严格禁止的行为
  - **禁止**直接运行任何脚本（setup_env.ps1、install.bat 等）
  - **禁止**直接创建 .env 文件而不经过 SubAgent 交互

  ### ✅ 推荐的正确流程
  1. **环境预检**: 使用 glob 查找现有环境
  2. **调用 SubAgent**: 使用 task 工具调用 general-purpose agent
  3. **接收结果**: 解析 JSON 格式的配置
  4. **创建文件**: 使用 write_file 创建 .env.{env_name}
  5. **验证配置**: 运行 validate.py 脚本

  ### 📞 SubAgent Prompt 模板
  ```
  你是 {{skill_name}}-init-agent 🐱。
  
  ## 输入参数
  - existing_envs: [{{existing_envs}}]
  - default_env_name: "{{default_env_name}}"
  
  ## 任务
  执行交互式配置收集流程...
  
  ## 输出格式（严格 JSON）
  { "status": "...", "env_name": "...", "config": {...}, "user_confirmation": ... }
  ```
```

### tools 章节

无需特殊工具定义，使用标准的 task、glob、write_file、run_shell_command 工具。

### skills 章节

如果需要，可以引用 SubAgent 定义：

```yaml
skills:
  - ./agents/{{skill_name}}-init-agent.md
```

## 错误处理

| 错误场景 | 处理方式 |
|----------|----------|
| SubAgent 返回格式错误 | 提示重新调用，提供正确的 JSON 格式示例 |
| validate.py 失败 | 显示错误详情，建议检查配置参数 |
| 连接测试失败 | 提示检查网络和 SAP 服务状态 |
| 用户取消 | 友好提示取消，提供重新初始化入口 |
| 配置未完成 | 询问是否继续完成配置 |

## 最佳实践

### 1. 多环境管理
支持同时管理多个环境，配置文件命名规则：`.env.{环境名}`

```
.env.erp-dev    # ERP 开发环境
.env.erp-test   # ERP 测试环境
.env.erp-prod   # ERP 生产环境
.env.crm-dev    # CRM 开发环境
```

### 2. 环境命名规范
- 只能包含：字母、数字、下划线、横线
- 推荐格式：`{system}-{env}`
- 示例：`erp-dev`, `crm-test`, `srm-prod`

### 3. 配置模板
在 `.env.example` 或文档中提供配置模板，包含：
- 所有必需配置项
- 常用可选配置项
- 配置项说明和示例值

### 4. 验证脚本
创建 `scripts/validate.py` 脚本，功能包括：
- 检查必需配置项是否存在
- 验证配置值格式
- 测试 SAP 连接
- 支持多环境验证（`-e {env_name}`）

## 与其他项目的集成

要在其他项目中使用此模式，需要：

1. **创建 skill.md** - 定义工具、环境变量、system_prompt
2. **创建 agents/{skill-name}-init-agent.md** - 定义 SubAgent
3. **创建 scripts/validate.py** - 验证脚本
4. **创建 .env.example** - 配置模板

参考示例见 `initialization-example.md`

## 参考资料

- 完整执行示例：见 `initialization-example.md`
- SAP CLI Skill 实现：`../skill.md`
- SubAgent 定义：`../agents/sapcli-init-agent.md`
