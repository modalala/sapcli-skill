# SAP CLI 渐进式操作手册

> 每次使用 sapcli 前，请先阅读此文档对应章节

---

## 📋 目录

1. [第一次使用（环境配置）](#第一次使用环境配置)
2. [日常快速开始](#日常快速开始)
3. [常用命令速查](#常用命令速查)
4. [进阶使用场景](#进阶使用场景)
5. [故障排除](#故障排除)

---

## 第一次使用（环境配置）

### 步骤 1: 确认配置文件存在

检查 `E:\code\sapcli\.env.sapcli` 文件是否存在：

```powershell
# PowerShell
Test-Path .env.sapcli
```

如果不存在，从示例文件复制：

```powershell
Copy-Item .env.sapcli.example .env.sapcli
```

### 步骤 2: 加载环境变量

**PowerShell 方式（推荐）:**

```powershell
Get-Content .env.sapcli | ForEach-Object { 
    if ($_ -match '^([^#][^=]*)=(.*)$') { 
        [Environment]::SetEnvironmentVariable($matches[1], $matches[2], 'Process') 
    } 
}
```

**CMD 方式:**

```cmd
for /f "tokens=1,2 delims==" %i in (.env.sapcli) do @set %i=%j
```

**验证加载成功:**

```powershell
$env:SAP_ASHOST
$env:SAP_USER
```

### 步骤 3: 测试连接

```bash
# 查看帮助
./sapcli --help

# 测试连接（列出包）
./sapcli package list
```

如果看到包列表，说明配置成功！

---

## 日常快速开始

### 每次开始工作前：

```powershell
# 1. 进入 sapcli 目录
cd E:\code\sapcli

# 2. 加载环境变量
Get-Content .env.sapcli | ForEach-Object { if ($_ -match '^([^#][^=]*)=(.*)$') { [Environment]::SetEnvironmentVariable($matches[1], $matches[2], 'Process') } }

# 3. 验证连接
./sapcli package list | Select-Object -First 5
```

---

## 常用命令速查

### 🔍 查询类命令

```bash
# 列出所有包
./sapcli package list

# 查看程序内容
./sapcli program read ZYOUR_PROGRAM

# 查看类内容
./sapcli class read ZCL_YOUR_CLASS

# 查看函数模块
./sapcli functionmodule read Z_YOUR_FUNCTION
```

### 📝 代码操作

```bash
# 读取程序到文件
./sapcli program read ZYOUR_PROGRAM > zyour_program.abap

# 从文件写入程序
./sapcli program write ZYOUR_PROGRAM zyour_program.abap --activate

# 激活对象
./sapcli program activate ZYOUR_PROGRAM

# 读取类
./sapcli class read ZCL_YOUR_CLASS > zcl_your_class.abap

# 写入类
./sapcli class write ZCL_YOUR_CLASS zcl_your_class.abap --activate
```

### 🧪 测试相关

```bash
# 运行 ABAP Unit 测试（类）
./sapcli aunit run class ZCL_YOUR_CLASS --output junit4

# 运行 ABAP Unit 测试（程序）
./sapcli aunit run program ZYOUR_PROGRAM --output junit4

# 运行 ABAP Unit 测试（包）
./sapcli aunit run package '$YOUR_PACKAGE' --output junit4
```

### 📦 包管理

```bash
# 创建包
./sapcli package create '$NEW_PACKAGE' 'Package Description'

# 查看包信息
./sapcli package read '$YOUR_PACKAGE'
```

### 🔧 其他常用

```bash
# ATC 代码检查
./sapcli atc run class ZCL_YOUR_CLASS

# 查看表数据预览
./sapcli datapreview table ZYOUR_TABLE

# 执行 RFC 函数
./sapcli startrfc Z_YOUR_RFC_FUNCTION
```

---

## 进阶使用场景

### 场景 1: 批量下载代码

```powershell
# 下载包内所有程序
$programs = ./sapcli program list --package '$YOUR_PACKAGE' | ConvertFrom-Json
foreach ($prog in $programs) {
    $name = $prog.name
    ./sapcli program read $name > "$name.abap"
    Write-Host "Downloaded: $name"
}
```

### 场景 2: Git 集成工作流

```bash
# 从 SAP 读取最新代码
./sapcli program read ZYOUR_PROGRAM > zyour_program.abap

# 提交到 Git
git add zyour_program.abap
git commit -m "Update from SAP"

# 修改代码后写回 SAP
./sapcli program write ZYOUR_PROGRAM zyour_program.abap --activate
```

### 场景 3: CI/CD 集成

```bash
# 在 CI 中运行所有测试
./sapcli aunit run package '$YOUR_PACKAGE' --output junit4 > test-results.xml

# 运行代码检查
./sapcli atc run package '$YOUR_PACKAGE' --output json > atc-results.json
```

---

## 🔧 配置参数详解

### 命令行参数

| 参数 | 环境变量 | 说明 | 默认值 |
|------|----------|------|--------|
| `--ashost` | `SAP_ASHOST` | SAP 应用服务器主机名或 IP | **必填** |
| `--port` | `SAP_PORT` | ADT 服务端口号 | 443 (SSL) / 80 (非 SSL) |
| `--client` | `SAP_CLIENT` | SAP 客户端编号 | **必填** |
| `--user` | `SAP_USER` | SAP 用户名 | **必填** |
| `--password` | `SAP_PASSWORD` | SAP 密码 | **必填** |
| `--sysnr` | `SAP_SYSNR` | 系统实例号 | 00 |
| `--no-ssl` | `SAP_SSL` | 禁用 SSL (值: no/false/off) | 启用 |
| `--skip-ssl-validation` | `SAP_SSL_VERIFY` | 跳过 SSL 证书验证 (值: no) | 验证 |
| `--corrnr` | `SAP_CORRNR` | 默认传输请求号 | - |

### 高级环境变量

```powershell
# 日志级别 (CRITICAL=50, ERROR=40, WARNING=30, INFO=20, DEBUG=10)
$env:SAPCLI_LOG_LEVEL = 10

# HTTP 请求超时时间（秒）
$env:SAPCLI_HTTP_TIMEOUT = 900

# SSL 服务器证书路径
$env:SAP_SSL_SERVER_CERT = "C:\certs\sap-server.crt"

# 临时密码（用于用户密码修改）
$env:SAPCLI_ABAP_USER_DUMMY_PASSWORD = "DummyPwd123!"
```

---

## 📚 完整命令参考

### 代码对象操作

| 命令 | 描述 | 文档 |
|------|------|------|
| `program` | 程序(Reports)操作 | [program.md](doc/commands/program.md) |
| `class` | 类操作 | [class.md](doc/commands/class.md) |
| `interface` | 接口操作 | [interface.md](doc/commands/interface.md) |
| `include` | 包含文件操作 | [include.md](doc/commands/include.md) |
| `functionmodule` | 函数模块操作 | [functionmodule.md](doc/commands/functionmodule.md) |
| `functiongroup` | 函数组操作 | [functiongroup.md](doc/commands/functiongroup.md) |

### CDS 和 RAP

| 命令 | 描述 | 文档 |
|------|------|------|
| `ddl` | CDS 数据定义 | [ddl.md](doc/commands/ddl.md) |
| `dcl` | CDS 访问控制 | [dcl.md](doc/commands/dcl.md) |
| `bdef` | 行为定义 | [bdef.md](doc/commands/bdef.md) |
| `businessservice` | RAP 业务服务 | [businessservice.md](doc/commands/businessservice.md) |

### DDIC 对象

| 命令 | 描述 | 文档 |
|------|------|------|
| `dataelement` | 数据元素 | [dataelement.md](doc/commands/dataelement.md) |
| `structure` | 结构体 | [structure.md](doc/commands/structure.md) |
| `table` | 透明表 | [table.md](doc/commands/table.md) |

### 开发管理

| 命令 | 描述 | 文档 |
|------|------|------|
| `package` | 包管理 | [package.md](doc/commands/package.md) |
| `cts` | 传输请求管理 | [cts.md](doc/commands/cts.md) |
| `gcts` | Git 启用 CTS | [gcts.md](doc/commands/gcts.md) |
| `abapgit` | abapGit 集成 | [abapgit.md](doc/commands/abapgit.md) |
| `checkout` | 代码检出 | [checkout.md](doc/commands/checkout.md) |
| `activation` | 对象激活 | [activation.md](doc/commands/activation.md) |

### 测试与质量

| 命令 | 描述 | 文档 |
|------|------|------|
| `aunit` | ABAP Unit 测试 | [aunit.md](doc/commands/aunit.md) |
| `atc` | ATC 代码检查 | [atc.md](doc/commands/atc.md) |

### 系统操作

| 命令 | 描述 | 文档 |
|------|------|------|
| `startrfc` | 执行 RFC 函数 | [startrfc.md](doc/commands/startrfc.md) |
| `datapreview` | 数据预览/SQL 查询 | [datapreview.md](doc/commands/datapreview.md) |
| `user` | 用户管理 | [user.md](doc/commands/user.md) |
| `bsp` | BSP 应用管理 | [bsp.md](doc/commands/bsp.md) |
| `flp` | Fiori Launchpad | [flp.md](doc/commands/flp.md) |
| `strust` | SSL 证书管理 | [strust.md](doc/commands/strust.md) |
| `badi` | BAdI 操作 | [badi.md](doc/commands/badi.md) |
| `featuretoggle` | 功能开关 | [featuretoggles.md](doc/commands/featuretoggles.md) |

---

## 🚀 进阶使用场景

### 场景 1: 批量下载代码

```powershell
# 下载包内所有程序
$programs = ./sapcli program list --package '$YOUR_PACKAGE' | ConvertFrom-Json
foreach ($prog in $programs) {
    $name = $prog.name
    ./sapcli program read $name > "$name.abap"
    Write-Host "Downloaded: $name"
}
```

### 场景 2: Git 集成工作流

```bash
# 从 SAP 读取最新代码
./sapcli program read ZYOUR_PROGRAM > zyour_program.abap

# 提交到 Git
git add zyour_program.abap
git commit -m "Update from SAP"

# 修改代码后写回 SAP
./sapcli program write ZYOUR_PROGRAM zyour_program.abap --activate
```

### 场景 3: CI/CD 集成

```bash
# 在 CI 中运行所有测试
./sapcli aunit run package '$YOUR_PACKAGE' --output junit4 > test-results.xml

# 运行代码检查
./sapcli atc run package '$YOUR_PACKAGE' --output json > atc-results.json
```

### 场景 4: 使用 gCTS

```bash
# 列出 gCTS 仓库
./sapcli gcts repolist

# 克隆仓库
./sapcli gcts clone https://github.com/user/repo.git $PACKAGE

# 切换分支
./sapcli gcts checkout $PACKAGE main

# 提交传输请求
./sapcli gcts commit $PACKAGE $CORRNR -m "Commit message"
```

### 场景 5: 使用 abapGit

```bash
# 链接包到远程仓库
./sapcli abapgit link $PACKAGE https://github.com/user/repo.git --branch main

# 拉取代码
./sapcli abapgit pull $PACKAGE
```

---

## 🧪 测试与代码质量

### ABAP Unit 测试

```bash
# 运行类的单元测试
./sapcli aunit run class ZCL_YOUR_CLASS --output human

# 运行包的单元测试并生成 JUnit 报告
./sapcli aunit run package '$YOUR_PACKAGE' --output junit4 > test-results.xml

# 运行测试并获取覆盖率报告
./sapcli aunit run class ZCL_YOUR_CLASS --result all --coverage-output jacoco --coverage-filepath coverage.xml
```

### ATC 代码检查

```bash
# 查看 ATC 配置
./sapcli atc customizing

# 运行代码检查
./sapcli atc run class ZCL_YOUR_CLASS --output human

# 使用特定检查变式
./sapcli atc run package '$YOUR_PACKAGE' -r MY_VARIANT --output checkstyle > atc-results.xml

# 列出 ATC 配置文件
./sapcli atc profile list
```

---

## 🔍 故障排除

### 问题 1: 连接超时

```
Error: Connection timeout
```

**解决:**
- 检查 `SAP_ASHOST` 和 `SAP_PORT` 是否正确
- 检查网络连接: `ping $env:SAP_ASHOST`
- 增加超时时间: `$env:SAPCLI_HTTP_TIMEOUT = 1800`

### 问题 2: 认证失败

```
Error: Authentication failed
```

**解决:**
- 确认用户名密码正确
- 检查 `SAP_CLIENT` 是否正确
- 检查用户是否被锁定
- 检查用户是否有 ADT 访问权限

### 问题 3: SSL 证书错误

```
Error: SSL certificate verify failed
```

**解决:**
- 开发环境: 设置 `$env:SAP_SSL_VERIFY = "no"`
- 生产环境: 导入正确的证书到系统 CA 存储
- 或者指定证书路径: `$env:SAP_SSL_SERVER_CERT = "path/to/cert.crt"`

### 问题 4: 对象不存在

```
Error: Object not found
```

**解决:**
- 确认对象名正确（注意大小写）
- 检查对象是否在正确的包中
- 使用 `list` 命令查看可用对象

### 问题 5: PyRFC 未安装

```
Error: startrfc command not available
```

**解决:**
- 安装 PyRFC: `pip install pynwrfc`
- 确保 SAP NW RFC SDK 已正确配置
- 参考: https://sap.github.io/PyRFC/

### 问题 6: 权限不足

```
Error: Authorization failed
```

**解决:**
- 确认用户有 S_ADT_AUTH 权限
- 确认用户有开发对象的相关权限
- 检查传输请求的所有权

### 调试模式

```bash
# 启用调试日志
$env:SAPCLI_LOG_LEVEL = 10
./sapcli program read ZYOUR_PROGRAM

# 查看详细 HTTP 通信
$env:SAPCLI_LOG_LEVEL = 0
./sapcli --help
```

---

## 💡 最佳实践

1. **总是先加载环境变量** - 避免重复输入连接信息
2. **使用 --output junit4** - 方便 CI 集成
3. **先读取再写入** - 避免意外覆盖
4. **使用版本控制** - 将 ABAP 代码纳入 Git 管理
5. **定期运行 AUnit** - 保持代码质量
6. **使用传输请求** - 所有修改都通过 CTS 管理
7. **启用 SSL 验证** - 生产环境不要跳过证书验证
8. **使用配置文件** - 将连接信息存储在 `.env.sapcli` 中

---

## 📖 更多文档

- **完整命令列表**: [doc/commands.md](doc/commands.md)
- **配置详细说明**: [doc/configuration.md](doc/configuration.md)
- **架构文档**: [doc/architecture.md](doc/architecture.md)
- **贡献指南**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **开发指南**: [HACKING.md](HACKING.md)

---

> 最后更新: 2026-03-03
> 配置环境: 开发环境 (SAP_ASHOST=your-sap-host:8000, CLIENT=000)
