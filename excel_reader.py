import xlrd


class ExcelReader:
    def __init__(self, path):
        """
        Excel reader class designed to get information out of excel files

        :param path: full excel file path
        """
        self.excel = xlrd.open_workbook(path)
        self.sheet_names_array = self.excel.sheet_names()

    def excel_to_array(self, sheet_index):
        """
        creates an array from the entire sheet in the current excel file
        :param sheet_index: starts from 0
        :return: entire excel sheet as array
        """
        current_sheet = self.excel.sheet_by_index(sheet_index)
        new_arr = []
        # amount_of_cols = current_sheet.ncols
        amount_of_rows = current_sheet.nrows
        for i in range(0, amount_of_rows):
            new_arr.append(current_sheet.row_values(i))
        return new_arr

    def get_cell(self, row, col, sheet_index):
        """
        returns a specific cell in the specific excel sheet

        :param row: excel row in the selected sheet, starts from 0
        :param col: excel column in the selected sheet, starts from 0
        :param sheet_index: starts from 0
        :return: the current cell selected as the type of value in it
        """
        current_sheet = self.excel.sheet_by_index(sheet_index)
        return current_sheet.cell(row, col).value

    def get_row(self, row, sheet_index):
        """
        returns a list from the selected row in the selected sheet.

        :param row:
        :param sheet_index: starts from 0
        :return: list of values from row
        """
        return self.excel.sheet_by_index(sheet_index).row_values(row)

    def get_headlines(self, sheet_index):
        """
        returns a list of the first row in the excel file, in case it contains headlines that you want to use
        :param sheet_index: starts from 0
        :return: list of values from row in line 0.
        """
        return self.get_row(0, sheet_index)

    def get_col(self, sheet_index, col, without_headlines):
        """
        creates a list of all the content of the column. if it has headline it will ignore it.

        :param sheet_index: starts from 0
        :param col: a column from the current sheet, starts from 0
        :param without_headlines: does it contain headlines or not
        :return: a list contains all the content of the column without headline
        """
        current_sheet = self.excel.sheet_by_index(sheet_index)
        amount_of_rows = current_sheet.nrows
        arr = []
        for i in range(without_headlines, amount_of_rows):
            arr.append(str(self.get_cell(i, col, sheet_index)).lower())
        return arr

    def get_amount_of_cols(self, sheet_index):
        """
        returns amount of columns from the selected sheet
        :param sheet_index:
        :return: integer containing the amount of columns
        """
        return self.excel.sheet_by_index(sheet_index).ncols

    def get_amount_of_rows(self, sheet_index):
        """
        returns the amount of columns in the current sheet
        :param sheet_index: starts from 0
        :return: amount of columns
        """
        return self.excel.sheet_by_index(sheet_index).nrows

    def print(self, sheet_index):
        """

        :param sheet_index: starts from 0
        :return:
        """
        for i in range(0, self.get_amount_of_rows(sheet_index)):
            for j in range(0, self.get_amount_of_cols(sheet_index)):
                print(self.get_cell(i, j, sheet_index), end='\t')
            print()
