[app]

# 应用标题 (显示在手机上)
title = Run Helper

# 版本号
version = 1.0.0

# 包名 (唯一标识)
package.name = runhelper
package.domain = com.runhelper

# 源代码入口
source.dir = .
source.include_exts = py

# 主程序文件
main.py = main.py

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

# 日志
log_level = 2

# 启用闪退报告
android.allow_backup = True

# gradle 依赖
android.gradle_dependencies =

# 架构 (armeabi-v7a 兼容性最好, arm64-v8a 是64位)
android.arch = armeabi-v7a

[buildozer]

# buildozer 日志级别
log_level = 2

# 构建目录
build_dir = .buildozer

# 清理构建
# 设置为 True 会删除之前的构建缓存
# buildozer clean = False
