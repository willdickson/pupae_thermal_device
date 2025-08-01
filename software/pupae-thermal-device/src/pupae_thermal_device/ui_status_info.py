# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'status_info.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_StatusInfo(object):
    def setupUi(self, StatusInfo):
        if not StatusInfo.objectName():
            StatusInfo.setObjectName(u"StatusInfo")
        StatusInfo.resize(819, 58)
        self.horizontalLayout_2 = QHBoxLayout(StatusInfo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(StatusInfo)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_label = QLabel(self.widget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QSize(0, 0))
        self.title_label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(True)
        self.title_label.setFont(font)

        self.horizontalLayout.addWidget(self.title_label)

        self.status_label = QLabel(self.widget)
        self.status_label.setObjectName(u"status_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy1)
        self.status_label.setMinimumSize(QSize(0, 0))
        self.status_label.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.status_label)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(StatusInfo)

        QMetaObject.connectSlotsByName(StatusInfo)
    # setupUi

    def retranslateUi(self, StatusInfo):
        StatusInfo.setWindowTitle(QCoreApplication.translate("StatusInfo", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("StatusInfo", u"Status:", None))
        self.status_label.setText("")
    # retranslateUi

