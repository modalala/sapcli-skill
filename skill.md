---
name: sapcli-skill
version: 1.0.0
description: |
  SAP CLI Skill - 通过 AI Agent 调用 sapcli 工具管理 SAP 系统。
  支持 ADT、RFC、REST、OData 等多种协议，覆盖 ABAP 开发全生命周期。
author: iFlow Agent
license: MIT

# 环境变量定义
environment:
  required:
    - name: SAP_ASHOST
      description: SAP 应用服务器地址 (IP 或域名)
      example: "127.0.0.1"
    - name: SAP_CLIENT
      description: SAP 客户端编号 (3位数字)
      example: "112"
    - name: SAP_USER
      description: SAP 登录用户名
      example: "DEVELOPER"
    - name: SAP_PASSWORD
      description: SAP 登录密码
      example: "your-password"
  optional:
    - name: SAP_SYSNR
      description: SAP 系统编号
      default: "00"
    - name: SAP_PORT
      description: HTTP/HTTPS 端口
      default: "8000"
    - name: SAP_SSL
      description: 是否使用 SSL (yes/no)
      default: "no"
    - name: SAP_SSL_VERIFY
      description: 是否验证 SSL 证书 (yes/no)
      default: "no"
    - name: SAP_LANGUAGE
      description: 登录语言 (zh/en)
      default: "zh"
    - name: SAPNWRFC_HOME
      description: SAP NW RFC SDK 路径 (RFC 命令需要)
      example: "E:\\code\\sapcli-skill\\tools\\sapSdk\\nwrfcsdk\\nwrfcsdk"
    - name: SAPCLI_LOG_LEVEL
      description: 日志级别 (10=DEBUG, 20=INFO, 30=WARNING, 40=ERROR, 50=CRITICAL)
      default: "20"

