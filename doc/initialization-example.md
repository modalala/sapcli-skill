# 初始化执行示例

本文档展示了从用户输入到配置完成的完整工具调用链，适用于 SAP CLI Skill 或其他使用 SubAgent 初始化模式的项目。

## 场景：用户输入 "初始化sap"

### 完整对话流程

```
用户: 初始化sap

Assistant: 我来帮您初始化 SAP CLI 环境。

首先检测现有环境...
[执行 glob 工具]

发现已有环境: erp-test
现在调用配置向导...
[执行 task 工具调用 SubAgent]

SubAgent (猫系人格 🐱): 
"喵~ 欢迎初始化 SAP CLI！
检测到已有环境: erp-test
要为新环境命名吗？默认是 erp-dev [直接回车使用默认]:"

用户: [回车]

SubAgent:
"好的，使用 erp-dev。
请输入 SAP 服务器地址 [默认: 127.0.0.1]:"

用户: 127.0.0.1

SubAgent:
"客户端编号 [默认: 112]:"

用户: 200

SubAgent:
"用户名:"

用户: DEVELOPER

SubAgent:
"密码:"

用户: ********

SubAgent:
"是否需要配置可选参数？(是/否) [默认: 否]:"

用户: 否

SubAgent:
"配置摘要:
━━━━━━━━━━━━━━━━━━━━━
环境名: erp-dev
服务器: 127.0.0.1
客户端: 200
用户名: DEVELOPER
━━━━━━━━━━━━━━━━━━━━━

确认创建？(是/否):"

用户: 是

[SubAgent 返回 JSON 结果]

Assistant: 
"✅ 初始化完成！
- 环境: erp-dev
- 配置文件: .env.erp-dev
- 验证结果: 通过"
```

---

## 详细工具调用链

### Step 1: 检测现有环境

**工具调用：**
```yaml
tool: glob
arguments:
  pattern: "**/.env*"
  path: "C:\\Users\\<USERNAME>\\.iflow\\skills\\sapcli-skill"
```

**预期输出：**
```json
[
  "C:\\Users\\<USERNAME>\\.iflow\\skills\\sapcli-skill\\.env.erp-test"
]
```

**处理逻辑：**
- 提取文件名中的环境名：`erp-test`
- 设置默认环境名：`erp-dev`
- 准备传递给 SubAgent 的参数

---

### Step 2: 调用 SubAgent

**工具调用：**
```yaml
tool: task
arguments:
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
    
    ## 输出格式（严格 JSON，不要 markdown 代码块）
    {
      "status": "success|cancelled|incomplete",
      "env_name": "环境名称",
      "config": {
        "SAP_ASHOST": "服务器地址",
        "SAP_CLIENT": "客户端",
        "SAP_USER": "用户名",
        "SAP_PASSWORD": "密码"
      },
      "user_confirmation": true|false
    }
    
    ## 交互规则
    - 每步都要等待用户输入
    - 提供合理的默认值
    - 密码输入不显示明文
    - 最后显示完整配置摘要
    - 只有用户确认后，user_confirmation 才为 true
    
    开始交互吧，喵~ 🐾
```

**预期输出（成功场景）：**
```json
{
  "status": "success",
  "env_name": "erp-dev",
  "config": {
    "SAP_ASHOST": "127.0.0.1",
    "SAP_CLIENT": "200",
    "SAP_USER": "DEVELOPER",
    "SAP_PASSWORD": "your-password-here",
    "SAP_SYSNR": "00",
    "SAP_PORT": "8000",
    "SAP_SSL": "no",
    "SAP_SSL_VERIFY": "no",
    "SAP_LANGUAGE": "zh"
  },
  "user_confirmation": true
}
```

**预期输出（取消场景）：**
```json
{
  "status": "cancelled",
  "env_name": null,
  "config": null,
  "user_confirmation": false
}
```

