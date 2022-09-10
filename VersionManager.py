# https://www.codewars.com/kata/5bc7bb444be9774f100000c3

class VersionManager:
    @staticmethod
    def check_version(val):
        try:
            x = int(val)
            return x
        except ValueError:
            raise Exception("Error occured while parsing version!")

    def __init__(self, version=''):
        self._init(version)
        self.__release_history = []

    def _init(self, version):
        if version:
            dot_count = version.count('.')
            if dot_count == 0:
                self.__major = self.check_version(version)
                self.__minor, self.__patch = 0, 0
            elif dot_count == 1:
                self.__major = self.check_version(version.split('.')[0])
                self.__minor = self.check_version(version.split('.')[1])
                self.__patch = 0
            else:
                self.__major = self.check_version(version.split('.')[0])
                self.__minor = self.check_version(version.split('.')[1])
                self.__patch = self.check_version(version.split('.')[2])
        else:
            self.__major, self.__minor, self.__patch = 0, 0, 1

    def inc_release(self):
        self.__release_history.append(self.release())

    def major(self):
        self.inc_release()
        self.__major += 1
        self.__minor, self.__patch = 0, 0
        return self

    def minor(self):
        self.inc_release()
        self.__minor += 1
        self.__patch = 0
        return self

    def patch(self):
        self.inc_release()
        self.__patch += 1
        return self

    def __repr__(self):
        return self.release()

    def release(self):
        return f"{self.__major}.{self.__minor}.{self.__patch}"

    def rollback(self):
        if self.__release_history:  # at least one release in history
            self._init(self.__release_history[-1])
            self.__release_history.pop()
        else:
            raise Exception("Cannot rollback!")
        return self


import codewars_test as test

a = VersionManager()
print(a.release())
a.major()
a.major()
print(a.release())
a.rollback()
a.rollback()
print(a.release())



@test.describe("Sample tests")
def sample_tests():
    @test.it("Initialization tests")
    def it_1():
        test.assert_equals(VersionManager().release(), "0.0.1", "Default initial version")
        test.assert_equals(VersionManager("").release(), "0.0.1", "Default initial version")
        test.assert_equals(VersionManager("1.2.3").release(), "1.2.3", "No version changes")
        test.assert_equals(VersionManager("1.2.3.4").release(), "1.2.3", "No version changes")
        test.assert_equals(VersionManager("1.2.3.d").release(), "1.2.3", "No version changes")
        test.assert_equals(VersionManager("1").release(), "1.0.0", "Default minor version is 0")
        test.assert_equals(VersionManager("1.1").release(), "1.1.0", "Default patch is 0")

    @test.it("Major releases tests")
    def it_2():
        test.assert_equals(VersionManager().major().release(), "1.0.0")
        test.assert_equals(VersionManager("1.2.3").major().release(), "2.0.0")
        test.assert_equals(VersionManager("1.2.3").major().major().release(), "3.0.0")

    @test.it("Minor releases tests")
    def it_3():
        test.assert_equals(VersionManager().minor().release(), "0.1.0")
        test.assert_equals(VersionManager("1.2.3").minor().release(), "1.3.0")
        test.assert_equals(VersionManager("1").minor().release(), "1.1.0")
        test.assert_equals(VersionManager("4").minor().minor().release(), "4.2.0")

    @test.it("Patch releases tests")
    def it_4():
        test.assert_equals(VersionManager().patch().release(), "0.0.2")
        test.assert_equals(VersionManager("1.2.3").patch().release(), "1.2.4")
        test.assert_equals(VersionManager("4").patch().patch().release(), "4.0.2")

    @test.it("Rollbacks tests")
    def it_5():
        test.assert_equals(VersionManager().major().rollback().release(), "0.0.1")
        test.assert_equals(VersionManager().minor().rollback().release(), "0.0.1")
        test.assert_equals(VersionManager().patch().rollback().release(), "0.0.1")
        test.assert_equals(VersionManager().major().patch().rollback().release(), "1.0.0")
        test.assert_equals(VersionManager().major().patch().rollback().major().rollback().release(), "1.0.0")

    @test.it("Seperated calls")
    def it_6():
        m = VersionManager("1.2.3")
        m.major()
        m.minor()
        test.assert_equals(m.release(), "2.1.0")

    @test.it("Exception calls")
    def it_7():
        try:
            VersionManager("a.b.c")
            test.fail("Should throw when initial version cannot be parsed")
        except Exception as e:
            test.assert_equals(str(e), "Error occured while parsing version!")

        try:
            VersionManager().rollback()
            test.fail("Should throw when cannot rollback")
        except Exception as e:
            test.assert_equals(str(e), "Cannot rollback!")
