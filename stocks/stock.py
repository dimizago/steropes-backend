import json

import numpy as np
from alpha_vantage.timeseries import TimeSeries
from statsmodels.tsa.stattools import adfuller
from django.conf import settings
import pandas as pd


class Stock:
    timeSeries = ''

    def __init__(self, output_format='pandas', indexing_type='date'):
        self.timeSeries = TimeSeries(key=settings.ALPHA_VANTAGE_KEY, output_format='pandas',
                                     indexing_type=indexing_type)

    def getIntraday(self, symbol, interval='1min', outputsize='full'):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_intraday(symbol=symbol, interval=interval, outputsize=outputsize)[0]))

    def getIntradayExtended(self, symbol, interval='15min', slice='year1month1'):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_intraday_extended(symbol=symbol, interval=interval, slice=slice)[0]))

    def getDaily(self, symbol, outputsize='full'):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_daily(symbol=symbol, outputsize=outputsize)[0]))

    def getDailyAdjusted(self, symbol, outputsize='full'):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_daily_adjusted(symbol=symbol, outputsize=outputsize))[0])

    def getWeekly(self, symbol):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_weekly(symbol=symbol))[0])

    def getWeeklyAdjusted(self, symbol):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_weekly_adjusted(symbol=symbol))[0])

    def getMonthly(self, symbol):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_monthly_adjusted(symbol=symbol))[0])

    def getMonthlyAdjusted(self, symbol):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_monthly_adjusted(symbol=symbol))[0])

    def getQuoteEndpoint(self, symbol):
        return self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_quote_endpoint(symbol=symbol))[0])

    def getSymbolSearch(self, keywords):
        stocks = self.stripColumnNumbers(pd.DataFrame(self.timeSeries.get_symbol_search(keywords=keywords)[0]))
        return stocks.reset_index().to_dict('index')

    def makeStationary(self, timeseries, num=1):
        nTs = adfuller(timeseries)
        if nTs[1] > 0.05:
            print("Difference: ", num)
            withDiff = np.log(timeseries).diff()
            timeseries = self.makeStationary(withDiff.dropna(), num + 1)

        return timeseries

    def stripColumnNumbers(self, dataFrame):
        dataFrame.columns = dataFrame.columns.str.replace(r'^\d+\.\s+', '')
        return dataFrame
