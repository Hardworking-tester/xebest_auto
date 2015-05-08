#encoding:utf-8
import logging
log_path="D:\\testlog\\resultlog.txt"
log=logging.getLogger("wwg")
log.setLevel(logging.WARNING)
filehandler=logging.FileHandler(log_path)
# filehandler.setLevel(logging.INFO)
formatter=logging.Formatter("%(asctime)s:%(module)s- %(funcName)s-%(lineno)d %(message)s","%Y年%m月%d日 %H:%M:%S")
filehandler.setFormatter(formatter)
log.addHandler(filehandler)
aa="http://192.168.1.241:8080/zhsq/client/weather!list.action"
log.warning("测试地址为：%s" %aa)
# logging.basicConfig(level=logging.DEBUG,
#                 format='hi:%(asctime)s  %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='D:\\testlog\\resultlog.txt',
#                 filemode='a')
# log=logging.getLogger("wwg")
# log.setLevel(logging.ERROR)
# logging.debug('This is debug11 message')
# logging.info('This is info message')
# logging.warning('This is warning message')
# logging.critical("dssd")