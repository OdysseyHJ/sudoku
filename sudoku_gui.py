import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import  sudoku


class CSudoRobot(QWidget):
    def __init__(self):
        super().__init__()


        # self.lblID = 0

        self.sections = {}

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 1000, 800)
        self.setWindowTitle('胡胡子给球球子的数独神器')
        # self.setWindowIcon(QIcon('AC.jpg'))

        self.table = QTableWidget(self)
        self.init_sudoku_map()


        self.btn_getRes = QPushButton("获取答案")
        self.btn_getRes.clicked.connect(self.button_event_get_res)

        self.btn_reset_table = QPushButton("重置")
        self.btn_reset_table.clicked.connect(self.button_event_reset_table)

        self.spacerItem = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn_getRes)
        self.vbox.addWidget(self.btn_reset_table)

        self.vbox.addSpacerItem(self.spacerItem)
        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.table)
        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox2)
        self.hbox.addLayout(self.vbox)
        self.setLayout(self.hbox)
        self.show()

    def init_sudoku_map(self):
        raw_count = 9
        column_count = 9
        self.table.setRowCount(raw_count)
        self.table.setColumnCount(column_count)

        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        for index in range(column_count):
            self.table.horizontalHeader().resizeSection(index, 60)
            self.table.verticalHeader().resizeSection(index, 60)

        # self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setFont(QFont('Times', 20, QFont.Black))

        for x_pos in range(column_count):
            for y_pos in range(raw_count):
                unit_item = QTableWidgetItem()
                unit_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                # unit_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.table.setItem(x_pos, y_pos, unit_item)

        # print(self.table.item(1,1).text())

    def button_event_get_res(self):
        sudoku_map = []
        for x in range(9):
            line = []
            for y in range(9):
                str_unit = self.table.item(x, y).text()
                num_unit = 0
                if len(str_unit) == 1:
                    num_unit = int(str_unit)
                # print(num_unit)
                line.append(num_unit)
            sudoku_map.append(line)

        # sudoku.print_sudoku_map(sudoku_map)
        sudoku.dfs_fill_sudoku_map(sudoku_map, 0, 0)
        # sudoku.print_sudoku_map(sudoku_map)
        self.refresh_table(sudoku_map)

    def button_event_reset_table(self):
        self.refresh_table()

    def refresh_table(self, table = None):
        # print(table)
        if table == None:
            for x_pos in range(9):
                for y_pos in range(9):
                    unit_item = QTableWidgetItem()
                    unit_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    # unit_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.table.setItem(x_pos, y_pos, unit_item)
        else:
            for x_pos in range(9):
                for y_pos in range(9):
                    unit_item = QTableWidgetItem(str(table[x_pos][y_pos]))
                    unit_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    # unit_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.table.setItem(x_pos, y_pos, unit_item)


def proc():

    app = QApplication(sys.argv)
    ex = CSudoRobot()
    # ex2 = fncTable([1,2,3])
    # ex2.show()

    sys.exit(app.exec_())