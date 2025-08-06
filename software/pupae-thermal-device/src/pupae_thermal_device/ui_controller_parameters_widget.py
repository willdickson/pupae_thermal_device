# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controller_parameters_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_ControllerParametersWidget(object):
    def setupUi(self, ControllerParametersWidget):
        if not ControllerParametersWidget.objectName():
            ControllerParametersWidget.setObjectName(u"ControllerParametersWidget")
        ControllerParametersWidget.resize(344, 285)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ControllerParametersWidget.sizePolicy().hasHeightForWidth())
        ControllerParametersWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(ControllerParametersWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.setpoint_right_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.setpoint_right_dblspinbox.setObjectName(u"setpoint_right_dblspinbox")
        self.setpoint_right_dblspinbox.setMinimum(16.000000000000000)
        self.setpoint_right_dblspinbox.setMaximum(34.000000000000000)
        self.setpoint_right_dblspinbox.setSingleStep(0.100000000000000)
        self.setpoint_right_dblspinbox.setValue(22.000000000000000)

        self.gridLayout.addWidget(self.setpoint_right_dblspinbox, 5, 2, 1, 1)

        self.controller_right_parameters_label = QLabel(ControllerParametersWidget)
        self.controller_right_parameters_label.setObjectName(u"controller_right_parameters_label")
        self.controller_right_parameters_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.controller_right_parameters_label, 0, 2, 1, 1)

        self.setpoint_left_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.setpoint_left_dblspinbox.setObjectName(u"setpoint_left_dblspinbox")
        self.setpoint_left_dblspinbox.setMinimum(16.000000000000000)
        self.setpoint_left_dblspinbox.setMaximum(34.000000000000000)
        self.setpoint_left_dblspinbox.setSingleStep(0.100000000000000)
        self.setpoint_left_dblspinbox.setValue(22.000000000000000)

        self.gridLayout.addWidget(self.setpoint_left_dblspinbox, 5, 1, 1, 1)

        self.offset_right_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.offset_right_dblspinbox.setObjectName(u"offset_right_dblspinbox")
        self.offset_right_dblspinbox.setMinimum(-10000.000000000000000)
        self.offset_right_dblspinbox.setMaximum(10000.000000000000000)

        self.gridLayout.addWidget(self.offset_right_dblspinbox, 4, 2, 1, 1)

        self.pgain_left_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.pgain_left_dblspinbox.setObjectName(u"pgain_left_dblspinbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pgain_left_dblspinbox.sizePolicy().hasHeightForWidth())
        self.pgain_left_dblspinbox.setSizePolicy(sizePolicy1)
        self.pgain_left_dblspinbox.setMinimumSize(QSize(100, 0))
        self.pgain_left_dblspinbox.setMaximum(10000.000000000000000)

        self.gridLayout.addWidget(self.pgain_left_dblspinbox, 1, 1, 1, 1)

        self.offset_left_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.offset_left_dblspinbox.setObjectName(u"offset_left_dblspinbox")
        self.offset_left_dblspinbox.setMinimum(-10000.000000000000000)
        self.offset_left_dblspinbox.setMaximum(10000.000000000000000)
        self.offset_left_dblspinbox.setSingleStep(1.000000000000000)

        self.gridLayout.addWidget(self.offset_left_dblspinbox, 4, 1, 1, 1)

        self.pgain_name_label = QLabel(ControllerParametersWidget)
        self.pgain_name_label.setObjectName(u"pgain_name_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pgain_name_label.sizePolicy().hasHeightForWidth())
        self.pgain_name_label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setBold(False)
        self.pgain_name_label.setFont(font)

        self.gridLayout.addWidget(self.pgain_name_label, 1, 0, 1, 1)

        self.pgain_right_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.pgain_right_dblspinbox.setObjectName(u"pgain_right_dblspinbox")
        sizePolicy1.setHeightForWidth(self.pgain_right_dblspinbox.sizePolicy().hasHeightForWidth())
        self.pgain_right_dblspinbox.setSizePolicy(sizePolicy1)
        self.pgain_right_dblspinbox.setMinimumSize(QSize(100, 0))
        self.pgain_right_dblspinbox.setMaximum(10000.000000000000000)

        self.gridLayout.addWidget(self.pgain_right_dblspinbox, 1, 2, 1, 1)

        self.label_29 = QLabel(ControllerParametersWidget)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 0, 3, 1, 1)

        self.igain_name_label = QLabel(ControllerParametersWidget)
        self.igain_name_label.setObjectName(u"igain_name_label")
        self.igain_name_label.setFont(font)

        self.gridLayout.addWidget(self.igain_name_label, 2, 0, 1, 1)

        self.enable_disable_pushbutton = QPushButton(ControllerParametersWidget)
        self.enable_disable_pushbutton.setObjectName(u"enable_disable_pushbutton")
        self.enable_disable_pushbutton.setMinimumSize(QSize(100, 0))
        self.enable_disable_pushbutton.setFont(font)

        self.gridLayout.addWidget(self.enable_disable_pushbutton, 6, 2, 1, 1)

        self.igain_right_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.igain_right_dblspinbox.setObjectName(u"igain_right_dblspinbox")
        self.igain_right_dblspinbox.setDecimals(3)
        self.igain_right_dblspinbox.setMaximum(10000.000000000000000)
        self.igain_right_dblspinbox.setSingleStep(0.001000000000000)

        self.gridLayout.addWidget(self.igain_right_dblspinbox, 2, 2, 1, 1)

        self.controller_parameters_left_label = QLabel(ControllerParametersWidget)
        self.controller_parameters_left_label.setObjectName(u"controller_parameters_left_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.controller_parameters_left_label.sizePolicy().hasHeightForWidth())
        self.controller_parameters_left_label.setSizePolicy(sizePolicy3)
        self.controller_parameters_left_label.setMinimumSize(QSize(0, 20))
        self.controller_parameters_left_label.setFont(font)
        self.controller_parameters_left_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.controller_parameters_left_label, 0, 1, 1, 1)

        self.setpoint_units_label = QLabel(ControllerParametersWidget)
        self.setpoint_units_label.setObjectName(u"setpoint_units_label")
        sizePolicy2.setHeightForWidth(self.setpoint_units_label.sizePolicy().hasHeightForWidth())
        self.setpoint_units_label.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.setpoint_units_label, 5, 3, 1, 1)

        self.setpoint_name_label = QLabel(ControllerParametersWidget)
        self.setpoint_name_label.setObjectName(u"setpoint_name_label")
        self.setpoint_name_label.setFont(font)

        self.gridLayout.addWidget(self.setpoint_name_label, 5, 0, 1, 1)

        self.offset_name_label = QLabel(ControllerParametersWidget)
        self.offset_name_label.setObjectName(u"offset_name_label")
        self.offset_name_label.setFont(font)

        self.gridLayout.addWidget(self.offset_name_label, 4, 0, 1, 1)

        self.controller_name_label = QLabel(ControllerParametersWidget)
        self.controller_name_label.setObjectName(u"controller_name_label")
        self.controller_name_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.controller_name_label, 6, 1, 1, 1)

        self.igain_left_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.igain_left_dblspinbox.setObjectName(u"igain_left_dblspinbox")
        self.igain_left_dblspinbox.setDecimals(3)
        self.igain_left_dblspinbox.setMaximum(10000.000000000000000)
        self.igain_left_dblspinbox.setSingleStep(0.001000000000000)

        self.gridLayout.addWidget(self.igain_left_dblspinbox, 2, 1, 1, 1)

        self.dgain_name_label = QLabel(ControllerParametersWidget)
        self.dgain_name_label.setObjectName(u"dgain_name_label")

        self.gridLayout.addWidget(self.dgain_name_label, 3, 0, 1, 1)

        self.dgain_left_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.dgain_left_dblspinbox.setObjectName(u"dgain_left_dblspinbox")
        self.dgain_left_dblspinbox.setMaximum(10000.000000000000000)

        self.gridLayout.addWidget(self.dgain_left_dblspinbox, 3, 1, 1, 1)

        self.dgain_right_dblspinbox = QDoubleSpinBox(ControllerParametersWidget)
        self.dgain_right_dblspinbox.setObjectName(u"dgain_right_dblspinbox")
        self.dgain_right_dblspinbox.setMaximum(10000.000000000000000)

        self.gridLayout.addWidget(self.dgain_right_dblspinbox, 3, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(ControllerParametersWidget)

        QMetaObject.connectSlotsByName(ControllerParametersWidget)
    # setupUi

    def retranslateUi(self, ControllerParametersWidget):
        ControllerParametersWidget.setWindowTitle(QCoreApplication.translate("ControllerParametersWidget", u"Form", None))
        self.controller_right_parameters_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"Right", None))
        self.pgain_name_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"PGain", None))
        self.label_29.setText("")
        self.igain_name_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"IGain", None))
        self.enable_disable_pushbutton.setText(QCoreApplication.translate("ControllerParametersWidget", u"Disabled", None))
        self.controller_parameters_left_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"Left", None))
        self.setpoint_units_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"C", None))
        self.setpoint_name_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"Setpoint", None))
        self.offset_name_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"Offset", None))
        self.controller_name_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"Controller", None))
        self.dgain_name_label.setText(QCoreApplication.translate("ControllerParametersWidget", u"DGain", None))
    # retranslateUi

