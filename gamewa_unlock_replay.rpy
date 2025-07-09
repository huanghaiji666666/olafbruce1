init -999 python:
    # 只修改“已观看”相关函数，保留 has_label 原功能
    def patch():
        result = None
        import renpy
        f = lambda *a, **k: True            # 恒返回 True
        renpy.exports.seen_image = f        # 缩略图锁定
        renpy.exports.has_seen  = f         # 用于 Replay 条件
        renpy.exports.seen_label = f        # 部分脚本也会判断
        return result                       # 单一 return
    patch()
