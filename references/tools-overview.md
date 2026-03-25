# 工具概览

本文档列出 SAP CLI Skill 支持的所有工具。

---

## 1. 工具分类

| 分类 | 数量 | 说明 |
|------|------|------|
| ADT 核心对象 | 6 | 程序、类、接口、函数等 |
| ADT 数据字典 | 6 | 表、结构、DDL、DCL 等 |
| ADT 传输部署 | 5 | 包、CTS、检出、签入等 |
| ADT 测试质量 | 2 | 单元测试、ATC |
| ADT 高级功能 | 6 | ABAPGit、RAP、BAdI 等 |
| RFC 工具 | 3 | RFC 函数、证书、用户 |
| REST/OData | 3 | gCTS、BSP、Fiori |

**总计**: 31 个工具

---

## 2. ADT 核心对象

### 2.1 program - 程序管理

| 子命令 | 说明 | 示例 |
|--------|------|------|
| create | 创建程序 | `sapcli program create ZPROGRAM` |
| read | 读取程序代码 | `sapcli program read ZPROGRAM` |
| write | 写入程序代码 | `sapcli program write ZPROGRAM file.abap` |
| activate | 激活程序 | `sapcli program activate ZPROGRAM` |

### 2.2 class - 类管理

| 子命令 | 说明 |
|--------|------|
| create | 创建类 |
| read | 读取类代码 |
| write | 写入类代码 |
| activate | 激活类 |
| attributes | 查看类属性 |
| execute | 执行类主方法 |

### 2.3 interface - 接口管理

| 子命令 | 说明 |
|--------|------|
| create | 创建接口 |
| read | 读取接口代码 |
| write | 写入接口代码 |
| activate | 激活接口 |

### 2.4 functiongroup - 函数组管理

| 子命令 | 说明 |
|--------|------|
| create | 创建函数组 |
| read | 读取函数组 |
| write | 写入函数组 |
| activate | 激活函数组 |

### 2.5 functionmodule - 函数模块管理

| 子命令 | 说明 |
|--------|------|
| create | 创建函数模块 |
| read | 读取函数模块 |
| write | 写入函数模块 |
| activate | 激活函数模块 |

### 2.6 include - 包含文件管理

| 子命令 | 说明 |
|--------|------|
| create | 创建包含文件 |
| read | 读取包含文件 |
| write | 写入包含文件 |
| activate | 激活包含文件 |

---

## 3. ADT 数据字典

### 3.1 table - 透明表管理

| 子命令 | 说明 |
|--------|------|
| create | 创建透明表 |
| read | 读取表定义 |
| write | 写入表定义 |
| activate | 激活表 |

### 3.2 structure - 结构体管理

| 子命令 | 说明 |
|--------|------|
| create | 创建结构体 |
| read | 读取结构体 |
| write | 写入结构体 |
| activate | 激活结构体 |

### 3.3 dataelement - 数据元素管理

| 子命令 | 说明 |
|--------|------|
| create | 创建数据元素 |
| read | 读取数据元素 |
| write | 写入数据元素 |
| activate | 激活数据元素 |

### 3.4 ddl - CDS 数据定义

| 子命令 | 说明 |
|--------|------|
| create | 创建 DDL |
| read | 读取 DDL |
| write | 写入 DDL |
| activate | 激活 DDL |

### 3.5 dcl - CDS 访问控制

| 子命令 | 说明 |
|--------|------|
| create | 创建 DCL |
| read | 读取 DCL |
| write | 写入 DCL |
| activate | 激活 DCL |

### 3.6 bdef - CDS 行为定义

| 子命令 | 说明 |
|--------|------|
| create | 创建 BDEF |
| read | 读取 BDEF |
| write | 写入 BDEF |
| activate | 激活 BDEF |

---

## 4. ADT 传输部署

### 4.1 package - 开发包管理

| 子命令 | 说明 |
|--------|------|
| create | 创建开发包 |
| list | 列出开发包 |
| stats | 开发包统计 |

### 4.2 cts - 变更传输系统

| 子命令 | 说明 |
|--------|------|
| list | 列出传输请求 |
| create | 创建传输请求 |
| release | 释放传输请求 |

### 4.3 checkout - 代码检出

从 SAP 检出源代码到本地。

### 4.4 checkin - 代码签入

从本地签入源代码到 SAP。

### 4.5 activation - 对象激活

批量激活对象。

---

## 5. ADT 测试质量

### 5.1 aunit - ABAP 单元测试

| 子命令 | 说明 |
|--------|------|
| run | 运行单元测试 |
| coverage | 测试覆盖率 |

### 5.2 atc - ABAP 测试 Cockpit

| 子命令 | 说明 |
|--------|------|
| run | 运行代码检查 |

---

## 6. ADT 高级功能

### 6.1 abapgit - ABAPGit 集成

| 子命令 | 说明 |
|--------|------|
| link | 关联仓库 |
| repo | 仓库管理 |

### 6.2 rap - RAP 业务服务

RAP 应用开发支持。

### 6.3 badi - BAdI 增强

| 子命令 | 说明 |
|--------|------|
| list | 列出 BAdI |
| activate | 激活 BAdI |
| deactivate | 停用 BAdI |

### 6.4 featuretoggle - 功能开关

管理功能开关。

### 6.5 datapreview - 数据预览

执行 OSQL 查询预览数据。

### 6.6 adt - ADT 元数据

| 子命令 | 说明 |
|--------|------|
| collections | 获取 ADT 集合 |

---

## 7. RFC 工具

### 7.1 startrfc - 执行 RFC 函数

执行任意 RFC 函数模块。

```bash
sapcli startrfc BAPI_USER_GET_DETAIL --param USER_NAME=DEVELOPER
```

### 7.2 strust - SSL 证书管理

| 子命令 | 说明 |
|--------|------|
| list | 列出证书 |
| upload | 上传证书 |
| delete | 删除证书 |

### 7.3 user - SAP 用户管理

| 子命令 | 说明 |
|--------|------|
| create | 创建用户 |
| read | 读取用户信息 |
| update | 更新用户 |
| delete | 删除用户 |

---

## 8. REST/OData

### 8.1 gcts - Git 变更传输

| 子命令 | 说明 |
|--------|------|
| repolist | 列出仓库 |
| clone | 克隆仓库 |
| checkout | 切换分支 |
| log | 查看日志 |
| pull | 拉取代码 |
| commit | 提交代码 |
| delete | 删除仓库 |
| config | 配置仓库 |

### 8.2 bsp - BSP 应用管理

| 子命令 | 说明 |
|--------|------|
| upload | 上传文件 |
| delete | 删除文件 |
| list | 列出文件 |

### 8.3 flp - Fiori 启动台

Fiori Launchpad 管理功能。

---

## 9. CLI 通用参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `--ashost` | 服务器地址 | `--ashost 192.168.1.100` |
| `--client` | 客户端 | `--client 100` |
| `--user` | 用户名 | `--user DEVELOPER` |
| `--password` | 密码 | `--password secret` |
| `--no-ssl` | 禁用 SSL | `--no-ssl` |
| `-v` | 详细输出 | `-v` |
| `--env` | 指定环境 | `--env erp-test` |