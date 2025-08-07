# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_values_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SystemValuesWidget(object):
    def setupUi(self, SystemValuesWidget):
        if not SystemValuesWidget.objectName():
            SystemValuesWidget.setObjectName(u"SystemValuesWidget")
        SystemValuesWidget.resize(306, 215)
        self.horizontalLayout = QHBoxLayout(SystemValuesWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.ierror_left_value_label = QLabel(SystemValuesWidget)
        self.ierror_left_value_label.setObjectName(u"ierror_left_value_label")
        self.ierror_left_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.ierror_left_value_label, 3, 1, 1, 1)

        self.error_right_value_label = QLabel(SystemValuesWidget)
        self.error_right_value_label.setObjectName(u"error_right_value_label")
        self.error_right_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.error_right_value_label, 2, 2, 1, 1)

        self.label_21 = QLabel(SystemValuesWidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)

        self.ierror_right_value_label = QLabel(SystemValuesWidget)
        self.ierror_right_value_label.setObjectName(u"ierror_right_value_label")
        self.ierror_right_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.ierror_right_value_label, 3, 2, 1, 1)

        self.temperature_right_value_label = QLabel(SystemValuesWidget)
        self.temperature_right_value_label.setObjectName(u"temperature_right_value_label")
        self.temperature_right_value_label.setMinimumSize(QSize(60, 0))
        self.temperature_right_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.temperature_right_value_label, 1, 2, 1, 1)

        self.power_left_value_label = QLabel(SystemValuesWidget)
        self.power_left_value_label.setObjectName(u"power_left_value_label")
        self.power_left_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.power_left_value_label, 5, 1, 1, 1)

        self.error_name_label = QLabel(SystemValuesWidget)
        self.error_name_label.setObjectName(u"error_name_label")

        self.gridLayout_2.addWidget(self.error_name_label, 2, 0, 1, 1)

        self.power_name_label = QLabel(SystemValuesWidget)
        self.power_name_label.setObjectName(u"power_name_label")

        self.gridLayout_2.addWidget(self.power_name_label, 5, 0, 1, 1)

        self.temperature_name_label = QLabel(SystemValuesWidget)
        self.temperature_name_label.setObjectName(u"temperature_name_label")

        self.gridLayout_2.addWidget(self.temperature_name_label, 1, 0, 1, 1)

        self.label_20 = QLabel(SystemValuesWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 0, 3, 1, 1)

        self.system_values_right_label = QLabel(SystemValuesWidget)
        self.system_values_right_label.setObjectName(u"system_values_right_label")
        self.system_values_right_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.system_values_right_label, 0, 2, 1, 1)

        self.power_right_value_label = QLabel(SystemValuesWidget)
        self.power_right_value_label.setObjectName(u"power_right_value_label")
        self.power_right_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.power_right_value_label, 5, 2, 1, 1)

        self.system_values_left_label = QLabel(SystemValuesWidget)
        self.system_values_left_label.setObjectName(u"system_values_left_label")
        self.system_values_left_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.system_values_left_label, 0, 1, 1, 1)

        self.error_left_value_label = QLabel(SystemValuesWidget)
        self.error_left_value_label.setObjectName(u"error_left_value_label")
        self.error_left_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.error_left_value_label, 2, 1, 1, 1)

        self.temperature_left_value_label = QLabel(SystemValuesWidget)
        self.temperature_left_value_label.setObjectName(u"temperature_left_value_label")
        self.temperature_left_value_label.setMinimumSize(QSize(60, 0))
        self.temperature_left_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.temperature_left_value_label, 1, 1, 1, 1)

        self.ierror_name_label = QLabel(SystemValuesWidget)
        self.ierror_name_label.setObjectName(u"ierror_name_label")

        self.gridLayout_2.addWidget(self.ierror_name_label, 3, 0, 1, 1)

        self.derror_name_label = QLabel(SystemValuesWidget)
        self.derror_name_label.setObjectName(u"derror_name_label")

        self.gridLayout_2.addWidget(self.derror_name_label, 4, 0, 1, 1)

        self.derror_left_value_label = QLabel(SystemValuesWidget)
        self.derror_left_value_label.setObjectName(u"derror_left_value_label")
        self.derror_left_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.derror_left_value_label, 4, 1, 1, 1)

        self.derror_right_value_label = QLabel(SystemValuesWidget)
        self.derror_right_value_label.setObjectName(u"derror_right_value_label")
        self.derror_right_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.derror_right_value_label, 4, 2, 1, 1)

        self.error_units_label = QLabel(SystemValuesWidget)
        self.error_units_label.setObjectName(u"error_units_label")
        self.error_units_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.error_units_label, 2, 3, 1, 1)

        self.ierror_units_label = QLabel(SystemValuesWidget)
        self.ierror_units_label.setObjectName(u"ierror_units_label")
        self.ierror_units_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.ierror_units_label, 3, 3, 1, 1)

        self.derror_units_label = QLabel(SystemValuesWidget)
        self.derror_units_label.setObjectName(u"derror_units_label")
        self.derror_units_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.derror_units_label, 4, 3, 1, 1)

        self.temperature_units_label = QLabel(SystemValuesWidget)
        self.temperature_units_label.setObjectName(u"temperature_units_label")

        self.gridLayout_2.addWidget(self.temperature_units_label, 1, 3, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(SystemValuesWidget)

        QMetaObject.connectSlotsByName(SystemValuesWidget)
    # setupUi

    def retranslateUi(self, SystemValuesWidget):
        SystemValuesWidget.setWindowTitle(QCoreApplication.translate("SystemValuesWidget", u"Form", None))
        self.ierror_left_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.error_right_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.label_21.setText("")
        self.ierror_right_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.temperature_right_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.power_left_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.error_name_label.setText(QCoreApplication.translate("SystemValuesWidget", u"Error", None))
        self.power_name_label.setText(QCoreApplication.translate("SystemValuesWidget", u"Power", None))
        self.temperature_name_label.setText(QCoreApplication.translate("SystemValuesWidget", u"Temperature", None))
        self.label_20.setText("")
        self.system_values_right_label.setText(QCoreApplication.translate("SystemValuesWidget", u"Right", None))
        self.power_right_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.system_values_left_label.setText(QCoreApplication.translate("SystemValuesWidget", u"Left", None))
        self.error_left_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.temperature_left_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.ierror_name_label.setText(QCoreApplication.translate("SystemValuesWidget", u"IError", None))
        self.derror_name_label.setText(QCoreApplication.translate("SystemValuesWidget", u"DError", None))
        self.derror_left_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.derror_right_value_label.setText(QCoreApplication.translate("SystemValuesWidget", u"0.0", None))
        self.error_units_label.setText(QCoreApplication.translate("SystemValuesWidget", u"C", None))
        self.ierror_units_label.setText(QCoreApplication.translate("SystemValuesWidget", u"C s", None))
        self.derror_units_label.setText(QCoreApplication.translate("SystemValuesWidget", u"C / s", None))
        self.temperature_units_label.setText(QCoreApplication.translate("SystemValuesWidget", u"C", None))
    # retranslateUi