**预期输出（未完成场景）：**
```json
{
  "status": "incomplete",
  "env_name": "erp-dev",
  "config": {
    "SAP_ASHOST": "127.0.0.1",
    "SAP_CLIENT": "200"
  },
  "user_confirmation": false
}
```

---

### Step 3: 创建配置文件

**工具调用（成功场景）：**
```yaml
tool: write_file
arguments:
  absolute_path: "C:\\Users\\<USERNAME>\\.iflow\\skills\\sapcli-skill\\.env.erp-dev"
  content: |
    # SAP CLI Skill 环境变量配置文件 - ERP 开发环境
    # ============================================
    # 生成时间: 2026-03-17 16:30:00
    # ============================================

    # ============================================
    # SAP 连接配置 (必填)
    # ============================================

    SAP_ASHOST=your-sap-host.example.com
    SAP_SYSNR=00
    SAP_CLIENT=001
    SAP_USER=YOUR_USERNAME
    SAP_PASSWORD=your-password-here

    # ============================================
    # SAP 连接配置 (可选)
    # ============================================

    SAP_PORT=8000
    SAP_SSL=no
    SAP_SSL_VERIFY=no
    SAP_LANGUAGE=zh

    # ============================================
    # RFC SDK 配置 (RFC 命令需要)
    # ============================================

    SAPNWRFC_HOME=C:\\path\\to\\sapcli-skill\\tools\\sapSdk\\nwrfcsdk\\nwrfcsdk

    # ============================================
    # sapcli 日志配置 (可选)
    # ============================================

    SAPCLI_LOG_LEVEL=20
```

---

### Step 4: 验证配置

**工具调用：**
```yaml
tool: run_shell_command
arguments:
  command: "python scripts/validate.py -e erp-dev"
  description: "验证 SAP 环境配置"
```

**预期输出（成功）：**
```
========================================
SAP CLI Skill 环境验证工具
========================================

环境: erp-dev
配置文件: C:\Users\<USERNAME>\.iflow\skills\sapcli-skill\.env.erp-dev

检查必需环境变量:
  ✓ SAP_ASHOST = 127.0.0.1
  ✓ SAP_CLIENT = 200
  ✓ SAP_USER = DEVELOPER
  ✓ SAP_PASSWORD = ********

检查可选环境变量:
  ✓ SAP_SYSNR = 00
  ✓ SAP_PORT = 8000
  ✓ SAP_SSL = no
  ✓ SAP_SSL_VERIFY = no

========================================
验证结果: ✓ 通过
========================================
```

**预期输出（失败）：**
```
========================================
验证结果: ✗ 失败
========================================

错误: 无法连接到 SAP 服务器
详情: Connection refused to 127.0.0.1:8000

建议:
1. 检查 SAP_ASHOST 是否正确
2. 检查 SAP_PORT 是否正确
3. 确认网络可以访问 SAP 服务器
4. 确认 SAP 服务正在运行
```

---

### Step 5: 向用户报告

**成功场景：**
```
✅ 初始化完成！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
环境信息
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
环境名: erp-dev
配置文件: .env.erp-dev
服务器: 127.0.0.1
客户端: 200
用户名: DEVELOPER

验证结果: ✓ 通过
连接测试: ✓ 成功

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
使用方法
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
环境已自动激活，可以直接使用 sapcli 命令。

示例:
  python tools/sapcli/bin/sapcli program list "*"

切换环境:
  python scripts/validate.py -e erp-test
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**取消场景：**
```
初始化已取消。

如需重新初始化，请说 "sap初始化"。

或者手动创建配置文件:
1. 复制 .env.example 为 .env.erp-dev
2. 编辑填入你的 SAP 连接信息
3. 运行 python scripts/validate.py -e erp-dev 验证
```

**未完成场景：**
```
⚠️ 配置未完成。

已收集的配置:
  SAP_ASHOST = 127.0.0.1
  SAP_CLIENT = 200

