# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'device_information_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_DeviceInformationDialog(object):
    def setupUi(self, DeviceInformationDialog):
        if not DeviceInformationDialog.objectName():
            DeviceInformationDialog.setObjectName(u"DeviceInformationDialog")
        DeviceInformationDialog.resize(280, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeviceInformationDialog.sizePolicy().hasHeightForWidth())
        DeviceInformationDialog.setSizePolicy(sizePolicy)
        DeviceInformationDialog.setMinimumSize(QSize(280, 100))
        DeviceInformationDialog.setMaximumSize(QSize(280, 135))
        DeviceInformationDialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(DeviceInformationDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(DeviceInformationDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.hardware_version_name_label = QLabel(self.widget)
        self.hardware_version_name_label.setObjectName(u"hardware_version_name_label")
        font = QFont()
        font.setBold(True)
        self.hardware_version_name_label.setFont(font)

        self.gridLayout.addWidget(self.hardware_version_name_label, 0, 0, 1, 1)

        self.hardware_version_value_label = QLabel(self.widget)
        self.hardware_version_value_label.setObjectName(u"hardware_version_value_label")

        self.gridLayout.addWidget(self.hardware_version_value_label, 0, 1, 1, 1)

        self.firmware_version_value_label = QLabel(self.widget)
        self.firmware_version_value_label.setObjectName(u"firmware_version_value_label")

        self.gridLayout.addWidget(self.firmware_version_value_label, 1, 1, 1, 1)

        self.firmware_version_name_label = QLabel(self.widget)
        self.firmware_version_name_label.setObjectName(u"firmware_version_name_label")
        self.firmware_version_name_label.setFont(font)

        self.gridLayout.addWidget(self.firmware_version_name_label, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(DeviceInformationDialog)

        QMetaObject.connectSlotsByName(DeviceInformationDialog)
    # setupUi

    def retranslateUi(self, DeviceInformationDialog):
        DeviceInformationDialog.setWindowTitle(QCoreApplication.translate("DeviceInformationDialog", u"Device Information", None))
        self.hardware_version_name_label.setText(QCoreApplication.translate("DeviceInformationDialog", u"Hardware Version", None))
        self.hardware_version_value_label.setText("")
        self.firmware_version_value_label.setText("")
        self.firmware_version_name_label.setText(QCoreApplication.translate("DeviceInformationDialog", u"Firmware Version", None))
    # retranslateUi

