help_guide = '''命令和二级命令均可只写首字母
/random help - 查阅帮助
/random - 在 [0, 100] 间取一个随机数
/random <数量> - 在 [0, 100] 间取若干个随机数
/random <a> <b> - 在 [a, b] 间取一个随机数
/random <a> <b> <数量> - 在 [a, b] 间取若干个随机数
/random bool - 取随机布尔值(True or False)
/random shuffle <序列> - 打乱该序列
/random choice <序列> - 在序列中挑一个元素
/random choice <序列> <数量> - 在序列中挑若干个元素'''
err = '错误: %s'