"""
SolarPerformance is a class for system performance.
"""
import sqlite3
import string


class SolarPerformance(object):

    """
    """
    namelist = []
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM systems")
    for i in cursor.fetchall():
        namelist.append(i[0].encode('utf-8'))
    conn.commit()
    conn.close()

    def __init__(self, systemname):

        for i in systemname:
            if i in " " + string.punctuation:
                raise NameError("System name is not allowed.")
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM systems WHERE name = '% s'" % systemname)

        if not cursor.fetchall():
            raise NameError("System name doesn't exist.")

        self.name = systemname
        conn.commit()
        conn.close()

    @classmethod
    def names(cls):
        """
        return a name list for all the systems
        """
        return SolarPerformance.namelist

    def givename(self):
        """
        return the instance's name
        """
        return self.name

    def lifetimeperformance(self):
        """
        return the performance of the system
        """
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT SUM(actualkwh)/SUM(expectedkwh) "
            "FROM data JOIN systems ON "
            "data.systemid=systems.systemid "
            "WHERE systems.name= '% s'" % self.name)
        return cursor.fetchall()[0][0]
