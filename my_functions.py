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
        
# custom functions
def format_n(n, int_flag=False):
    try:
        pre, suf = n.split('.')
    except:
        return int(n.replace(',', '') or 0)
    pre = pre.replace(',', '')
    suf = int(suf)/100
    res = int(pre) + suf
    return int(res) if int_flag else res

format_n("1,000", int_flag=True)
