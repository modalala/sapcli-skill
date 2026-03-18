# SAP CLI 初始化对话记录

**日期:** 2026年3月17日  
**工作目录:** E:\code\plm\need-2

---

## 对话内容

### 用户请求
用户请求进行 sapcli 初始化配置。

### 执行过程

1. **启动 sapcli-skill**
   - 基础目录: `C:\Users\<USERNAME>\.iflow\skills\sapcli-skill`

2. **运行初始化脚本**
   ```powershell
   powershell scripts/setup_env.ps1
   ```

3. **初始化菜单选项**
   - List environments - 列出所有环境配置
   - Switch environment - 切换环境
   - Q. Quit - 退出

4. **现有环境检测**
   - 发现环境配置文件: `.env.erp-test` (ERP 测试环境)
   - 当前没有默认的 `.env` 文件（激活的配置）

### 当前状态

已检测到现有环境：
- `.env.erp-test` - ERP 测试环境配置已存在

**待完成的初始化操作：**

1. **使用现有 erp-test 环境** - 切换到已有的测试环境配置
2. **创建新环境** - 创建新的 SAP 环境配置（如 erp-dev、erp-prod 等）
3. **列出所有环境** - 查看已配置的环境列表
4. **验证连接** - 测试现有配置的连接

### 后续配置所需信息

如需完成配置，需要提供：
- SAP 服务器地址 (`SAP_ASHOST`)
- 客户端编号 (`SAP_CLIENT`)
- 用户名 (`SAP_USER`)
- 密码 (`SAP_PASSWORD`)

---

## 常用命令参考

### 验证安装
```bash
python scripts/validate.py
```

### 运行命令
```bash
python tools/sapcli/bin/sapcli --help
```

### 环境切换
```bash
# 交互式切换
powershell scripts/setup_env.ps1

# 命令行快速切换
powershell scripts/setup_env.ps1 -SwitchEnv erp-test

# 验证指定环境（不切换）
python scripts/validate.py -e erp-test
```

### 列出所有环境
```bash
python scripts/validate.py --list
```

---

## 命令分类概览

### 1. ADT 核心对象管理 (6个)
- `program` - 报表程序管理
- `include` - 包含文件管理
- `functiongroup` - 函数组管理
- `functionmodule` - 函数模块管理
- `class` - ABAP 类管理
- `interface` - ABAP 接口管理

### 2. ADT 数据字典 (6个)
- `table` - 透明表管理
- `structure` - 结构体管理
- `dataelement` - 数据元素管理
- `ddl` - CDS 数据定义
- `dcl` - CDS 访问控制
- `bdef` - CDS 行为定义

### 3. ADT 传输部署 (5个)
- `package` - 开发包管理
- `cts` - 变更传输系统
- `checkout` - 代码检出
- `checkin` - 代码签入
- `activation` - 对象激活

### 4. ADT 测试质量 (2个)
- `aunit` - ABAP 单元测试
- `atc` - ABAP 测试 Cockpit

### 5. ADT 高级功能 (6个)
- `abapgit` - ABAPGit 集成
- `rap` - RAP 业务服务
- `badi` - BAdI 增强
- `featuretoggle` - 功能开关
- `datapreview` - 数据预览
- `adt` - ADT 元数据

### 6. RFC 工具 (需要 sapSdk)
- `startrfc` - 执行 RFC 函数
- `strust` - SSL 证书管理
- `user` - 用户管理

### 7. REST/OData
- `gcts` - Git 变更传输
- `bsp` - BSP 应用管理
- `flp` - Fiori 启动台
