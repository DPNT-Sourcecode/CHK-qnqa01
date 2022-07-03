from solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_simple_input(self):
        assert checout('AB') == "Hello, John!"
