import pandas as pd


class Helper:

    @classmethod
    def read_CSV(cls, filepath):
        """
        Read the CSV and convert the object column into respective data types
        :param filepath: path of the file
        :return: Dataframe (Pandas)
        """

        df = pd.read_csv(filepath)

        # Converting the date object into datetime64 format
        df['date'] = pd.to_datetime(df['date'])

        # Converting all kind of date format to one particular format of YYYY-MM-DD
        df['date'] = df['date'].dt.strftime('%Y-%m-%d')

        # Converting all object type to either float64 or int64 data type
        df['open'] = pd.to_numeric(df['open'], errors='coerce')
        df['close'] = pd.to_numeric(df['close'], errors='coerce')
        df['low'] = pd.to_numeric(df['low'], errors='coerce')
        df['high'] = pd.to_numeric(df['high'], errors='coerce')

        return df

