"""
    @author: yaunsine
    时间工具类
"""
import datetime

class TimeUtils():
    def __init__(self) -> None:
        pass
    def get_now_time(self) -> str:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now_time

if __name__ == '__main__':
    pass