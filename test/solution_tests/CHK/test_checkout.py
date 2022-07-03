from solutions.CHK.checkout_solution import checkout
'''
Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
'''
class TestCheckout():
    def test_simple_input(self):
        assert checkout('AB') == 80
        assert checkout('AB') == 80

    def test_invalid_input(self):
        assert checkout(123) == -1
        assert checkout('random words') == -1
        assert checkout(None) == -1
        assert checkout(str) == -1
        assert checkout('EFGH') == -1
