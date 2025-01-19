#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime


class Runtime():
    """This class compute duration time between TaskRuntime.start() and TaskRuntime.stop() call"""

    def __init__(self):

        self.__startTime = None
        self.__stopTime = None
        self.__duration = 0
        self.__averageTimes = []
        self.__maxAverageValues = 10

    def start(self):
        """Save start time"""
        self.__startTime = datetime.now()

    def stop(self):
        """Save end time"""
        self.__stopTime = datetime.now()
        self.__duration = self.__stopTime - self.__startTime

        if(len(self.__averageTimes)<=self.__maxAverageValues):
            self.__averageTimes.append(self.__duration.total_seconds())

    def runtime(self):
        """Return duration in s"""
        return self.__duration

    def averageRuntime(self):
        """Return average duration time"""
        time = 0
        for t in self.__averageTimes:
            time+=t
        return time/len(self.__averageTimes)