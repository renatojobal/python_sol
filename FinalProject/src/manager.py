import pandas as pd
import numpy as np
import logging  # Library for log
import utils
from place import Place
import constants

class Manager:
    """
    Manager class
    """

    def __init__(self):
        # Read the data in the csv
        self.dataset = pd.read_csv('../data/covid_data_updated.csv', sep=',', index_col='Country')

        # Split the datasets values in different datasets
        self.dataset_deaths = self.dataset.applymap(utils.strip_value_deaths)
        self.dataset_cases = self.dataset.applymap(utils.strip_value_cases)

        self.countries = []  # List for keep the countries

        # Load the data here

        # Calculate global data
        world = Place('World', self.dataset_cases.sum(numeric_only=True), self.dataset_deaths.sum(numeric_only=True))

        # Add the World as a 'country'
        self.countries.append(world)

        # Create a country object for each row
        index_number = 0
        for index_name, row in self.dataset.iterrows():

            # Compare if the actual row belong to a previous country
            if index_name == self.countries[-1].name:

                # Add this row as an state of the previous added country
                place = Place(name=self.dataset.iloc[index_number][0],
                              cases=self.dataset_cases.iloc[index_number][1:],
                              deaths=self.dataset_deaths.iloc[index_number][1:])

                self.countries[-1].states.append(place)
                self.countries[-1].has_states = True

            else:
                # Add this row as a new country
                new_country = Place(name=index_name,
                                    cases=self.dataset_cases.iloc[index_number][1:],
                                    deaths=self.dataset_deaths.iloc[index_number][1:])
                self.countries.append(new_country)

            index_number += 1

    def get_country_by_name(self, target_name):
        """
        Search in the country list for the country
        :return: Place
        """
        for country in self.countries:
            if target_name == country.name:
                return country

    def get_data(self, country: Place, data_to_plot: int, option: int, state: str = 'All'):
        """
        Get from the correct place the specified data in the parameters
        :param country: target country
        :param data_to_plot: 1 = cases; 2 = deaths; 3 = both of them
        :param option: 1 = cumulative; 2 = daily
        :param state: if state is different from 'All' return the data from teh state, otherwise from the country
        :return: tuple(cases_to_plot, deaths_to_plot)
        """
        cases_to_plot = None
        deaths_to_plot = None

        target_place = country
        if state != 'All':
            target_place = country.get_state_by_name(state)

        if data_to_plot == constants.CASES:
            cases_to_plot = target_place.get_cases(option)
        elif data_to_plot == constants.DEATHS:
            deaths_to_plot = target_place.get_deaths(option)
        else:
            cases_to_plot = target_place.get_cases(option)
            deaths_to_plot = target_place.get_deaths(option)

        return cases_to_plot, deaths_to_plot


def _test():
    """
    Test the manager
    """
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Starting test for manager.py')

    manager = Manager()
    logging.info(len(manager.countries))

    logging.info(manager.countries[9])


if __name__ == '__main__':
    _test()