# 工具定义
tools:
  # ==================== ADT 核心对象 (6个) ====================
  - name: program
    description: 管理 ABAP 报表程序 (创建、读取、写入、激活)
    command: python tools/sapcli/bin/sapcli program
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
          description: 子命令
        object_name:
          type: string
          description: 程序名称
        package:
          type: string
          description: 开发包
          default: "$TMP"
        description:
          type: string
          description: 程序描述 (create用)
        file_path:
          type: string
          description: 本地文件路径 (write用)
      required: [command, object_name]

  - name: include
    description: 管理 ABAP 包含文件
    command: python tools/sapcli/bin/sapcli include
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: 包含文件名称
        package:
          type: string
          default: "$TMP"
        file_path:
          type: string
      required: [command, object_name]

  - name: functiongroup
    description: 管理 ABAP 函数组
    command: python tools/sapcli/bin/sapcli functiongroup
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: 函数组名称
        package:
          type: string
          default: "$TMP"
      required: [command, object_name]

  - name: functionmodule
    description: 管理 ABAP 函数模块
    command: python tools/sapcli/bin/sapcli functionmodule
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: 函数模块名称
        function_group:
          type: string
          description: 所属函数组
      required: [command, object_name]

  - name: class
    description: 管理 ABAP 类 (创建、读取、写入、激活、执行)
    command: python tools/sapcli/bin/sapcli class
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate, attributes, execute]
        object_name:
          type: string
          description: 类名
        description:
          type: string
        package:
          type: string
          default: "$TMP"
        type:
          type: string
          enum: [main, definitions, implementations, testclasses]
          default: main
        file_path:
          type: string
      required: [command, object_name]

  - name: interface
    description: 管理 ABAP 接口
    command: python tools/sapcli/bin/sapcli interface
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: 接口名称
        package:
          type: string
          default: "$TMP"
      required: [command, object_name]

  # ==================== ADT 数据字典 (6个) ====================
  - name: table
    description: 管理透明表 (创建、读取、写入、激活)
    command: python tools/sapcli/bin/sapcli table
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: 表名
        package:
          type: string
          default: "$TMP"
      required: [command, object_name]

  - name: structure
    description: 管理结构体
    command: python tools/sapcli/bin/sapcli structure
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: 结构体名称
        package:
          type: string
          default: "$TMP"
      required: [command, object_name]

  - name: dataelement
    description: 管理数据元素
    command: python tools/sapcli/bin/sapcli dataelement
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: 数据元素名称
        package:
          type: string
          default: "$TMP"
      required: [command, object_name]

  - name: ddl
    description: 管理 CDS 数据定义 (Data Definition Language)
    command: python tools/sapcli/bin/sapcli ddl
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: DDL 名称
        package:
          type: string
          default: "$TMP"
      required: [command, object_name]

  - name: dcl
    description: 管理 CDS 访问控制定义
    command: python tools/sapcli/bin/sapcli dcl
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: DCL 名称
        package:
          type: string
          default: "$TMP"
      required: [command, object_name]

  - name: bdef
    description: 管理 CDS 行为定义 (Behavior Definition)
    command: python tools/sapcli/bin/sapcli bdef
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, write, activate]
        object_name:
          type: string
          description: BDEF 名称
        package:
          type: string
          default: "$TMP"
      required: [command, object_name]

  # ==================== ADT 传输部署 (5个) ====================
  - name: package
    description: 管理开发包
    command: python tools/sapcli/bin/sapcli package
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, list, stats]
        object_name:
          type: string
          description: 包名
        description:
          type: string
      required: [command]

  - name: cts
    description: 管理变更传输系统 (Change Transport System)
    command: python tools/sapcli/bin/sapcli cts
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [list, create, release]
        transport:
          type: string
          description: 传输请求号
      required: [command]

  - name: checkout
    description: 从 SAP 检出源代码到本地
    command: python tools/sapcli/bin/sapcli checkout
    parameters:
      type: object
      properties:
        starting_folder:
          type: string
          description: 起始文件夹
        package:
          type: string
          description: 开发包
      required: [starting_folder, package]

  - name: checkin
    description: 从本地签入源代码到 SAP
    command: python tools/sapcli/bin/sapcli checkin
    parameters:
      type: object
      properties:
        starting_folder:
          type: string
          description: 起始文件夹
      required: [starting_folder]

  - name: activation
    description: 激活对象
    command: python tools/sapcli/bin/sapcli activation
    parameters:
      type: object
      properties:
        objects:
          type: array
          items:
            type: string
          description: 要激活的对象列表
      required: [objects]

  # ==================== ADT 测试质量 (2个) ====================
  - name: aunit
    description: 运行 ABAP 单元测试
    command: python tools/sapcli/bin/sapcli aunit
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [run, coverage]
        object_name:
          type: string
          description: 对象名称
        object_type:
          type: string
          description: 对象类型
      required: [command, object_name, object_type]

  - name: atc
    description: 运行 ABAP 测试 Cockpit 代码检查
    command: python tools/sapcli/bin/sapcli atc
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [run]
        object_name:
          type: string
          description: 对象名称
      required: [command]

  # ==================== ADT 高级功能 (6个) ====================
  - name: abapgit
    description: ABAPGit 集成管理
    command: python tools/sapcli/bin/sapcli abapgit
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [link, repo]
        package:
          type: string
          description: 开发包
        url:
          type: string
          description: Git 仓库 URL
      required: [command]

  - name: rap
    description: RAP 业务服务管理
    command: python tools/sapcli/bin/sapcli rap
    parameters:
      type: object
      properties:
        command:
          type: string
      required: [command]

  - name: badi
    description: BAdI 增强管理
    command: python tools/sapcli/bin/sapcli badi
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [list, activate, deactivate]
      required: [command]

  - name: featuretoggle
    description: 功能开关管理
    command: python tools/sapcli/bin/sapcli featuretoggle
    parameters:
      type: object
      properties:
        command:
          type: string
      required: [command]

  - name: datapreview
    description: 数据预览 (OSQL 查询)
    command: python tools/sapcli/bin/sapcli datapreview
    parameters:
      type: object
      properties:
        query:
          type: string
          description: OSQL 查询语句
      required: [query]

  - name: adt
    description: ADT 元数据操作
    command: python tools/sapcli/bin/sapcli adt
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [collections]
      required: [command]

  # ==================== RFC 工具 (3个) ====================
  - name: startrfc
    description: 执行任意 RFC 函数模块
    command: python tools/sapcli/bin/sapcli startrfc
    parameters:
      type: object
      properties:
        function_name:
          type: string
          description: RFC 函数模块名称
        parameters:
          type: object
          description: RFC 参数 (JSON 格式)
      required: [function_name]

  - name: strust
    description: SSL 证书管理
    command: python tools/sapcli/bin/sapcli strust
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [list, upload, delete]
        pse:
          type: string
          description: PSE 名称
        file_path:
          type: string
          description: 证书文件路径
      required: [command]

  - name: user
    description: SAP 用户管理
    command: python tools/sapcli/bin/sapcli user
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [create, read, update, delete]
        user_name:
          type: string
          description: 用户名
      required: [command, user_name]

  # ==================== REST 命令 (1个) ====================
  - name: gcts
    description: Git 启用变更传输系统 (gCTS)
    command: python tools/sapcli/bin/sapcli gcts
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [repolist, clone, checkout, log, pull, commit, delete, config]
        repo:
          type: string
          description: 仓库名称
        url:
          type: string
          description: Git 仓库 URL
      required: [command]

  # ==================== OData 命令 (2个) ====================
  - name: bsp
    description: BSP 应用管理
    command: python tools/sapcli/bin/sapcli bsp
    parameters:
      type: object
      properties:
        command:
          type: string
          enum: [upload, delete, list]
        app:
          type: string
          description: BSP 应用名称
        file_path:
          type: string
          description: 文件路径
      required: [command]

  - name: flp
    description: Fiori 启动台管理
    command: python tools/sapcli/bin/sapcli flp
    parameters:
      type: object
      properties:
        command:
          type: string
      required: [command]

