# encoding:utf-8
import cx_Oracle
class SelectFromOracle():

    def selectFromOracle(self,sql,key):
        """
        where语句中：key值为中文的时候需要用到编码格式转换，所以需要这种格式的查询语句
        """
        con=cx_Oracle.connect("yydscs01", "cs_123","192.168.2.102/chinapay")
        cr=con.cursor()
        data=key.decode('utf-8').encode('gbk')
        sql=sql+"'"+data+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        count_data=cr.rowcount
        return count_data


    def selectFromOracleWithoutChineseWord(self,sql,key):
        """
        where语句中：key值不是中文的时候不需要用到编码格式转换，所以需要这种格式的查询语句
        """
        con=cx_Oracle.connect("yydscs01", "cs_123","192.168.2.102/chinapay")
        cr=con.cursor()
        data=key
        sql=sql+"'"+data+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        count_data=cr.rowcount
        return count_data


    def select(self):

        sql="select dd.* from yydscs.IMS_NEWS dd where dd.title="
        self.selectFromOracle(sql,"是打发")




