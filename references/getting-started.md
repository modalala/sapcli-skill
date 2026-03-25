# 快速开始指南

本文档帮助你快速上手 SAP CLI Skill。

---

## 1. 环境要求

- Python 3.8+
- SAP NW RFC SDK (仅 RFC 功能需要)
- SAP 系统访问权限

---

## 2. 初始化配置

### 方式一：交互式初始化

说 "sap初始化" 或 "初始化 SAP 环境"，系统会引导你完成配置。

### 方式二：手动创建配置文件

在 skill 根目录创建 `.env.erp-dev` 文件：

```env
# SAP 连接配置
SAP_ASHOST=your-sap-host.example.com
SAP_CLIENT=001
SAP_USER=YOUR_USERNAME
SAP_PASSWORD=your-password

# 可选配置
SAP_SYSNR=00
SAP_PORT=8000
SAP_SSL=no
SAP_SSL_VERIFY=no
SAP_LANGUAGE=zh
```

---

## 3. 验证连接

```bash
python scripts/validate.py -e erp-dev
```

成功输出：
```
✓ SAP 连接成功
✓ 环境变量配置正确
```

---

## 4. 第一个示例

### 4.1 创建程序

```
我想创建一个名为 ZHELLO_WORLD 的 SAP 程序
```

### 4.2 读取类代码

```
读取 ZCL_TEST 类的源代码
```

### 4.3 执行 RFC 函数

```
执行 RFC 函数 BAPI_USER_GET_DETAIL，参数 USER_NAME = "DEVELOPER"
```

---

## 5. 常用命令参考

| 任务 | CLI 命令 |
|------|----------|
| 创建程序 | `sapcli program create ZPROGRAM` |
| 读取程序 | `sapcli program read ZPROGRAM` |
| 创建类 | `sapcli class create ZCL_TEST` |
| 执行 RFC | `sapcli startrfc BAPI_USER_GET_DETAIL` |

---

## 6. 下一步

- 查看 `references/environment-setup.md` 了解详细配置
- 查看 `references/tools-overview.md` 了解所有工具
- 查看 `skills/` 目录下的子 skills 了解具体功能