import logging
import constants

def _calculate_daily(dataset_cumulative):
    """
    Calculate the data from the dataset with cumulative data
    :return: pandas.Series
    """
    dataset_daily = dataset_cumulative.copy()  # Create a new instance

    for index in range(1, len(dataset_cumulative)):
        aux = dataset_cumulative[index] - dataset_cumulative[index - 1]
        dataset_daily[index] = aux
    return dataset_daily


class Place:
    """
    Each instance will have his own data to present
    """

    def __init__(self, name: str, cases, deaths):
        """
        Instance from Place
        :param name: name of the place. It will appear on the screen
        :param cases: cumulative cases
        :param deaths: cumulative deaths
        """
        logging.debug(cases.head())
        self.name = name

        self.cases_cumulative = cases
        self.deaths_cumulative = deaths
        self.cases_daily = None  # Initialize it as None
        self.deaths_daily = None  # Initialize it as None

        self.has_states = False
        self.states = []

    def get_cases(self, option: int):
        """
        Return cases form the place
        :param option: 1 = cumulative; 2 = daily
        :return: pandas.Series
        """
        if option == constants.OPTION_CUMULATIVE:
            return self.cases_cumulative
        else:
            if self.cases_daily is None:
                self.cases_daily = _calculate_daily(self.cases_cumulative)

            return self.cases_daily

    def get_deaths(self, option):
        """
        Return deaths from the place
        :param option: 1 = cumulative; 2 = daily
        :return: pandas.Series
        """
        if option == constants.OPTION_CUMULATIVE:
            return self.deaths_cumulative
        else:
            if self.deaths_daily is None:
                self.deaths_daily = _calculate_daily(self.deaths_cumulative)
            return self.deaths_daily

    def get_state_by_name(self, target_state: str):
        """
        Search for the target state
        :param target_state: name of the state
        :return: Place
        """
        for state in self.states:
            if target_state == state.name:
                return state
        logging.warning('State with name ' + str(target_state) + ' not fount')
        return self

    def __str__(self):
        string = f"""
        Country name: {self.name}
        Has states: {self.has_states}
        """
        return string

    def __repr__(self):
        return self.__str__()


