#encoding:utf-8
import cx_Oracle
class OracleT1():


    def select1(self):
        con=cx_Oracle.connect('yydscs','yycs_123','192.168.2.63/chinapay')
        cr=con.cursor()
        sql="select mq.send_content from yydscs.csm_msg_sms_send mq where mq.send_to_user_id='3738017' order by mq.send_add_time desc"
        cr.execute(sql)
        rs=cr.fetchone()
        for m in rs:
            mv=m.decode('gbk')
            checkcode=mv[13:19]
            print checkcode
        # for x in rs:
            # print x
            # for i in x:
            #     checkcode=i.decode('gbk')
            #     print checkcode
                # newcode=checkcode.split(",")
                # print newcode
        # print rs
pp=OracleT1()
pp.select1()