import re


def validate_data(
    sn: tuple,
    _print: tuple,
    card_type: tuple,
    pan: tuple,
    momt: tuple,
    mozk: tuple,
) -> dict:
    """
    Gets tuple of sn, print, card_type, pan, momt, mozk values
    Validate data, and returns errors if any
    """

    errors_total = {}

    card_types = [
        "01.00",
        "00.10",
        "00.11",
        "00.11",
        "00.13",
        "00.15",
        "00.16",
        "00.17",
        "00.18",
        "00.20",
        "00.21",
        "00.22",
        "00.23",
        "00.24",
        "00.25",
        "00.26",
        "00.27",
        "00.41",
        "00.42",
        "00.43",
        "00.44",
        "00.45",
        "00.46",
        "00.47",
        "00.48",
        "00.49",
    ]

    # check sn values
    sn_check = re.compile("^[A-z0-9]+$")
    for i, el in enumerate(sn, start=1):
        index = str(i)
        sn_match = sn_check.match(el)
        if not sn_match:
            errors = errors_total.get(index, [])
            errors.append(f"SN: {el}")
            errors_total[index] = errors

    # check print values
    print_check = re.compile("^[0-9]+$")
    for i, el in enumerate(_print, start=1):
        index = str(i)
        print_match = print_check.match(el)
        if not print_match:
            errors = errors_total.get(index, [])
            errors.append(f"PRINT: {el}")
            errors_total[index] = errors

    # check card type values
    for i, el in enumerate(card_type, start=1):
        index = str(i)
        if el not in card_types:
            errors = errors_total.get(index, [])
            errors.append(f"CARD TYPE: {el}")
            errors_total[index] = errors

    # check PAN19 values
    PAN19_check = re.compile("^[0-9]{19}$")
    for i, el in enumerate(pan, start=1):
        index = str(i)
        PAN19_match = PAN19_check.match(el)
        if not PAN19_match:
            errors = errors_total.get(index, [])
            errors.append(f"PAN19: {el}")
            errors_total[index] = errors

    # check momt values
    momt_check = re.compile("^[0-9]{1,3}$")
    for i, el in enumerate(momt, start=1):
        index = str(i)
        momt_match = momt_check.match(el)
        if not momt_match:
            errors = errors_total.get(index, [])
            errors.append(f"MOMT: {el}")
            errors_total[index] = errors

    # check momt values
    mozk_check = re.compile("^[0-9]{1,3}$")
    for i, el in enumerate(mozk, start=1):
        index = str(i)
        mozk_match = mozk_check.match(el)
        if not mozk_match:
            errors = errors_total.get(index, [])
            errors.append(f"MOZK: {el}")
            errors_total[index] = errors

    return errors_total
