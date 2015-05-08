# encoding:utf-8
import xlrd
class GetRowAndColNumber():
    def getRowAndColNumber(self,excel_path,sheet_name,key):
        """该函数的作用：通过参数sheet_name和key，去返回一个该key所在行号和列号的列表"""
        data=xlrd.open_workbook(excel_path)
        sheet=data.sheet_by_name(sheet_name)
        rows=sheet.nrows
        cols=sheet.ncols
        row_col_list=[]
        for row_number in range(rows):
            for col_number in range(cols):
                if sheet.cell_value(row_number,col_number)==key:
                    row_col_list.append(row_number)
                    row_col_list.append(col_number)
                    return row_col_list

