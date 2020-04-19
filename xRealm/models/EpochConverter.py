import time


# call this method by importing it into your class and the directly calling "EpochConverter.get_time(insert_time)"
class EpochConverter:
    @staticmethod
    def get_date(epoch_time):
        return time.strftime('%y-%m-%d', time.localtime(epoch_time))
    @staticmethod
    def get_time(epoch_time):
        return time.strftime('%H:%M:%S', time.localtime(epoch_time))
