from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt

class listModel(QtCore.QAbstractListModel):
    def __init__(self, df=None):
        super().__init__()
        self.df = df or {}

        # 읽은 데이터 상태 표시 이미지
        self.tick = QtGui.QImage('./image/tick.png')
        self.redcross = QtGui.QImage('./image/redcross.png')

    # ListView 에 보여질 데이터 선별
    # Override
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # Json
            _, json = self.df['account'][index.row()]
            platform = json['PLATFORM']
            id = json['ID']
            pw = json['PW']
            job = json['JOB']

            strTemp = f'{job}\t{platform}\t{id}\t'
            return strTemp

        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.df['account'][index.row()]
            if status:
                return self.tick
            else:
                return self.redcross

    # Override
    def rowCount(self, index):
        return self.df['account'].__len__()