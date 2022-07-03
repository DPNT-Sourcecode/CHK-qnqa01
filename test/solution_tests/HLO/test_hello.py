from solutions.HLO.hello_solution import hello


class TestSum():
    def test_sum(self):
        assert hello('John') == "Hello, John!"
