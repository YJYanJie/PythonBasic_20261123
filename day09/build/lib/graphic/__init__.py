# 限制包中的哪些模块可以被导入
# from 包名 import 模块
# from . import circle
# from . import rectangle


# 绝对路径导入,会将circle作为顶级模块,直接从 sys.path 中找 circle 模块,而不是找 graphic.circle
# import circle


__all__ = ["circle"]