# RuijieWebAutoLoginCUIT

基于Python的锐捷V2校园网eportal Web自动登录脚本（成都信息工程大学）

Python源码fork自[PeacherMZ/RuijieWebAutoLogin](https://github.com/PeacherMZ/RuijieWebAutoLogin)仓库，并对代码细节进行了优化。

## 环境和依赖

+ Python 3.x

+ requests依赖库（使用`python -m pip install requests`安装）

## 食用方法

1. git clone此仓库。

2. 只需将post中的请求头相关参数填在对应位置（见源码注释）。

3. 运行此Python脚本，即可实现每20~40秒自动查询与登录。

PS：成都信息工程大学（CUIT）的校园网登录IP为10.254.241.19，已在代码中替换。
