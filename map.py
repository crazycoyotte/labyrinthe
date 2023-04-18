import xlrd
import case
import constant


class Map:

    def __init__(self, filename):

        self.actual_map = []

        # Open the workbook
        self.book = xlrd.open_workbook(filename)

        # Get the first sheet
        sheet = self.book.sheet_by_index(0)
        self.rows = sheet.nrows
        self.cols = sheet.ncols

        # Read the rows and the cols
        for y in range(self.rows):
            for x in range(self.cols):
                cell_value = sheet.cell_value(y, x)
                element = cell_value.split(",")
                # print(x, y, cell_value)
                self.case = case.Case(x, y, element[0], element[1])
                self.actual_map.append(self.case)

    def get_cell_by_xy(self, x, y):
        id = x + self.cols * y
        cell = self.actual_map[id]
        return cell
