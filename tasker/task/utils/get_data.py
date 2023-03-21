import csv
import os
from xlsx2csv import Xlsx2csv


def get_csv_data(filename: str) -> tuple:
    """
    Gets csv filename and extracting sn, print, pan, momt, mozk values into tuples
    """
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter=";", quotechar='"')
        next(reader, None)

        sn_list, print_list, card_type_list, pan_list, momt, mozk = (
            [],
            [],
            [],
            [],
            [],
            [],
        )

        for row in reader:
            sn_list.append(row[0])  # sn
            print_list.append(row[1])  # print
            card_type_list.append(row[5])  # card type
            pan_list.append(row[4])  # pan
            momt.append(row[2])  # momt
            mozk.append(row[3])  # mozk

    return (
        tuple(sn_list),
        tuple(print_list),
        tuple(card_type_list),
        tuple(pan_list),
        tuple(momt),
        tuple(mozk),
    )


def extract_data(filename: str) -> tuple:
    """
    Gets csv filename,
    converts a file to the csv format if the file is in the xlsx format
    returns extracted sn, print, pan, momt, mozk values
    """
    csv_file = "output_file.csv"

    # checking file format
    if filename.endswith(".csv"):
        sn_list, print_list, card_type_list, pan_list, momt, mozk = get_csv_data(
            filename
        )
    elif filename.endswith(".xlsx"):
        Xlsx2csv(filename, outputencoding="utf-8", delimiter=";").convert(csv_file)

        sn_list, print_list, card_type_list, pan_list, momt, mozk = get_csv_data(
            csv_file
        )
        os.remove(csv_file)
    else:
        raise Exception("Используйте файлы с расширением xlsx или csv!")
    return sn_list, print_list, card_type_list, pan_list, momt, mozk