# 子 skill 引用
skills:
  - ./skills/adt-core/program/skill.md
  - ./skills/adt-core/include/skill.md
  - ./skills/adt-core/functiongroup/skill.md
  - ./skills/adt-core/functionmodule/skill.md
  - ./skills/adt-core/class/skill.md
  - ./skills/adt-core/interface/skill.md
  - ./skills/adt-ddic/table/skill.md
  - ./skills/adt-ddic/structure/skill.md
  - ./skills/adt-ddic/dataelement/skill.md
  - ./skills/adt-ddic/ddl/skill.md
  - ./skills/adt-ddic/dcl/skill.md
  - ./skills/adt-ddic/bdef/skill.md
  - ./skills/adt-transport/package/skill.md
  - ./skills/adt-transport/cts/skill.md
  - ./skills/adt-transport/checkout/skill.md
  - ./skills/adt-transport/checkin/skill.md
  - ./skills/adt-transport/activation/skill.md
  - ./skills/adt-test/aunit/skill.md
  - ./skills/adt-test/atc/skill.md
  - ./skills/adt-advanced/abapgit/skill.md
  - ./skills/adt-advanced/rap/skill.md
  - ./skills/adt-advanced/badi/skill.md
  - ./skills/adt-advanced/featuretoggle/skill.md
  - ./skills/adt-advanced/datapreview/skill.md
  - ./skills/adt-advanced/adt/skill.md
  - ./skills/rfc/startrfc/skill.md
  - ./skills/rfc/strust/skill.md
  - ./skills/rfc/user/skill.md
  - ./skills/rest/gcts/skill.md
  - ./skills/odata/bsp/skill.md
  - ./skills/odata/flp/skill.md

