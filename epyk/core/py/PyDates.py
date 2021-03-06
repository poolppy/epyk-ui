"""
Common module for managing dates.

This module is a light wrapper on top of datetime in order to perform basic operations on dates.
This will also standardise the date format to YYYY-MM-DD in the Python layer to simplify the
conversion to the Javascript

All the tests in this module are using doctest
https://docs.python.org/2/library/doctest.html
"""

import time
import datetime


class PyDates(object):
  class __internal(object):
    _props, _context, jsOnLoadEvtsFnc = {}, {}, []

  def __init__(self, src=None):
    self.__src = src if src else self.__internal()

  @property
  def today(self):
    """
    Return a String date in a format YYYY-MM-DD

    Even if within the property python date object are used, this function will
    always return a string date in a specific format to guarantee and simplify the compatibility between languages
    within the components

    Example
    PyDates().today

    Documentation
    https://docs.python.org/2/library/datetime.html

    :return: A string date in the format YYYY-MM-DD
    """
    return datetime.datetime.today().strftime('%Y-%m-%d')

  @property
  def now(self):
    """
    Return the current timestamp in a format YYYY-MM-DD HH:mm:dd

    Example
    PyDates().now

    Documentation
    https://docs.python.org/2/library/datetime.html

    :return: Return a string timestamp
    """
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

  @property
  def cob(self):
    """
    Returns the last close of business date

    In this property the parameter weekdays is forced to True.

    Example
    rptObj.py.dates.cob

    :return: A string date
    """
    return self.date_from_alias("T")

  @property
  def month_end(self):
    """
    Returns the last month end date

    In this property the parameter weekdays is forced to True.

    Example
    rptObj.py.dates.month_end

    :return: A string date
    """
    return self.date_from_alias("M")

  @property
  def months(self):
    """
    Returns the list of month end dates from the beginning of the year

    In this property the parameter weekdays is forced to True.

    Example
    rptObj.py.dates.months

    :return: A list of String dates
    """
    date_split = list(map(lambda x: int(x), self.today.split("-")))
    return self.month_ends(datetime.datetime(date_split[0], 1, 1).strftime('%Y-%m-%d'), self.today)

  @property
  def quarters(self):
    """
    Return the list of quarter dates since the beginning of the year

    In this property the parameter weekdays is forced to True.

    Example
    rptObj.py.dates.quarters

    :return: A list of String dates
    """
    results = []
    for i, v in enumerate(self.months):
      if i % 3 == 2:
        results.append(v)
    return results

  def date_from_alias(self, alias, from_date=None):
    """
    Return the date corresponding to an alias code like T, T-N, M...

    Example
    >>> PyDates().date_from_alias("T", "2019-08-08")
    '2019-08-07'

    :param alias: The alias of the operation (T-3, M-2....)
    :param from_date: The start date from which the time operation is applied. Today by default

    :return: The converted date or a list of dates
    """
    if from_date is None:
      cob_date = datetime.datetime.today()
    else:
      cob_date = datetime.datetime(*map(lambda x: int(x), from_date.split("-")))
    if len(alias) > 1:
      f_type, f_count = alias[0], "".join(alias[2:])
    else:
      f_type, f_count = alias, 0
    if f_type == 'T':
      for i in range(0, int(f_count) + 1):
        if len(alias) > 1:
          if alias[1] == '+':
            cob_date = cob_date + datetime.timedelta(days=1)
            while cob_date.weekday() in [5, 6]:
              cob_date = cob_date + datetime.timedelta(days=1)
          else:
            cob_date = cob_date - datetime.timedelta(days=1)
            while cob_date.weekday() in [5, 6]:
              cob_date = cob_date - datetime.timedelta(days=1)
        else:
          cob_date = cob_date - datetime.timedelta(days=1)
          while cob_date.weekday() in [5, 6]:
            cob_date = cob_date - datetime.timedelta(days=1)
      return cob_date.strftime('%Y-%m-%d')

    if f_type == 'M':
      end_month_date = datetime.datetime(cob_date.year, cob_date.month - int(f_count), 1)
      end_month_date = end_month_date - datetime.timedelta(days=1)
      while end_month_date.weekday() in [5, 6]:
        end_month_date = end_month_date - datetime.timedelta(days=1)
      return end_month_date.strftime('%Y-%m-%d')

    if f_type == 'W':
      cob_date = cob_date - datetime.timedelta(days=1)
      while cob_date.weekday() != 4:
        cob_date = cob_date - datetime.timedelta(days=1)
      cob_date = cob_date - datetime.timedelta(days=(int(f_count) * 7))
      return cob_date.strftime('%Y-%m-%d')

    if f_type == 'Y':
      end_year_date = datetime.datetime(cob_date.year - int(f_count), 1, 1)
      end_year_date = end_year_date - datetime.timedelta(days=1)
      while end_year_date.weekday() in [5, 6]:
        end_year_date = end_year_date - datetime.timedelta(days=1)
      return end_year_date.strftime('%Y-%m-%d')

    return alias

  def date_from_excel(self, xlDate):
    """
    Convert a Excel date to a AReS standard date format YYYY-MM-DD.

    Example
    >>> PyDates().date_from_excel(39448)
    '2008-01-01'

    Documentation
    https://support.office.com/en-gb/article/date-function-e36c0c8c-4104-49da-ab83-82328b832349?ui=en-US&rs=en-GB&ad=GB

    :param xlDate:

    :return: The date as a String in the common format YYYY-MM-DD in AReS
    """
    dt = datetime.datetime.fromordinal(datetime.datetime(1900, 1, 1).toordinal() + xlDate - 2)
    return dt.strftime('%Y-%m-%d')

  def month_ends(self, from_dt, to_dt, weekdays=True):
    """
    Return the list of end of month dates between two dates

    Example
    >>> PyDates().month_ends("2019-01-01", "2019-06-05", False)
    ['2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30', '2019-05-31']

    :param from_dt: The start date in format YYYY-MM-DD
    :param to_dt: The end date in format YYYY-MM-DD
    :param weekdays: remove the weekends from the potential dates (take the day before). Default True

    :return: A list of dates.
    """
    if to_dt < from_dt:
      tmp = from_dt
      from_dt = to_dt
      to_dt = tmp
    results = []
    date_split = list(map(lambda x: int(x), from_dt.split("-")))
    end_dt = datetime.datetime(*map(lambda x: int(x), to_dt.split("-")))
    dt = datetime.datetime(date_split[0], date_split[1]+1, 1) - datetime.timedelta(days=1)
    while dt < end_dt:
      results.append(dt.strftime('%Y-%m-%d'))
      dt = datetime.datetime(dt.year + int((dt.month + 1) / 12), (dt.month + 1) % 12 + 1, 1)
      dt = dt - datetime.timedelta(days=1)
      if weekdays:
        while dt.weekday() in [5, 6]:
          dt = dt - datetime.timedelta(days=1)
    return results

  def range_dates(self, from_dt, to_dt, weekdays=True):
    """
    Get the list of dates between two dates.

    The date should be two string dates in the format YYYY-MM-DD.
    The resulting range of date will always be increasing

    Example
    >>> PyDates().range_dates("2019-01-01", "2019-01-11")
    ['2019-01-11', '2019-01-10', '2019-01-09', '2019-01-08', '2019-01-07', '2019-01-04', '2019-01-03', '2019-01-02', '2019-01-01']

    :param from_dt: The start date in format YYYY-MM-DD
    :param to_dt: The end date in format YYYY-MM-DD
    :param weekdays: remove the weekends from the potential dates (take the day before). Default True

    :return: A list of dates.
    """
    start_date = self.date_from_alias(from_dt)
    end_date = self.date_from_alias(to_dt, from_date=start_date)
    if start_date < end_date:
      start_date = self.date_from_alias(to_dt, from_date=start_date)
      end_date = self.date_from_alias(from_dt)
    dt = datetime.datetime(*map(lambda x: int(x), start_date.split('-')))
    target_date = datetime.datetime(*map(lambda x: int(x), end_date.split('-')))
    dates = [start_date]
    while dt > target_date:
      dt = dt - datetime.timedelta(days=1)
      if not dt.weekday() in [5, 6] or not weekdays:
        dates.append(dt.strftime('%Y-%m-%d'))
    return dates

  def to_server_time(self, timestamp, offset, reference=60):
    """
    Return the converted timestamp to be stored in the database.
    This conversion will be based on the offset coming from the UI to convert to common time

    Example
    >>> PyDates().to_server_time("2019-08-20 20:04:10", 2)
    '2019-08-20 21:06:10'

    :param timestamp: The client timestamp
    :param offset: The client offset time to be applied before storage in hour
    :param reference: The reference time used on the server side

    :return: The server timestamp string
    """
    date = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    date = date + datetime.timedelta(minutes=(int(offset) + reference))
    return date.strftime('%Y-%m-%d %H:%M:%S')

  def to_user_time(self, timestamp, offset, reference=60):
    """
    Return the converted timestamp to be returned to the user.
    This is converting a stored timestamp to a user one.

    Example
    >>> PyDates().to_user_time('2019-08-20 21:06:10', 2)
    '2019-08-20 20:04:10'

    :param timestamp: The server timestamp
    :param offset: The client offset time to be applied before storage
    :param reference: The reference time used on the server side

    :return: The client timestamp string
    """
    date = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    date = date + datetime.timedelta(minutes=-1 * (int(offset) + reference))
    return date.strftime('%Y-%m-%d %H:%M:%S')
