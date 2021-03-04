
def temp_validation(value):
    """

    :param value: temperature value given by the system
    :return: Boolean
    """
    min_value = 0
    max_value = 45
    return True if (value > min_value) and (value < max_value) else False


def soc_validation(value):
    """

    :param value: state of charge value given by the system
    :return: Boolean
    """
    min_value = 20
    max_value = 80
    return True if (value > min_value) and (value < max_value) else False


def cr_validation(value):
    """

    :param value: charge rate value given by the system
    :return: Boolean
    """
    max_value = 0.8
    return True if (value < max_value) else False


def battery_is_ok(temp_val, soc_val, cr_val):
    """

    :param temp_val: this is the temperature value from cpu
    :param soc_val:  this is the state of charge value
    :param cr_val:  this is the charge rate value
    :return: Boolean
    """
    final_list = [temp_validation(temp_val), soc_validation(soc_val),
                  cr_validation(cr_val)]
    return True if False not in final_list else False


if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
