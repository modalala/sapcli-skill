#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SAP CLI 连接验证命令"""

import sys
import io

# Windows 编码修复
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass


def command(arguments):
    """验证 SAP 连接配置"""
    print("=" * 50)
    print("SAP CLI 连接配置验证")
    print("=" * 50)
    print()

    # 显示配置信息
    print("配置信息:")
    print(f"  SAP_ASHOST    : {arguments.ashost or '未设置'}")
    print(f"  SAP_CLIENT    : {arguments.client or '未设置'}")
    print(f"  SAP_USER      : {arguments.user or '未设置'}")
    print(f"  SAP_PORT      : {arguments.port or '默认'}")
    print(f"  SAP_SSL       : {'否' if arguments.ssl is False else '是'}")
    print(f"  SAP_SYSNR     : {arguments.sysnr or '00'}")
    print()

    # 检查必要配置
    errors = []
    if not arguments.ashost and not getattr(arguments, 'mshost', None):
        errors.append("缺少 SAP_ASHOST 或 SAP_MSHOST")
    if not arguments.client:
        errors.append("缺少 SAP_CLIENT")
    if not arguments.user and not (getattr(arguments, 'snc_qop', None) or
                                    getattr(arguments, 'snc_myname', None) or
                                    getattr(arguments, 'snc_partnername', None)):
        errors.append("缺少 SAP_USER")

    if errors:
        print("配置错误:")
        for error in errors:
            print(f"  ✗ {error}")
        return 1

    print("配置检查: ✓ 通过")
    print()

    # 尝试连接
    print("正在测试连接...")
    try:
        connection = arguments.connection_factory(arguments)
        print("连接测试: ✓ 成功")
        print()
        print("=" * 50)
        print("所有检查通过，SAP CLI 配置正确!")
        print("=" * 50)
        return 0
    except Exception as e:
        print(f"连接测试: ✗ 失败")
        print(f"错误信息: {str(e)}")
        return 1


class Command:
    """check 命令类"""
    name = 'check'
    description = '验证 SAP 连接配置'

    def install_parser(self, parser):
        parser.set_defaults(execute=command)

    def __call__(self, arguments):
        return arguments.execute(arguments)