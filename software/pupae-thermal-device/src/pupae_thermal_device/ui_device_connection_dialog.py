# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'device_connection_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DeviceConnectionDialog(object):
    def setupUi(self, DeviceConnectionDialog):
        if not DeviceConnectionDialog.objectName():
            DeviceConnectionDialog.setObjectName(u"DeviceConnectionDialog")
        DeviceConnectionDialog.resize(500, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeviceConnectionDialog.sizePolicy().hasHeightForWidth())
        DeviceConnectionDialog.setSizePolicy(sizePolicy)
        DeviceConnectionDialog.setMinimumSize(QSize(500, 250))
        DeviceConnectionDialog.setMaximumSize(QSize(600, 350))
        DeviceConnectionDialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(DeviceConnectionDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.port_selection_widget = QWidget(DeviceConnectionDialog)
        self.port_selection_widget.setObjectName(u"port_selection_widget")
        self.horizontalLayout = QHBoxLayout(self.port_selection_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.port_label = QLabel(self.port_selection_widget)
        self.port_label.setObjectName(u"port_label")
        font = QFont()
        font.setBold(True)
        self.port_label.setFont(font)

        self.horizontalLayout.addWidget(self.port_label)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.port_combobox = QComboBox(self.port_selection_widget)
        self.port_combobox.setObjectName(u"port_combobox")
        self.port_combobox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.port_combobox)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.connect_pushbutton = QPushButton(self.port_selection_widget)
        self.connect_pushbutton.setObjectName(u"connect_pushbutton")

        self.horizontalLayout.addWidget(self.connect_pushbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.filter_checkbox = QCheckBox(self.port_selection_widget)
        self.filter_checkbox.setObjectName(u"filter_checkbox")

        self.horizontalLayout.addWidget(self.filter_checkbox)


        self.verticalLayout_2.addWidget(self.port_selection_widget)

        self.port_info_widget = QWidget(DeviceConnectionDialog)
        self.port_info_widget.setObjectName(u"port_info_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.port_info_widget.sizePolicy().hasHeightForWidth())
        self.port_info_widget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.port_info_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(self.port_info_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.port_info_label = QLabel(self.port_info_widget)
        self.port_info_label.setObjectName(u"port_info_label")
        self.port_info_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.port_info_label)


        self.verticalLayout_2.addWidget(self.port_info_widget)

        self.dialog_close_widget = QWidget(DeviceConnectionDialog)
        self.dialog_close_widget.setObjectName(u"dialog_close_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.dialog_close_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(375, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.close_dialog_pushbutton = QPushButton(self.dialog_close_widget)
        self.close_dialog_pushbutton.setObjectName(u"close_dialog_pushbutton")

        self.horizontalLayout_2.addWidget(self.close_dialog_pushbutton)


        self.verticalLayout_2.addWidget(self.dialog_close_widget)


        self.retranslateUi(DeviceConnectionDialog)

        QMetaObject.connectSlotsByName(DeviceConnectionDialog)
    # setupUi

    def retranslateUi(self, DeviceConnectionDialog):
        DeviceConnectionDialog.setWindowTitle(QCoreApplication.translate("DeviceConnectionDialog", u"Device Connection", None))
        self.port_label.setText(QCoreApplication.translate("DeviceConnectionDialog", u"Port:", None))
        self.connect_pushbutton.setText(QCoreApplication.translate("DeviceConnectionDialog", u"Connect", None))
        self.filter_checkbox.setText(QCoreApplication.translate("DeviceConnectionDialog", u"filter", None))
        self.port_info_label.setText("")
        self.close_dialog_pushbutton.setText(QCoreApplication.translate("DeviceConnectionDialog", u"Close", None))
    # retranslateUi

