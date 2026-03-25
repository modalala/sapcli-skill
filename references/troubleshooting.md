# 故障排除

本文档提供 SAP CLI Skill 常见问题的解决方案。

---

## 1. 连接问题

### 1.1 无法连接到 SAP 服务器

**症状**: `Connection refused` 或 `Timeout`

**排查步骤**:
1. 检查 SAP_ASHOST 是否正确
   ```bash
   ping <SAP_ASHOST>
   ```
2. 检查 SAP_SYSNR 是否正确
3. 检查 SAP_PORT 是否正确
4. 检查防火墙设置

**解决方案**:
- 确保 SAP 服务器正在运行
- 确保网络可达
- 检查端口是否开放 (默认: 3200 + SYSNR)

### 1.2 SSL 连接失败

**症状**: `SSL handshake failed`

**排查步骤**:
1. 检查 SSL 设置
   ```env
   SAP_SSL=yes
   SAP_PORT=44300
   ```
2. 检查证书是否有效

**解决方案**:
- 开发环境可禁用 SSL 验证: `SAP_SSL_VERIFY=no`
- 生产环境需导入正确的证书

---

## 2. 认证问题

### 2.1 登录失败

**症状**: `Logon failed` 或 `Invalid credentials`

**排查步骤**:
1. 确认 SAP_USER 正确
2. 确认 SAP_PASSWORD 正确
3. 确认 SAP_CLIENT 正确
4. 检查用户是否被锁定

**解决方案**:
- 联系 SAP 管理员解锁账户
- 重置密码
- 确认客户端编号

### 2.2 权限不足

**症状**: `No authorization` 或 `Missing permission`

**常见权限对象**:
- S_DEVELOP: 开发权限
- S_TRANSPRT: 传输权限
- S_RFC: RFC 权限

**解决方案**:
- 联系 SAP 管理员分配相应权限
- 使用具有足够权限的用户账户

---

## 3. RFC 问题

### 3.1 RFC SDK 未找到

**症状**: `SAPNWRFC_HOME not set` 或 `RFC SDK not found`

**解决方案**:
1. 下载 SAP NW RFC SDK
2. 设置环境变量:
   ```env
   SAPNWRFC_HOME=E:\path\to\nwrfcsdk
   ```
3. 确保 DLL/SO 文件存在:
   - Windows: `nwrfcsdk\bin\*.dll`
   - Linux: `nwrfcsdk/lib/*.so`

### 3.2 RFC 函数执行失败

**症状**: `Function not found` 或 `RFC Error`

**排查步骤**:
1. 确认函数名称正确
2. 确认函数是 Remote-enabled
3. 检查参数格式

**解决方案**:
- 使用事务 SE37 验证函数是否存在
- 检查参数名称和类型

---

## 4. 对象操作问题

### 4.1 对象不存在

**症状**: `Object not found`

**排查步骤**:
1. 确认对象名称拼写正确
2. 确认对象类型正确
3. 确认对象在当前客户端

**解决方案**:
- 使用事务 SE80 或 SE93 搜索对象
- 检查传输请求是否已导入

### 4.2 激活失败

**症状**: `Activation failed`

**常见原因**:
- 语法错误
- 依赖对象未激活
- 命名冲突

**解决方案**:
1. 使用 ATC 检查代码:
   ```bash
   sapcli atc run <object_name>
   ```
2. 激活依赖对象
3. 检查语法错误

---

## 5. 传输问题

### 5.1 无法创建传输请求

**症状**: `Cannot create transport request`

**原因**:
- 无传输权限
- 未配置传输层
- 系统设置问题

**解决方案**:
- 检查 S_TRANSPRT 权限
- 联系传输管理员

### 5.2 传输请求无法释放

**症状**: `Cannot release transport`

**原因**:
- 请求不完整
- 对象锁定
- 权限问题

**解决方案**:
- 检查请求内容完整性
- 确保无对象被锁定
- 检查传输日志

---

## 6. 环境配置问题

### 6.1 环境变量未生效

**症状**: 配置了 .env 文件但变量未加载

**解决方案**:
1. 确认文件命名正确: `.env.erp-dev`
2. 确认文件格式正确 (无 BOM，UTF-8)
3. 使用 `--env` 参数指定环境:
   ```bash
   sapcli --env erp-test program read ZPROGRAM
   ```

### 6.2 多环境冲突

**症状**: 使用了错误的环境配置

**解决方案**:
- 明确指定环境: `--env erp-prod`
- 检查当前激活环境

---

## 7. 性能问题

### 7.1 命令执行缓慢

**可能原因**:
- 网络延迟
- SAP 系统负载高
- 大对象操作

**解决方案**:
- 使用 `-v` 参数查看详细日志
- 减少数据量
- 在非高峰时段执行

### 7.2 超时错误

**症状**: `Timeout` 或 `Connection lost`

**解决方案**:
- 增加超时时间:
  ```env
  SAPCLI_HTTP_TIMEOUT=900
  ```
- 检查网络稳定性

---

## 8. 日志与调试

### 8.1 启用调试日志

```env
SAPCLI_LOG_LEVEL=10
```

### 8.2 查看日志文件

日志文件位置: `~/.sapcli/logs/`

### 8.3 常用调试命令

```bash
# 详细模式
sapcli -v program read ZPROGRAM

# 指定环境
sapcli --env erp-dev --ashost 192.168.1.100 program read ZPROGRAM
```

---

## 9. 获取帮助

### 9.1 查看帮助

```bash
sapcli --help
sapcli program --help
sapcli program create --help
```

### 9.2 问题报告

如遇到未解决的问题，请提供以下信息：
- 错误信息完整输出
- 环境配置 (去除敏感信息)
- SAP 系统版本
- 操作系统版本