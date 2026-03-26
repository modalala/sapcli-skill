---
name: sapcli-skill
version: 1.0.1
description: |
  管理 SAP 系统和 ABAP 开发。创建程序、类、表，执行 RFC 函数，管理传输请求。
  当用户提到 SAP、ABAP、程序开发、CDS、RAP、传输请求、SAP 连接配置时使用此 skill。
  支持通过 sapcli 工具管理 SAP 系统的完整开发生命周期。
author: miki
license: MIT
---

# SAP CLI Skill

管理 SAP 系统和 ABAP 开发的 AI Agent 工具集。

## 快速开始

1. **初始化环境**: 运行 `sap初始化` 或说 "初始化 SAP 环境"
2. **验证连接**: `python scripts/validate.py`
3. **开始使用**: 参考 skills/ 目录下的子 skills

## 功能模块

| 模块 | 子 skills | 主要功能 |
|------|-----------|---------|
| ADT 核心对象 | 6 | program, class, interface, functiongroup, functionmodule, include |
| ADT 数据字典 | 6 | table, structure, dataelement, ddl, dcl, bdef |
| ADT 传输部署 | 5 | package, cts, checkout, checkin, activation |
| ADT 测试质量 | 2 | aunit, atc |
| ADT 高级功能 | 6 | abapgit, rap, badi, featuretoggle, datapreview, adt |
| RFC 工具 | 3 | startrfc, strust, user |
| REST/OData | 3 | gcts, bsp, flp |

**总计**: 31 个工具，详见 `references/tools-overview.md`

## 环境配置

详见 `references/environment-setup.md`

### 必需环境变量

- `SAP_ASHOST`: SAP 服务器地址
- `SAP_CLIENT`: 客户端编号 (3位数字)
- `SAP_USER`: 用户名
- `SAP_PASSWORD`: 密码

### 可选环境变量

- `SAP_SYSNR`: 系统编号 (默认: 00)
- `SAP_PORT`: HTTP 端口 (默认: 8000)
- `SAP_SSL`: 是否使用 SSL (默认: no)
- `SAP_LANGUAGE`: 登录语言 (默认: zh)
- `SAPNWRFC_HOME`: RFC SDK 路径 (RFC 功能需要)

## SAP 环境初始化

当用户说 "sap初始化"、"初始化 SAP 环境"、"配置 SAP 连接" 时执行：

### 流程

1. **检测现有环境**: 查找 `.env.*` 文件
2. **收集配置**: 使用 AskUserQuestion 一次性收集：
   - 环境名称 (默认: erp-dev)
   - SAP_ASHOST (服务器地址)
   - SAP_CLIENT (客户端)
   - SAP_USER (用户名)
   - SAP_PASSWORD (密码)
3. **创建配置文件**: 写入 `.env.{env_name}`
4. **验证连接**: 运行 `python scripts/validate.py -e {env_name}`

### 多环境支持

支持同时管理多个 SAP 环境：
- `.env.erp-dev` - ERP 开发环境
- `.env.erp-test` - ERP 测试环境
- `.env.erp-prod` - ERP 生产环境

## 常用操作

### 创建程序

```
sapcli program create ZPROGRAM --package $TMP
sapcli program write ZPROGRAM ./code.abap --activate
```

### 读取类代码

```
sapcli class read ZCL_TEST --type main
```

### 执行 RFC 函数

```
sapcli startrfc BAPI_USER_GET_DETAIL --param USER_NAME=DEVELOPER
```

### 管理传输请求

```
sapcli cts list
sapcli cts create --description "新功能开发"
```

## Windows 使用注意事项

### 编码问题

Windows 控制台默认使用 GBK 编码，必须设置 `PYTHONIOENCODING=utf-8` 以避免中文乱码。

### 运行 sapcli

sapcli 通过 Python 直接运行，需要设置 PYTHONPATH 和环境变量：

```bash
# 设置环境变量
PYTHONIOENCODING=utf-8
PYTHONPATH=/path/to/sapcli-skill/tools/sapcli
SAP_ASHOST=YourSapHost
SAP_CLIENT=112
SAP_USER=YourUsername
SAP_PASSWORD=YourPassword
SAP_PORT=8000
SAP_SSL=no

# 运行 sapcli
python /path/to/sapcli-skill/tools/sapcli/bin/sapcli program read ZSDR136
```

### 环境配置文件

配置文件位于 `.env.erp-dev`，包含 SAP 连接参数：

```ini
SAP_ASHOST=YourSapHost
SAP_CLIENT=112
SAP_USER=YourUsername
SAP_PASSWORD=YourPassword
SAP_PORT=8000
SAP_SSL=no
```

## 故障排除

详见 `references/troubleshooting.md`

### 常见问题

| 问题 | 解决方案 |
|------|----------|
| 连接失败 | 检查 SAP_ASHOST、SAP_PORT、网络连通性 |
| 认证失败 | 检查 SAP_USER、SAP_PASSWORD、SAP_CLIENT |
| RFC 不可用 | 检查 SAPNWRFC_HOME 是否正确设置 |
| 激活失败 | 检查语法错误，使用 atc run 检查代码 |

## 目录结构

```
sapcli-skill/
├── SKILL.md              # 本文件
├── references/           # 详细文档
│   ├── getting-started.md
│   ├── environment-setup.md
│   ├── tools-overview.md
│   └── troubleshooting.md
├── skills/               # 31 个子 skills
│   ├── adt-core/
│   ├── adt-ddic/
│   ├── adt-transport/
│   ├── adt-test/
│   ├── adt-advanced/
│   ├── rfc/
│   ├── rest/
│   └── odata/
├── agents/
│   └── sapcli-init-agent.md
├── scripts/
│   ├── validate.py
│   └── generate_skills.py
├── evals/
│   └── evals.json
└── tools/
    ├── sapcli/
    └── sapSdk/
```

## 相关文档

- 快速开始: `references/getting-started.md`
- 环境配置: `references/environment-setup.md`
- 工具参考: `references/tools-overview.md`
- 故障排除: `references/troubleshooting.md`