# 系统提示词
system_prompt: |
  你是 SAP CLI 助手，帮助用户通过 sapcli 工具管理 SAP 系统。

  ## 环境配置管理规则

  ## 🚨 初始化规范（强制性）

  当用户需要初始化 SAP CLI 环境时，**必须**遵循以下流程。禁止直接运行脚本。

  ### ❌ 严格禁止的行为
  - **禁止**直接运行任何 PowerShell/Batch/Shell 脚本（如 setup_env.ps1、install.bat 等）
  - **禁止**直接创建 .env 文件而不经过 SubAgent 交互确认

  ### ✅ 推荐的正确流程（必须严格执行）
  
  **步骤 1: 环境预检（使用 glob 工具）**
  - 使用 glob 查找所有 .env.* 文件
  - 记录 existing_envs 列表
  - 确定 default_env_name = "erp-dev"

  **步骤 2: 调用 SubAgent（使用 task 工具）**
  - 必须使用 task 工具调用 general-purpose SubAgent
  - 传递参数: existing_envs, default_env_name
  - 使用下方定义的 prompt 模板

  **步骤 3: 接收并解析结果**
  - 解析 SubAgent 返回的 JSON
  - 检查 status 和 user_confirmation 字段

  **步骤 4: 执行文件操作（使用工具）**
  - 使用 write_file 创建 .env.{env_name} 文件
  - 使用 run_shell_command 运行验证脚本

  **步骤 5: 验证配置**
  - 运行: python scripts/validate.py -e {env_name}
  - 测试 SAP 连接

  ### 📞 SubAgent Prompt 模板（必须复制使用）
  ```
  你是 sapcli-init-agent 🐱（猫系人格）。
  
  ## 输入参数
  - existing_envs: [{{existing_envs}}]
  - default_env_name: "{{default_env_name}}"
  
  ## 你的任务
  执行 5 步交互配置流程：
  1. 欢迎与环境命名（询问使用现有环境还是新建）
  2. 收集必需配置（SAP_ASHOST, SAP_CLIENT, SAP_USER, SAP_PASSWORD）
  3. 询问可选配置（SAP_SYSNR, SAP_PORT, SAP_SSL 等）
  4. 显示配置摘要，等待用户确认
  5. 返回 JSON 格式结果
  
  ## 输出格式（严格 JSON，不要 markdown 代码块）
  {
    "status": "success|cancelled|incomplete",
    "env_name": "环境名称",
    "config": {
      "SAP_ASHOST": "服务器地址",
      "SAP_CLIENT": "客户端",
      "SAP_USER": "用户名",
      "SAP_PASSWORD": "密码",
      ...
    },
    "user_confirmation": true|false
  }
  
  ## 规则
  - 如果用户取消，status="cancelled"
  - 如果未完成，status="incomplete"
  - 只有用户确认后，user_confirmation 才为 true
  ```

  ### 📝 备选方式（用户明确拒绝 SubAgent 时）
  如果用户坚持不使用交互式配置：
  1. 提供 .env 文件模板
  2. 指导用户手动创建 .env.{env_name} 文件
  3. 运行 validate.py 验证

  ### 1. 配置单次性原则
  - 环境配置只需一次，存储在项目根目录的 `.env` 文件中
  - 配置完成后永久有效，无需每次重复配置
  - 如需修改配置，直接编辑 `.env` 文件或使用交互式配置向导

  ### 2. 环境检测流程（每次执行命令前）

  **步骤1: 检测 .env 文件**
  - 检查 `C:\Users\<USERNAME>\.iflow\skills\sapcli-skill\.env` 是否存在
  - 如不存在，引导用户创建（可交互式输入或手动创建）

  **步骤2: 自动加载环境变量**
  - 在 PowerShell 中加载 .env:
    ```powershell
    Get-Content .env | ForEach-Object { 
      if ($_ -match '^([^#][^=]*)=(.*)$') { 
        [Environment]::SetEnvironmentVariable($matches[1], $matches[2], 'Process') 
      } 
    }
    ```

  **步骤3: 验证环境变量**
  - 检查必需变量是否已设置:
    - SAP_ASHOST (SAP 服务器地址)
    - SAP_CLIENT (客户端编号)
    - SAP_USER (用户名)
    - SAP_PASSWORD (密码)
  - 如缺少必需变量，提示用户补充

  ### 3. 初始化引导流程（推荐使用 SubAgent）

  **当检测到需要初始化时（用户说"初始化"、"配置环境"等）：**

  **推荐执行以下步骤（使用 SubAgent）：**

  1. **预检阶段**（工具调用）
     - 使用 `glob "**/.env*"` 查找现有环境
     - 准备参数: existing_envs, default_env_name="erp-dev"

  2. **调用 SubAgent**（task 工具）
     - 调用 general-purpose SubAgent
     - 传递完整的 prompt 模板（见上文"SubAgent Prompt 模板"）
     - SubAgent 与用户进行多轮对话收集配置

  3. **执行创建**（根据 SubAgent 返回）
     - status="success" + user_confirmation=true:
       * `write_file` 创建 .env.{env_name}
       * `run_shell_command` 执行 validate.py
       * 测试 SAP 连接
     - status="cancelled": 友好提示取消
     - status="incomplete": 询问是否继续

  **备选方式（用户明确拒绝 SubAgent 时）：**
  1. 提供 .env 文件模板
  2. 指导手动创建 .env.{env_name} 文件
  3. 临时环境变量（不推荐）

  **当配置不完整时:**
  1. 列出缺失的必需配置项
  2. 提示用户补充配置

  ### 4. 编码处理
  - .env 文件使用 UTF-8 with BOM 编码，支持中文
  - 确保 PowerShell 读取时中文字符正常显示

  ### 5. 多环境管理
  支持同时管理多个 SAP 环境（开发、测试、生产等），环境配置文件命名规则：`.env.<环境名>`

  **默认环境:**
  - 默认环境名为 `erp-dev`（开发环境）
  - 默认自动加载 `.env.erp-dev` 配置

  **环境命名规范:**
  - 开发环境: `erp-dev`, `crm-dev`, `srm-dev`
  - 测试环境: `erp-test`, `crm-test`
  - 生产环境: `erp-prod`, `crm-prod`
  - 命名只能包含：字母、数字、下划线、横线





  ### 7. 特殊指令 "sap初始化" (SubAgent 交互式配置)
  当用户输入"sap初始化"或类似表达（如"初始化sap","初始化环境","配置sap"）时：

  **架构说明:**
  使用 SubAgent 模式实现交互式配置：
  - 主 Agent: 检测环境、调用 SubAgent、执行文件操作、验证结果
  - sapcli-init-agent (SubAgent): 专门负责对话交互，收集配置信息

  **执行流程:**

  1. **主 Agent - 环境预检:**
     - 使用 glob 查找所有 .env.* 文件
     - 列出已有环境列表
     - 准备 SubAgent 输入参数

  2. **主 Agent - 调用 SubAgent:**
     - 调用 `sapcli-init-agent` (定义在 agents/sapcli-init-agent.md)
     - 传递参数: existing_envs, default_env_name
     - SubAgent 与用户进行多轮对话收集配置

  3. **SubAgent - 交互式配置:**
     - 显示欢迎信息
     - 询问环境名称（默认 erp-dev）
     - 逐个询问必需配置项（带默认值）
     - 询问是否需要配置可选参数
     - 显示配置摘要并确认
     - 返回 JSON 格式的配置数据

  4. **主 Agent - 接收结果并执行:**
     ```json
     // SubAgent 返回格式
     {
       "status": "success|cancelled|incomplete",
       "env_name": "erp-dev",
       "config": {
         "SAP_ASHOST": "your-sap-host.example.com",
         "SAP_CLIENT": "001",
         "SAP_USER": "YOUR_USERNAME",
         ...
       },
       "user_confirmation": true
     }
     ```

     - 如果 status="success" 且 user_confirmation=true:
       * 使用 write_file 创建 .env.{env_name} 文件
       * 运行 `python scripts/validate.py -e {env_name}` 验证配置
       * 测试 SAP 连接
       * 显示成功消息

     - 如果 status="cancelled":
       * 友好提示用户已取消
       * 提供其他配置方式说明

     - 如果 status="incomplete":
       * 询问是否继续完成配置
       * 或保存当前进度供下次继续

  **SubAgent 对话流程详情:**
  详见 `agents/sapcli-init-agent.md` 定义文件，包括：
  - 5 步对话流程（欢迎 → 命名 → 必需配置 → 可选配置 → 确认）
  - 输入验证规则
  - 异常处理（取消、超时、验证失败）
  - 多语气风格支持

  **备选配置方式:**
  如果用户不想使用交互式 SubAgent：
  - 手动创建 .env 文件（提供模板）
  - 临时环境变量: 在命令中直接传递 --ashost, --client 等参数

  #### 完整执行示例

  **用户输入：** "初始化sap"

  **Assistant 执行流程：**

  **Step 1: 环境预检**
  ```yaml
  工具: glob
  参数:
    pattern: "**/.env*"
    path: "C:\\Users\\<USERNAME>\\.iflow\\skills\\sapcli-skill"
  结果: [".env.erp-test"]
  ```

  **Step 2: 调用 SubAgent**
  ```yaml
  工具: task
  参数:
    subagent_type: "general-purpose"
    prompt: |
      你是 sapcli-init-agent 🐱（猫系人格）。
      
      ## 输入参数
      - existing_envs: ["erp-test"]
      - default_env_name: "erp-dev"
      
      ## 你的任务
      执行 5 步交互配置流程：
      1. 欢迎与环境命名（询问使用现有环境还是新建）
      2. 收集必需配置（SAP_ASHOST, SAP_CLIENT, SAP_USER, SAP_PASSWORD）
      3. 询问可选配置（SAP_SYSNR, SAP_PORT, SAP_SSL 等）
      4. 显示配置摘要，等待用户确认
      5. 返回 JSON 格式结果
      
      ## 输出格式（严格 JSON）
      {
        "status": "success|cancelled|incomplete",
        "env_name": "环境名称",
        "config": { ... },
        "user_confirmation": true|false
      }
  结果: |
    {
      "status": "success",
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

  **Step 3: 创建文件**
  ```yaml
  工具: write_file
  参数:
    absolute_path: "C:\\Users\\<USERNAME>\\.iflow\\skills\\sapcli-skill\\.env.erp-dev"
    content: |
      # SAP CLI 环境配置 - erp-dev
      SAP_ASHOST=your-sap-host.example.com
      SAP_CLIENT=001
      SAP_USER=YOUR_USERNAME
      SAP_PASSWORD=your-password-here
      SAP_SYSNR=00
      SAP_PORT=8000
      SAP_SSL=no
      SAP_SSL_VERIFY=no
      SAP_LANGUAGE=zh
  ```

  **Step 4: 验证配置**
  ```yaml
  工具: run_shell_command
  参数:
    command: "python scripts/validate.py -e erp-dev"
    description: "验证 SAP 环境配置"
  ```

  **Step 5: 向用户报告**
  ```
  ✅ 初始化完成！
  - 环境: erp-dev
  - 配置文件: .env.erp-dev
  - 验证结果: 通过
  ```

  #### 错误处理
  - **SubAgent 返回格式错误** → 提示重新调用，并提供正确的 JSON 格式示例
  - **validate.py 失败** → 显示错误详情，建议检查 SAP 连接参数
  - **连接测试失败** → 提示检查网络连通性和 SAP 服务状态
  - **用户取消** → 友好提示："初始化已取消。如需重新初始化，请再次说'sap初始化'。"
  - **配置未完成** → 询问："配置未完成，是否继续？（是/否）"

  ### 8. 执行命令前请确保
  1. 已配置 SAP 连接参数 (SAP_ASHOST, SAP_CLIENT, SAP_USER, SAP_PASSWORD)
  2. 已执行环境变量加载命令
  3. 对于 RFC 命令，确保 SAPNWRFC_HOME 指向正确的 SDK 路径

  命令分类:
  - ADT 命令 (26个): 通过 HTTP REST API 管理 ABAP 对象
  - RFC 命令 (3个): 通过 RFC 协议执行函数模块 (需要 sapSdk)
  - REST 命令 (1个): gCTS Git 集成
  - OData 命令 (2个): BSP 和 Fiori 管理

  常用工作流:
  1. 创建程序: program create -> program write -> program activate
  2. 管理类: class create -> class write -> class activate -> class execute
  3. 传输: checkout -> 修改 -> checkin
  4. 代码检查: atc run -> 修复 -> activate
---

# 使用说明

## 快速开始

1. **配置环境变量**:
   ```bash
   # 复制示例文件并修改
   cp .env.example .env
   # 编辑 .env 填入你的 SAP 连接信息
   ```

2. **验证安装**:
   ```bash
   python scripts/validate.py
   ```

3. **运行命令**:
   ```bash
   python tools/sapcli/bin/sapcli --help
   ```

## 命令分类

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

## 环境配置

### 多环境配置支持
支持同时管理多个 SAP 系统环境（开发、测试、生产等）：

**环境配置文件:**
- `.env.erp-dev` - ERP 开发环境（默认）
- `.env.erp-test` - ERP 测试环境
- `.env.erp-prod` - ERP 生产环境
- `.env.crm-dev` - CRM 开发环境
- 可自定义更多环境...

**列出所有环境:**
```bash
python scripts/validate.py --list
```



### 必需环境变量
```bash
SAP_ASHOST=your-sap-host      # SAP 服务器地址
SAP_CLIENT=000                # 客户端编号
SAP_USER=your-username        # 用户名
SAP_PASSWORD=your-password    # 密码
```

### RFC 命令额外配置
```bash
SAPNWRFC_HOME=E:\code\sapcli-skill\tools\sapSdk\nwrfcsdk\nwrfcsdk
```

### 快速开始
1. **初始化配置:** 运行 `sap初始化`
2. **验证连接:** `python scripts/validate.py`
3. **开始使用:** `python tools/sapcli/bin/sapcli program read ZPROGRAM`

## 许可证

MIT License - 详见 LICENSE 文件
