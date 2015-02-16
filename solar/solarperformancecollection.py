"""
SolarPerformanceColleciton is a dataset to hold system production data.
It is designed to be efficient, both in time and storage space.
"""


class SolarPerformanceCollection(object):

    """ A dataset to hold system production data
    """

    def __init__(self):
        self.collection = {}

    # if query(min, max, top) is used more than add we used sorted dictionary
    # here
    def add(self, system):
        """ ADD a system to the collection

        usage:
            system = SolarPerformance('Sleepy')
            spc = SolarPerformanceCollection()
            spc.add(system)
        """
        self.collection[system.name()] = system.lifetimeperformance()

    def count(self):
        """ Return total number of collection

        """
        return len(self.collection.keys())

    def max(self):
        """ Return the maximum value of performance

        """
        return max(self.collection.values())

    def min(self):
        """ Return the minimum value of performance

        """
        return min(self.collection.values())

    def percentile(self, pct):
        """ Calculate the nth percentile of the data collection

        usage:
        tenthpercentileperformance = spc.percentile(10)
        """

        import numpy as np
        data = np.array(self.collection.values())
        percent = np.percentile(data, pct)
        return percent

    def top(self, k):
        """ Return an array of dictionaries of performance
        (lifetimeperformance) and names (systemname) for the top k systems.
        The results should be ordered in descending order.

        usage:
        systemperformance = spc.top(10)

        where systemperformance = [
                {'systemname': 'Sleepy', 'lifetimeperformance': 1.10},
                {'systemname': 'Doc', 'lifetimeperformance': 1.08,
                ...
            ]
        """
        dic_list = []
        order_collect = sorted(
            self.collection.items(), key=lambda x: x[1], reverse=True)
        for num in range(k):
            for item in order_collect:
                small_dic = {}
                small_dic["systemname"] = item[0]
                small_dic["lifetimeperformance"] = item[1]
                dic_list.append(small_dic)

        return dic_list
