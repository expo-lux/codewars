# https://www.codewars.com/kata/51fda2d95d6efda45e00004e
# 4 kuy
import codewars_test as test


class User:
    def __init__(self):
        self.__rank = -8
        self.__progress = 0

    @staticmethod
    def check_rank(rank: int):
        if rank not in range(-8, 9) or rank == 0:
            raise Exception(f"Invalid rank {rank}")

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value):
        self.check_rank(value)
        self.__rank = value

    def __level_up(self):
        if self.rank != -1:
            self.rank += 1
        else:
            self.rank += 2

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        unused_points = value
        while unused_points >= 100 and self.rank < 8:
            self.__level_up()
            unused_points -= 100
        self.__progress = 0 if self.rank == 8 else unused_points

    @staticmethod
    def same_sign(rank1, rank2):
        return rank1 * rank2 > 0

    def inc_progress(self, activity_rank: int):
        self.check_rank(activity_rank)
        if activity_rank == self.rank:
            self.progress += 3
            return
        if self.same_sign(activity_rank, self.rank):
            if activity_rank + 1 == self.rank:
                self.progress += 1
            elif activity_rank > self.rank:
                self.progress += 10 * (activity_rank - self.rank) ** 2
        else:
            if activity_rank + 2 == self.rank:
                self.progress += 1
            elif activity_rank > self.rank:
                self.progress += 10 * (activity_rank - self.rank - 1) ** 2


user = User()
test.assert_equals(user.rank, -8)
test.assert_equals(user.progress, 0)
user.inc_progress(-7)
test.assert_equals(user.progress, 10)
user.inc_progress(-5)
test.assert_equals(user.progress, 0)
test.assert_equals(user.rank, -7)

activities = [7, 1, 8, 7, 7, -3, -5, 8, -4, -3]
x = User()
for item in activities:
    x.inc_progress(item)
