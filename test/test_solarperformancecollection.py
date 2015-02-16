"""
SolarPerformanceCollection Test Set
"""

import unittest
from solar import SolarPerformanceCollection

DATA = {
    'Sneezy': 0.919177337397975,
    'Sleepy': 1.18652810676406,
    'Mickey Mouse': 1.05477555768535,
    'Dopey': 0.966604278620813,
    'Doc': 1.10329187448733,
    'Grumpy': 0.702467910341306,
    'Bashful': 1.00987703264902,
    'Happy': 1.11151164379285
}

KEYS = [key for key, value in DATA.items()]
VALUES = [value for key, value in DATA.items()]


class SolarPerformanceStub(object):

    """
    Stub out the SolarPerformance class
    """

    def __init__(self, systemname, performance):
        self.systemname = systemname
        self.performance = performance

    def name(self):
        """ Stub out name """
        return self.systemname

    def lifetimeperformance(self):
        """ Stub out lifetimeproduction """
        return self.performance


class TestSolarPerformance(unittest.TestCase):

    """
    SolarPerformanceCollection Test Set
    """

    def setUp(self):
        self.spc = SolarPerformanceCollection()
        for name, performance in DATA.items():
            system = SolarPerformanceStub(name, performance)
            self.spc.add(system)

    def tearDown(self):
        pass

    def test_count(self):
        """
        Instance should have a method to count the number of items in
        the collection
        """

        spc = self.spc
        self.assertTrue(spc.count(), len(VALUES))

    def test_min(self):
        """
        Instance should have a method to display the minimum value in
        the collection
        """

        spc = self.spc
        self.assertTrue(spc.min(), min(VALUES))

    def test_max(self):
        """
        Instance should have a method to display the maximum value in
        the collection
        """

        spc = self.spc
        self.assertTrue(spc.max(), max(VALUES))

    def test_percentile(self):
        """
        Instance should have a method to calculate the nth percentile of
        the data
        """
        spc = self.spc
        self.assertTrue(spc.percentile(1), max(VALUES))
        self.assertTrue(spc.percentile(0), min(VALUES))
        self.assertTrue(spc.percentile(0.3) <= spc.percentile(0.4))

    def test_top(self):
        """
        Instance should have a method to return the top k values of
        the collection
        """
        spc = self.spc
        test_value = sorted(VALUES)
        act_value = []
        for i in range(8):
            act_value.append(spc.top(i + 1)[0]["lifetimeperformance"])
        self.assertTrue(test_value, act_value)

if __name__ == "__main__":
    unittest.main()
