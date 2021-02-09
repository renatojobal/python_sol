def strip_value_cases(cell):
    """
    Split a cell like "1234 567" into a list and return the first value
    :param cell: the cell form the dataset
    :return: int
    """
    try:
        if any(map(str.isdigit, cell)):  # Verify if the cell has number or not
            result = cell.split()
            return int(result[0])
        else:
            return cell
    except:
        return ''


def strip_value_deaths(cell):
    """
    Split a cell like "1234 567" into a list and return the second value
    :param cell: the cell form the dataset
    :return: int
    """
    try:
        if any(map(str.isdigit, cell)):  # Verify if the cell has number or not
            result = cell.split()
            return int(result[1])
        else:
            return cell
    except:
        return ''


# Test
if __name__ == '__main__':
    print(strip_value_deaths('115566    4654546'))
