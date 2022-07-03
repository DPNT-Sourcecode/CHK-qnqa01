from solutions.HLO import hello


class TestSum():
    def test_sum(self):
        assert hello('Jonh') == "Hello, John!"
