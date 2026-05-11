[app]

# 应用标题 (显示在手机上)
title = Run Helper

# 版本号
version = 2.0.0

# 包名 (唯一标识)
package.name = runhelper
package.domain = com.runhelper

# 源代码入口
source.dir = .
source.include_exts = py

# 依赖库
requirements = python3,kivy,requests

# Android 最低 API 级别
android.minapi = 21

# 权限
android.permissions = INTERNET

# 横竖屏
orientation = portrait

# 是否全屏
fullscreen = 0

# 图标
# icon.filename = icon.png

# SDK 最低版本
android.api = 31

# 固定 NDK 以减少 CI 漂移
android.ndk = 25b
android.ndk_api = 21

# 日志
log_level = 2

# 自动接受SDK license (避免交互)
android.accept_sdk_license = True

# 启用闪退报告
android.allow_backup = True

# 仅构建 64 位架构，避免旧架构工具链带来的额外不稳定因素
android.arch = arm64-v8a

[buildozer]

# buildozer 日志级别
log_level = 2

# 构建目录
build_dir = .buildozer

# 清理构建
# 设置为 True 会删除之前的构建缓存
# buildozer clean = False
