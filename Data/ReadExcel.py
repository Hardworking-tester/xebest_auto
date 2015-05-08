#encoding:utf-8
import xlrd
class ReadExcel():
    def getTable(self,file_path):
        """
        读取一个excel文件并返回该表格对象
        """
        data=xlrd.open_workbook(file_path)
        table=data.sheets()[0]
        return table

    def getTableBySheetName(self,file_path,sheetname):
        """
        读取一个excel文件并返回该表格对象
        """
        data=xlrd.open_workbook(file_path)
        table=data.sheet_by_name(sheetname)
        return table

    def getExcelRows(self,file_path):
        """
        通过获取到的表格对象得到总行数
        """
        table=self.getTable(file_path)
        rows=table.nrows
        return rows
    def getExcelCols(self,file_path):
        """
        通过获取到的表格对象得到总行数
        """
        table=self.getTable(file_path)
        cols=table.ncols
        return cols