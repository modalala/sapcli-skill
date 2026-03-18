# SAP CLI Skill

[![Skill](https://img.shields.io/badge/Skill-Claude%20Code-blue)](https://claude.ai/code)
[![Protocol](https://img.shields.io/badge/Protocol-ADT%20%7C%20RFC%20%7C%20REST%20%7C%20OData-green)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**创造者：** miki

通过 AI Agent（如 Claude Code、iFlow CLI）调用 sapcli 工具管理 SAP 系统。

## 架构概览

```mermaid
graph TB
    subgraph "AI Agent"
        A[Claude Code / iFlow CLI]
    end
    
    subgraph "SAP CLI Skill"
        B[skill.md<br/>主Skill定义]
        C[33个子Skill]
        D["环境配置<br/>.env.{环境名}"]
    end
    
    subgraph "协议层"
        E[ADT Protocol<br/>HTTP/HTTPS]
        F[RFC Protocol<br/>需要SDK]
        G[REST API]
        H[OData]
    end
    
    subgraph "SAP系统"
        I[ABAP Objects]
        J[Data Dictionary]
        K[Transport System]
        L[RFC Functions]
    end
    
    A --> B
    B --> C
    C --> D
    C --> E
    C --> F
    C --> G
    C --> H
    E --> I
    E --> J
    E --> K
    F --> L
```

## 命令体系

```mermaid
mindmap
  root((SAP CLI<br/>33个命令))
    ADT核心对象[ADT核心对象 6个]
      program[program<br/>报表程序]
      include[include<br/>包含文件]
      functiongroup[functiongroup<br/>函数组]
      functionmodule[functionmodule<br/>函数模块]
      class[class<br/>ABAP类]
      interface[interface<br/>ABAP接口]
    ADT数据字典[ADT数据字典 6个]
      table[table<br/>透明表]
      structure[structure<br/>结构体]
      dataelement[dataelement<br/>数据元素]
      ddl[ddl<br/>CDS定义]
      dcl[dcl<br/>访问控制]
      bdef[bdef<br/>行为定义]
    ADT传输部署[ADT传输部署 5个]
      package[package<br/>开发包]
      cts[cts<br/>传输请求]
      checkout[checkout<br/>代码检出]
      checkin[checkin<br/>代码签入]
      activation[activation<br/>对象激活]
    ADT测试质量[ADT测试质量 2个]
      aunit[aunit<br/>单元测试]
      atc[atc<br/>代码检查]
    ADT高级功能[ADT高级功能 6个]
      abapgit[abapgit<br/>Git集成]
      rap[rap<br/>RAP服务]
      badi[badi<br/>增强管理]
      featuretoggle[featuretoggle<br/>功能开关]
      datapreview[datapreview<br/>数据预览]
      adt[adt<br/>元数据]
    RFC工具[RFC工具 3个]
      startrfc[startrfc<br/>执行RFC]
      strust[strust<br/>SSL证书]
      user[user<br/>用户管理]
    REST[REST 1个]
      gcts[gcts<br/>gCTS]
    OData[OData 2个]
      bsp[bsp<br/>BSP应用]
      flp[flp<br/>Fiori启动台]
```

## 功能概览

| 分类 | 数量 | 命令 |
|------|------|------|
| **ADT 核心对象** | 6 | program, include, functiongroup, functionmodule, class, interface |
| **ADT 数据字典** | 6 | table, structure, dataelement, ddl, dcl, bdef |
| **ADT 传输部署** | 5 | package, cts, checkout, checkin, activation |
| **ADT 测试质量** | 2 | aunit, atc |
| **ADT 高级功能** | 6 | abapgit, rap, badi, featuretoggle, datapreview, adt |
| **RFC 工具** | 3 | startrfc, strust, user |
| **REST 命令** | 1 | gcts |
| **OData 命令** | 2 | bsp, flp |

## 快速开始

### 1. 安装

```bash
cd E:\code
git clone <repository-url> sapcli-skill
cd sapcli-skill
```

### 2. 初始化配置

**方式一：交互式初始化（推荐）**

```bash
# 在 AI Agent 中输入
sap初始化
```

**方式二：手动配置**

```powershell
# 复制示例配置文件并修改
copy .env.example .env
notepad .env
```

### 3. 验证安装

```bash
python scripts/validate.py
```

### 4. 测试连接

```bash
python tools/sapcli/bin/sapcli --help
```

## 典型工作流程

### 开发工作流

```mermaid
sequenceDiagram
    participant Dev as 开发者
    participant Agent as AI Agent
    participant SAP as SAP系统
    
    Dev->>Agent: 创建程序 ZHELLO
    Agent->>SAP: program create
    SAP-->>Agent: 创建成功
    Agent-->>Dev: ✓ 程序已创建
    
    Dev->>Agent: 写入代码
    Agent->>SAP: program write
    SAP-->>Agent: 写入成功
    Agent-->>Dev: ✓ 代码已上传
    
    Dev->>Agent: 激活程序
    Agent->>SAP: program activate
    SAP-->>Agent: 激活成功
    Agent-->>Dev: ✓ 程序已激活
```

### 传输工作流

```mermaid
sequenceDiagram
    participant Dev as 开发者
    participant Agent as AI Agent
    participant SAP as SAP系统
    participant Git as Git仓库
    
    Dev->>Agent: 检出代码
    Agent->>SAP: checkout package=$TMP
    SAP-->>Agent: 返回源代码
    Agent->>Git: 保存到本地
    Agent-->>Dev: ✓ 检出完成
    
    Dev->>Git: 修改代码
    Dev->>Agent: 签入代码
    Agent->>SAP: checkin
    SAP-->>Agent: 签入成功
    Agent-->>Dev: ✓ 签入完成
    
    Dev->>Agent: 创建传输请求
    Agent->>SAP: cts create
    SAP-->>Agent: 请求号创建
    Agent-->>Dev: ✓ 请求号: DEVK9XXXXX
```

## 目录结构

```mermaid
graph TD
    A[sapcli-skill/] --> B[skill.md]
    A --> C[README.md]
    A --> D[".env.{环境名}"]
    A --> E[tools/]
    A --> F[skills/]
    A --> G[scripts/]
    A --> H[agents/]
    
    E --> E1[sapcli/]
    E --> E2[sapSdk/]
    
    F --> F1[adt-core/]
    F --> F2[adt-ddic/]
    F --> F3[adt-transport/]
    F --> F4[adt-test/]
    F --> F5[adt-advanced/]
    F --> F6[rfc/]
    F --> F7[rest/]
    F --> F8[odata/]
    
    F1 --> F1a[program/]
    F1 --> F1b[class/]
    F1 --> F1c[interface/]
    F1 --> F1d[include/]
    F1 --> F1e[functiongroup/]
    F1 --> F1f[functionmodule/]
    
    F2 --> F2a[table/]
    F2 --> F2b[structure/]
    F2 --> F2c[dataelement/]
    F2 --> F2d[ddl/]
    F2 --> F2e[dcl/]
    F2 --> F2f[bdef/]
    
    G --> G1[validate.py]
    G --> G2[generate_skills.py]
    
    H --> H1[sapcli-init-agent.md]
```

## 使用示例

### 创建 ABAP 程序

```bash
python tools/sapcli/bin/sapcli program create ZHELLO \
    --description "Hello World" \
    --package $TMP
```

### 读取程序代码

```bash
python tools/sapcli/bin/sapcli program read ZHELLO --save-to ./ZHELLO.abap
```

### 上传并激活

```bash
python tools/sapcli/bin/sapcli program write ZHELLO ./ZHELLO.abap --activate
```

### 执行 RFC 函数

```bash
# 需要配置 SAPNWRFC_HOME
python tools/sapcli/bin/sapcli startrfc STFC_CONNECTION '{"REQUTEXT":"Hello"}'
```

## 环境变量

### 必需变量

| 变量 | 说明 | 示例 |
|------|------|------|
| `SAP_ASHOST` | SAP 服务器地址 | `127.0.0.1` |
| `SAP_CLIENT` | 客户端编号 | `001` |
| `SAP_USER` | 用户名 | `DEVELOPER` |
| `SAP_PASSWORD` | 密码 | `your-password` |

### 可选变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `SAP_SYSNR` | 系统编号 | `00` |
| `SAP_PORT` | HTTP 端口 | `8000` |
| `SAP_SSL` | 使用 SSL | `no` |
| `SAP_SSL_VERIFY` | 验证 SSL 证书 | `no` |
| `SAP_LANGUAGE` | 登录语言 | `zh` |
| `SAPNWRFC_HOME` | RFC SDK 路径 | - |

### RFC 命令配置

如果使用 RFC 命令（startrfc, strust, user），需要额外配置：

```powershell
# 设置 RFC SDK 路径
$env:SAPNWRFC_HOME = "E:\code\sapcli-skill\tools\sapSdk\nwrfcsdk\nwrfcsdk"

# 添加到 PATH
$env:PATH = "$env:PATH;$env:SAPNWRFC_HOME\lib"

# 安装 PyRFC
pip install pynwrfc
```

## Skill 规范

本项目遵循 Claude Code Skill 规范：

- **主 Skill 文件**: `skill.md` - 包含所有工具定义和环境变量
- **子 Skill 文件**: `skills/<category>/<command>/skill.md` - 具体命令的详细定义
- **环境配置**: `.env.{环境名}` - 环境变量配置

### 多环境管理

```mermaid
graph LR
    A[AI Agent] --> B{选择环境}
    B --> C[.env.erp-dev]
    B --> D[.env.erp-test]
    B --> E[.env.erp-prod]
    B --> F[.env.crm-dev]
    C --> G[执行命令]
    D --> G
    E --> G
    F --> G
    G --> H[SAP系统]
```

### 在 Claude Code 中使用

1. 在 Claude Code 中加载此 Skill：
   ```
   /load skill E:\code\sapcli-skill\skill.md
   ```

2. 使用 Skill 管理 SAP：
   ```
   "创建程序 ZTEST001"
   "激活类 ZCL_HELLO"
   "运行 RFC STFC_CONNECTION"
   ```

### 在 iFlow CLI 中使用

将项目路径添加到 iFlow CLI 配置中：

```json
{
  "skills": [
    "E:\\code\\sapcli-skill"
  ]
}
```

## 协议说明

| 协议 | 命令数 | 通信方式 | 需要 SDK |
|------|--------|----------|----------|
| **ADT** | 26 | HTTP/HTTPS REST API | 否 |
| **RFC** | 3 | RFC 协议 | 是 (sapSdk + PyRFC) |
| **REST** | 1 | HTTP REST API | 否 |
| **OData** | 2 | OData 协议 | 否 |

```mermaid
graph LR
    subgraph "ADT Protocol"
        A1[26个命令] --> B1[HTTP/HTTPS]
        B1 --> C1[SAP ADT服务]
    end
    
    subgraph "RFC Protocol"
        A2[3个命令] --> B2[RFC协议]
        B2 --> C2[SAP网关]
    end
    
    subgraph "REST/OData"
        A3[3个命令] --> B3[HTTP REST]
        B3 --> C3[SAP Gateway]
    end
```

## 常见问题

### Q: 连接失败怎么办？

A: 检查以下几点：
1. SAP_ASHOST 是否正确
2. SAP_CLIENT 是否带前导零（如 `112` 不是 `001`）
3. 用户名和密码是否正确
4. SAP_SSL 设置是否与服务器匹配
5. 网络是否可达

### Q: RFC 命令报错 "sapnwrfc not found"？

A: 需要安装 PyRFC 并配置 SDK：
```bash
pip install pynwrfc
$env:SAPNWRFC_HOME = "E:\code\sapcli-skill\tools\sapSdk\nwrfcsdk\nwrfcsdk"
```

### Q: 如何查看详细日志？

A: 设置日志级别：
```powershell
$env:SAPCLI_LOG_LEVEL = 10  # DEBUG
```

## 贡献指南

1. Fork 项目
2. 创建分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 相关链接

- [SAP CLI 官方文档](doc/commands/)
- [PyRFC 文档](doc/pyrfc-reference.md)
- [SAP NW RFC SDK](https://support.sap.com/en/product/connectors/nwrfcsdk.html)

---

**维护者**: iFlow Agent  
**最后更新**: 2026-03-18