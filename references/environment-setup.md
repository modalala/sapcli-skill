# 环境配置详解

本文档详细说明 SAP CLI Skill 的环境配置。

---

## 1. 环境变量

### 1.1 必需变量

| 变量名 | 说明 | 示例 |
|--------|------|------|
| SAP_ASHOST | SAP 应用服务器地址 | `192.168.1.100` 或 `sap.example.com` |
| SAP_CLIENT | SAP 客户端编号 (3位数字) | `100`, `200`, `001` |
| SAP_USER | SAP 登录用户名 | `DEVELOPER` |
| SAP_PASSWORD | SAP 登录密码 | `your-password` |

### 1.2 可选变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| SAP_SYSNR | SAP 系统编号 | `00` |
| SAP_PORT | HTTP/HTTPS 端口 | `8000` |
| SAP_SSL | 是否使用 SSL | `no` |
| SAP_SSL_VERIFY | 是否验证 SSL 证书 | `no` |
| SAP_LANGUAGE | 登录语言 | `zh` |
| SAPNWRFC_HOME | SAP NW RFC SDK 路径 | - |
| SAPCLI_LOG_LEVEL | 日志级别 (10-50) | `20` |

---

## 2. 多环境配置

### 2.1 环境文件命名

```
.env.erp-dev      # ERP 开发环境
.env.erp-test     # ERP 测试环境
.env.erp-prod     # ERP 生产环境
.env.crm-dev      # CRM 开发环境
```

### 2.2 环境命名规范

- 只能包含：字母、数字、下划线、横线
- 建议格式：`{系统}-{环境类型}`
- 示例：`erp-dev`, `crm-test`, `srm-prod`

### 2.3 默认环境

默认使用 `erp-dev` 环境。如需指定其他环境：

```bash
python scripts/validate.py -e erp-test
```

---

## 3. RFC 功能配置

RFC 功能需要 SAP NW RFC SDK。

### 3.1 下载 SDK

从 SAP 官网下载 NW RFC SDK：
https://support.sap.com/en/product/connectors/nwrfcsdk.html

### 3.2 配置路径

```env
SAPNWRFC_HOME=E:\code\sapcli-skill\tools\sapSdk\nwrfcsdk\nwrfcsdk
```

### 3.3 验证 RFC

```bash
sapcli startrfc RFC_PING
```

---

## 4. SSL/TLS 配置

### 4.1 启用 SSL

```env
SAP_SSL=yes
SAP_PORT=44300
```

### 4.2 证书验证

生产环境建议启用证书验证：

```env
SAP_SSL_VERIFY=yes
```

### 4.3 证书管理

使用 `strust` 工具管理证书：

```bash
sapcli strust list
sapcli strust upload --pse SSL --file certificate.crt
```

---

## 5. 日志配置

### 5.1 日志级别

| 级别 | 值 | 说明 |
|------|-----|------|
| DEBUG | 10 | 详细调试信息 |
| INFO | 20 | 一般信息 |
| WARNING | 30 | 警告 |
| ERROR | 40 | 错误 |
| CRITICAL | 50 | 严重错误 |

### 5.2 启用调试日志

```env
SAPCLI_LOG_LEVEL=10
```

---

## 6. 配置验证

### 6.1 验证脚本

```bash
python scripts/validate.py -e erp-dev
```

### 6.2 检查项

- ✓ 环境变量是否设置
- ✓ SAP 服务器是否可达
- ✓ 用户认证是否成功
- ✓ RFC SDK 是否可用（如需要）

---

## 7. 故障排除

### 7.1 连接失败

检查项：
1. SAP_ASHOST 是否正确
2. 网络是否可达 (`ping <SAP_ASHOST>`)
3. SAP_SYSNR 是否正确
4. SAP_PORT 是否正确

### 7.2 认证失败

检查项：
1. SAP_USER 是否正确
2. SAP_PASSWORD 是否正确
3. SAP_CLIENT 是否正确
4. 用户是否被锁定

### 7.3 RFC 功能不可用

检查项：
1. SAPNWRFC_HOME 是否设置
2. SDK 文件是否存在
3. DLL/SO 文件权限是否正确