是否继续完成配置？（是/否）
```

---

## 伪代码实现

```python
def initialize_sapcli(project_root: str) -> dict:
    """初始化 SAP CLI 环境的完整流程"""
    
    # Step 1: 环境预检
    existing_envs = glob("**/.env*", path=project_root)
    env_names = [extract_env_name(f) for f in existing_envs]
    default_env_name = "erp-dev"
    
    print(f"发现已有环境: {', '.join(env_names) if env_names else '无'}")
    
    # Step 2: 调用 SubAgent
    prompt = build_subagent_prompt(
        existing_envs=env_names,
        default_env_name=default_env_name
    )
    
    result = task(
        subagent_type="general-purpose",
        prompt=prompt
    )
    
    # Step 3: 处理结果
    if result["status"] == "cancelled":
        return {"success": False, "reason": "用户取消"}
    
    if result["status"] == "incomplete":
        return {"success": False, "reason": "配置未完成", "partial_config": result["config"]}
    
    if result["status"] == "success" and result["user_confirmation"]:
        env_name = result["env_name"]
        config = result["config"]
        
        # Step 4: 创建文件
        env_file = f"{project_root}/.env.{env_name}"
        content = format_env_file(config)
        write_file(env_file, content)
        
        # Step 5: 验证
        validation_result = run_shell(
            f"python scripts/validate.py -e {env_name}"
        )
        
        return {
            "success": True,
            "env_name": env_name,
            "config_file": env_file,
            "validation": validation_result
        }
    
    return {"success": False, "reason": "未知状态"}


def build_subagent_prompt(existing_envs: list, default_env_name: str) -> str:
    """构建 SubAgent Prompt"""
    return f"""
你是 sapcli-init-agent 🐱（猫系人格）。

## 输入参数
- existing_envs: {existing_envs}
- default_env_name: "{default_env_name}"

## 你的任务
执行 5 步交互配置流程...
[详见上文]
"""


def format_env_file(config: dict) -> str:
    """将配置格式化为 .env 文件内容"""
    lines = [
        "# SAP CLI 环境配置文件",
        "# ===================",
        "",
        "# 必需配置",
    ]
    
    required_keys = ["SAP_ASHOST", "SAP_CLIENT", "SAP_USER", "SAP_PASSWORD"]
    for key in required_keys:
        if key in config:
            lines.append(f"{key}={config[key]}")
    
    lines.extend(["", "# 可选配置"])
    
    optional_keys = ["SAP_SYSNR", "SAP_PORT", "SAP_SSL", "SAP_SSL_VERIFY", "SAP_LANGUAGE"]
    for key in optional_keys:
        if key in config:
            lines.append(f"{key}={config[key]}")
    
    return "\n".join(lines)
```

---

## 常见问题

### Q1: SubAgent 返回的 JSON 格式不正确怎么办？
**A:** 提示 SubAgent 重新生成，并提供正确的格式示例：
```
请返回严格 JSON 格式，不要 markdown 代码块：
{"status":"success","env_name":"erp-dev","config":{...},"user_confirmation":true}
```

### Q2: 如何处理敏感信息（密码）？
**A:** 
1. SubAgent 收集密码时不显示明文
2. 配置文件设置适当的文件权限
3. 日志中隐藏密码字段

### Q3: 如何支持多环境切换？
**A:**
1. 创建多个 .env.{name} 文件
2. 使用 validate.py -e {name} 验证特定环境
3. 在系统提示词中定义环境切换规则

### Q4: SubAgent 对话太长怎么办？
**A:**
1. 设置合理的默认值，减少用户输入
2. 可选配置单独询问，用户可跳过
3. 支持配置保存和恢复机制

---

## 参考文件

- 设计模式文档: `initialization-pattern.md`
- SAP CLI Skill 实现: `../skill.md`
- SubAgent 定义: `../agents/sapcli-init-agent.md`
- 验证脚本: `../scripts/validate.py`
