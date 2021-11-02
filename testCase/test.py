import pytest

class Test01():

    @pytest.mark.departadd
    def test_01(self):
        print('---用例01---，属于departadd模块下')

    @pytest.mark.test1
    def test_02(self):
        print('---用例02---，属于test模块下')

    @pytest.mark.test1
    def test_03(self):
        print('---用例03---，属于test模块下')

if __name__ == '__main__':
    pytest.main(['-m','departadd'])