#encoding:utf-8
import cx_Oracle
class SmsCheckCode():
    #此方法用于在使用余额付款时从数据库中得到短信验证码
    def getCheckCode(self):

        con=cx_Oracle.connect('yydscs','yycs_123','192.168.2.63/chinapay')
        cr=con.cursor()
        sql="select mq.send_content from yydscs.csm_msg_sms_send mq where mq.send_to_user_id='3738017' order by mq.send_add_time desc"
        cr.execute(sql)
        rs=cr.fetchone()
        for m in rs:
            mv=m.decode('gbk')
            checkcode=mv[13:19]
            return checkcode