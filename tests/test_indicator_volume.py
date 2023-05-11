# -*- coding: utf-8 -*-
from unittest import TestCase, skip
import pandas.testing as pdt
from pandas import DataFrame, Series

import talib as tal

from .config import error_analysis, sample_data, CORRELATION, CORRELATION_THRESHOLD
from .context import pandas_ta


class TestVolume(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = sample_data
        cls.data.columns = cls.data.columns.str.lower()
        cls.open = cls.data["open"]
        cls.high = cls.data["high"]
        cls.low = cls.data["low"]
        cls.close = cls.data["close"]
        if "volume" in cls.data.columns:
            cls.volume_ = cls.data["volume"]

    @classmethod
    def tearDownClass(cls):
        del cls.open
        del cls.high
        del cls.low
        del cls.close
        if hasattr(cls, "volume"):
            del cls.volume_
        del cls.data

    def setUp(self): pass
    def tearDown(self): pass


    def test_ad(self):
        """Volume: AD"""
        result = pandas_ta.ad(self.high, self.low, self.close, self.volume_, talib=False)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "AD")

        try:
            expected = tal.AD(self.high, self.low, self.close, self.volume_)
            pdt.assert_series_equal(result, expected, check_names=False)
        except AssertionError:
            try:
                corr = pandas_ta.utils.df_error_analysis(result, expected)
                self.assertGreater(corr, CORRELATION_THRESHOLD)
            except Exception as ex:
                error_analysis(result, CORRELATION, ex)

        result = pandas_ta.ad(self.high, self.low, self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "AD")

    def test_ad_open(self):
        """Volume: AD (Open)"""
        result = pandas_ta.ad(self.high, self.low, self.close, self.volume_, self.open)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "ADo")

    def test_adosc(self):
        """Volume: ADOSC"""
        result = pandas_ta.adosc(self.high, self.low, self.close, self.volume_, talib=False)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "ADOSC_3_10")

        try:
            expected = tal.ADOSC(self.high, self.low, self.close, self.volume_)
            pdt.assert_series_equal(result, expected, check_names=False)
        except AssertionError:
            try:
                corr = pandas_ta.utils.df_error_analysis(result, expected)
                self.assertGreater(corr, CORRELATION_THRESHOLD)
            except Exception as ex:
                error_analysis(result, CORRELATION, ex)

        result = pandas_ta.adosc(self.high, self.low, self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "ADOSC_3_10")

    def test_aobv(self):
        """Volume: AOBV"""
        result = pandas_ta.aobv(self.close, self.volume_)
        self.assertIsInstance(result, DataFrame)
        self.assertEqual(result.name, "AOBVe_4_12_2_2_2")

    def test_cmf(self):
        """Volume: CMF"""
        result = pandas_ta.cmf(self.high, self.low, self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "CMF_20")

    def test_efi(self):
        """Volume: EFI"""
        result = pandas_ta.efi(self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "EFI_13")

    def test_eom(self):
        """Volume: EOM"""
        result = pandas_ta.eom(self.high, self.low, self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "EOM_14_100000000")

    # @skip
    def test_kvo(self):
        """Volume: KVO"""
        result = pandas_ta.kvo(self.high, self.low, self.close, self.volume_)
        if result is not None:
            self.assertIsInstance(result, DataFrame)
            self.assertEqual(result.name, "KVO_34_55_13")

    def test_mfi(self):
        """Volume: MFI"""
        result = pandas_ta.mfi(self.high, self.low, self.close, self.volume_, talib=False)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "MFI_14")

        try:
            expected = tal.MFI(self.high, self.low, self.close, self.volume_)
            pdt.assert_series_equal(result, expected, check_names=False)
        except AssertionError:
            try:
                corr = pandas_ta.utils.df_error_analysis(result, expected)
                self.assertGreater(corr, CORRELATION_THRESHOLD)
            except Exception as ex:
                error_analysis(result, CORRELATION, ex)

        result = pandas_ta.mfi(self.high, self.low, self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "MFI_14")

    def test_nvi(self):
        """Volume: NVI"""
        result = pandas_ta.nvi(self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "NVI_1")

    def test_obv(self):
        """Volume: OBV"""
        result = pandas_ta.obv(self.close, self.volume_, talib=False)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "OBV")

        try:
            expected = tal.OBV(self.close, self.volume_)
            pdt.assert_series_equal(result, expected, check_names=False)
        except AssertionError:
            try:
                corr = pandas_ta.utils.df_error_analysis(result, expected)
                self.assertGreater(corr, CORRELATION_THRESHOLD)
            except Exception as ex:
                error_analysis(result, CORRELATION, ex)

        result = pandas_ta.obv(self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "OBV")

    def test_pvi(self):
        """Volume: PVI"""
        result = pandas_ta.pvi(self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "PVI_1")

    def test_pvol(self):
        """Volume: PVOL"""
        result = pandas_ta.pvol(self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "PVOL")

    def test_pvr(self):
        """Volume: PVR"""
        result = pandas_ta.pvr(self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "PVR")
        # sample indicator values from SPY
        # self.assertEqual(result[0], 1)
        # self.assertEqual(result[1], 3)
        # self.assertEqual(result[4], 2)
        # self.assertEqual(result[6], 4)

    def test_pvt(self):
        """Volume: PVT"""
        result = pandas_ta.pvt(self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "PVT")

    def test_vhm(self):
        """Volume: VHM"""
        result = pandas_ta.vhm(self.volume_, 30, 30)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "VHM_30")

        result = pandas_ta.vhm(self.volume_, 10, 20)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "VHM_10_20")

    def test_vp(self):
        """Volume: VP"""
        result = pandas_ta.vp(self.close, self.volume_)
        self.assertIsInstance(result, DataFrame)
        self.assertEqual(result.name, "VP_10")

    def test_vwap(self):
        """Volume: VWAP"""
        result = pandas_ta.vwap(self.high, self.low, self.close, self.volume_)
        self.assertIsInstance(result, Series)
        self.assertEqual(result.name, "VWAP_D")

        result = pandas_ta.vwap(self.high, self.low, self.close, self.volume_, bands=[1])
        self.assertIsInstance(result, DataFrame)
        self.assertEqual(result.name, "VWAP_D")

        result = pandas_ta.vwap(self.high, self.low, self.close, self.volume_, bands=[-1, 1])
        self.assertIsInstance(result, DataFrame)
        self.assertEqual(result.name, "VWAP_D")

        result = pandas_ta.vwap(self.high, self.low, self.close, self.volume_, bands=[1, 2, 4, 8])
        self.assertIsInstance(result, DataFrame)
        self.assertEqual(result.name, "VWAP_D")

        result = pandas_ta.vwap(self.high, self.low, self.close, self.volume_, bands=[1, 2.5, 4.13])
        self.assertIsInstance(result, DataFrame)
        self.assertEqual(result.name, "VWAP_D")

    def test_wb_tsv(self):
        """Volume: WB TSV"""
        result = pandas_ta.wb_tsv(self.close, self.volume_)
        self.assertIsInstance(result, DataFrame)
        self.assertEqual(result.name, "TSV_18_10")
