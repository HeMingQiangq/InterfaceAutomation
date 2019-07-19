# linkface接口自动化测试

它包含功能:
  * 测试数据初始化，并对数据的插入做了封装。
  * unittest单元测试框架运行测试
  * HTMLTestRunner生成接口测试报告


Python版本与依赖库：
  * python3.5+ :https://www.python.org/
  * Requests : https://github.com/kennethreitz/requests
  * PyMySQL : https://github.com/PyMySQL/PyMySQL

框架说明：
  * config路径下为全局配置信息，修改settings.py中的信息，可以切换测试环境
  * db_fixture路径下为数据库连接模块
  * excel_cases路径下存放excel版本测试用例模板及用例文件
  * interface路径下为测试用例
  * pictureDatas路径下为用例所需的图片参数
  * report路径下为HTML格式的测试报告
  * result路径下为保存的CSV格式的接口调用返回
  * db_config.ini中为数据库连接配置信息
  * clent.py为http请求客户端，其中封装的功能如下：
      1、构造http请求，如设置请求url，请求方法，请求头，请求体，发送请求
      2、解析json格式http响应
      3、断言方法，常用断言status和dictEqual
      4、工具类方法，如写入csv文件、截断小数
  * HTMLTestRunner.py为生成html报告所需的第三方包
  * run.py为统一执行测试脚本的文件
  * 用例设计形式参考interface路径下的common_use.py
