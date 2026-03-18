# SAP CLI Skill

**路径**: `E:\code\sapcli-skill\skill.md`

这是 iFlow CLI 的 skill 引用文件，实际配置请查看主 skill.md 文件。

## 快速链接

- [主 Skill 文件](../skill.md)
- [README](../README.md)
- [验证脚本](../scripts/validate.py)

## 支持的命令

- ADT 命令 (26个): program, class, include, functiongroup, functionmodule, interface, table, structure, dataelement, ddl, dcl, bdef, package, cts, checkout, checkin, activation, aunit, atc, abapgit, rap, badi, featuretoggle, datapreview, adt
- RFC 命令 (3个): startrfc, strust, user
- REST 命令 (1个): gcts
- OData 命令 (2个): bsp, flp

## 环境要求

- Python 3.7+
- SAP 连接信息 (SAP_ASHOST, SAP_CLIENT, SAP_USER, SAP_PASSWORD)
- RFC 命令需要 PyRFC 和 SAP NW RFC SDK
