import xlrd
from datetime import datetime

"""
    @Updates
        17/02/2020:
        Working methods: All

    @Important notes:
        the path needs to contain 2 dots on the start of the file system so it will find it
        example:"..\\data\\data location\\excel file.xls"
"""


class ExcelReader:
    def __init__(self, path):
        self.excel = xlrd.open_workbook(path)
        self.sheet_names_array = self.excel.sheet_names()

    def excel_to_array(self, sheet_index):
        current_sheet = self.excel.sheet_by_index(sheet_index)
        new_arr = []
        amount_of_rows = current_sheet.nrows
        for i in range(0, amount_of_rows):
            new_arr.append(current_sheet.row_values(i))
        return new_arr

    def get_cell(self, row, col, sheet_index):
        current_sheet = self.excel.sheet_by_index(sheet_index)
        return current_sheet.cell(row, col).value

    def get_row(self, row, sheet_index):
        return self.excel.sheet_by_index(sheet_index).row_values(row)

    def get_headlines(self, sheet_index):
        return self.get_row(0, sheet_index)

    # if you want the headlines write 0, else write 1
    def get_col(self, sheet_index, col, without_headlines):
        current_sheet = self.excel.sheet_by_index(sheet_index)
        amount_of_rows = current_sheet.nrows
        arr = []
        for i in range(without_headlines, amount_of_rows):
            arr.append(str(self.get_cell(i, col, sheet_index)).lower())
        return arr

    def get_distinct_col(self, sheet_index, col, without_headlines):
        return list(dict.fromkeys(self.get_col(sheet_index, col, without_headlines)))

    def get_amount_of_cols(self, sheet_index):
        return self.excel.sheet_by_index(sheet_index).ncols

    def get_amount_of_rows(self, sheet_index):
        return self.excel.sheet_by_index(sheet_index).nrows

    def generate_headline_dict(self, sheet_index):
        dic = dict()
        row = self.get_row(0, sheet_index)
        for i in range(0, len(row)):
            dic[row[i]] = i
        return dic

    def convert_float_to_datetime(self, excel_date):
        return datetime(*xlrd.xldate_as_tuple(excel_date, 0))
# a = ExcelReader("..\\data\\data location\\excel file.xls")
# curr_arr = a.excel_to_array(0)
# # print(curr_arr)
# # print(a.get_row(4, 0))
# # print(a.get_headlines(0))
# arr = a.get_col(0, 3, 1)
# print(a.get_distinct_col(0, 3, 1))
# print(arr)
