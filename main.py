import argparse

from process_data import ProcessData


def main():
    """
    Parse the argument and call the processing class to run all the function
    :return: None
    """
    parser = argparse.ArgumentParser(description="Data Parser")
    parser.add_argument('--csvFilePath', type=str, help='CSV File path')
    parser.add_argument('--sort', type=str, nargs='?',
                        help="Sort with Stock Name. 'asc': Ascending and 'desc': Descending")
    parser.add_argument(
        '--stockName',
        type=str,
        nargs='?',
        help="Name of the stock you are interested in"
    )
    parser.add_argument('--startDate', help="Start date")
    parser.add_argument('--endDate', help="End Date")
    args = parser.parse_args()

    process_data = ProcessData(args)
    process_data.question_one()
    process_data.question_two()
    process_data.question_three()
    process_data.question_four()


if __name__ == '__main__':
    main()
