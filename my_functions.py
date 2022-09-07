import argparse
import datetime


def valid_date(s: str) -> str:
    """
    A function to verify that the START_DATE and END_DATE are in the right format of `%Y-%m-%d`

    Parameters
    ----------
    s : an str in the form YYYY-mm-dd
    """
    try:
        # return datetime.strptime(s, "%Y-%m-%d")
        datetime.strptime(s, "%Y-%m-%d")
        return s
    except ValueError:
        msg = "not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)