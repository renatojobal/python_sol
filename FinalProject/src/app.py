import sys
from screen import *
from place import Place

from PyQt5 import QtWidgets, QtCore
import matplotlib
import matplotlib.dates as mdates
import logging
from manager import Manager

import constants
_translate = QtCore.QCoreApplication.translate
matplotlib.use('QT5Agg')  # Use QT5Agg as backend


class DialogApplication(QtWidgets.QDialog):
    """
    Main class for interface
    """

    def __init__(self):
        super().__init__()

        # Set up the dialog
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)

        # Create manger instance
        self.manager = Manager()

        # Plot
        self.ax1: matplotlib.axes._subplots.AxesSubplot = self.dialog.mplwidget.canvas.axes  # Left axis
        self.ax2: matplotlib.axes._subplots.AxesSubplot = self.ax1.twinx()  # Right axis
        print(self.ax1.__class__)

        # Variables the user can change
        self.current_country_txt = 'Global'
        self.current_country: Place = self.manager.countries[0]

        self.current_state_txt = 'All'

        self.current_moving_average = 1
        self.current_data_to_plot = constants.CASES
        self.current_option = constants.OPTION_CUMULATIVE

        # Populate widgets
        self.populate_widgets()

        # Set UI listeners
        self.dialog.comboBoxCountries.currentTextChanged.connect(self.handle_country_change)
        self.dialog.sliderAverage.valueChanged.connect(self.handle_slider_change)
        self.dialog.comboBoxRegions.currentTextChanged.connect(self.update_plot)
        self.dialog.radioButtonCases.clicked.connect(self.handle_change_data_to_plot)
        self.dialog.radioButtonDeaths.clicked.connect(self.handle_change_data_to_plot)
        self.dialog.radioButtonBoth.clicked.connect(self.handle_change_data_to_plot)
        self.dialog.radioButtonCumulative.clicked.connect(self.handle_change_option)
        self.dialog.radioButtonDaily.clicked.connect(self.handle_change_option)

        # Update the plot
        self.update_plot()

        # Present the dialog
        self.show()

    def populate_widgets(self):
        """
        Set default values for the combo box
        :return: None
        """
        for country in self.manager.countries:
            self.dialog.comboBoxCountries.addItem(country.name)
        pass

        self.dialog.comboBoxRegions.addItem('All')

    def handle_slider_change(self):
        """
        Update the attribute value.
        Update the label.
        Update the graph after.
        :return: None
        """
        # Get slider value
        self.current_moving_average = int(self.dialog.sliderAverage.value())

        # Update the label
        if self.current_moving_average != 1:
            text = "Average of %d days" % self.current_moving_average
        else:
            text = "Average of %d day" % self.current_moving_average
        self.dialog.labelAverageOfDays.setText(_translate("Dialog", text))

        # Update the plot
        self.update_plot()

    def handle_country_change(self):
        """
        Update the attribute value.
        Fill the combo box of states according to the selected country
        Update the graph after.
        :return: None
        """
        self.current_country_txt: str = self.dialog.comboBoxCountries.currentText()

        # Get the country selected
        self.current_country = self.manager.get_country_by_name(self.current_country_txt)

        # Clean the combo box for states
        self.dialog.comboBoxRegions.clear()

        self.dialog.comboBoxRegions.addItem('All')

        # Populate the state combo box according to the country
        for state in self.current_country.states:
            self.dialog.comboBoxRegions.addItem(state.name)

        self.update_plot()

    def handle_change_data_to_plot(self):
        """
        Update the attribute value.
        Update the graph after.
        :return: None
        """
        if self.dialog.radioButtonCases.isChecked():
            self.current_data_to_plot = constants.CASES
        elif self.dialog.radioButtonDeaths.isChecked():
            self.current_data_to_plot = constants.DEATHS
        else:
            self.current_data_to_plot = constants.CASES_AND_DEATHS

        self.update_plot()

    def handle_change_option(self):
        """
        Update the attribute value.
        Update the graph after.
        :return: None
        """
        if self.dialog.radioButtonCumulative.isChecked():
            self.current_option = constants.OPTION_CUMULATIVE
        else:
            self.current_option = constants.OPTION_DAILY

        self.update_plot()

    def update_plot(self):
        """
        Ask for the data to the manager and then call the method @paint_graph to pain the data
        :return: None
        """
        logging.info("Updating graph")

        self.current_state_txt = self.dialog.comboBoxRegions.currentText()

        cases_to_plot, deaths_to_plot = self.manager.get_data(
            country=self.current_country,
            state=self.current_state_txt,
            data_to_plot=self.current_data_to_plot,
            option=self.current_option
        )
        self.clean_graph()

        # Update the title we the data
        self.update_title()

        # Paint the data
        self.paint_graph(axis=self.ax1, data=cases_to_plot, color='tab:blue', label='Cases')
        self.paint_graph(axis=self.ax2, data=deaths_to_plot, color='tab:red', label='Deaths')

        self.dialog.mplwidget.canvas.draw()

    def paint_graph(self, axis, data, color, label):
        """
        :param axis: axis for paint the data in it
        :param data: target data to present
        :param color: color to paint
        :param label: label on the y axis
        :return: None
        """
        if data is not None:
            months = mdates.MonthLocator()
            axis.xaxis.set_major_locator(months)

            months_fmt = mdates.DateFormatter('%m/%d')
            axis.xaxis.set_major_formatter(months_fmt)

            axis.plot(data.rolling(window=self.current_moving_average).mean(), color=color)

            axis.tick_params(axis='y', labelcolor=color)
            axis.set_ylabel(label, color=color)

    def clean_graph(self):
        """
        Clean the graph from previous presented data
        :return: None
        """
        self.dialog.mplwidget.canvas.axes.clear()
        self.ax1.clear()
        self.ax2.clear()

    def update_title(self):
        """
        Update the label title according to the data presented
        :return: None
        """
        title = ''
        if self.current_option == constants.OPTION_CUMULATIVE:
            title += 'Cumulative Number of '
        else:
            title += 'Daily Number of '

        if self.current_data_to_plot == constants.CASES:
            title += 'Cases in '
        elif self.current_data_to_plot == constants.DEATHS:
            title += 'Deaths in '
        else:
            title += 'Cases and Deaths in '

        title += self.current_country_txt

        if self.current_state_txt != 'All':
            title += f"-{self.current_state_txt}"

        title += f" ({self.current_moving_average}-day mean)"

        self.dialog.labelTitle.setText(title)


if __name__ == '__main__':
    """
    Present the dialog application
    """
    logging.basicConfig(level=logging.INFO)
    logging.debug('Starting test for manager.py')
    app = QtWidgets.QApplication(sys.argv)
    dialog = DialogApplication()
    dialog.show()
    sys.exit(app.exec_())
