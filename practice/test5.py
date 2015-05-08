# encoding:utf-8
import time
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filepath="F:\\testresult\\"+now+"ResultReport.html"
result=open(filepath,'wb')
# runner=HTMLTestRunner.HTMLTestRunner(stream=result,title=u'测试报告',description=u'用例执行情况')
# runner.run(testunit)
result.close()