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

New items and offers:
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
'''
class TestCheckout():
    def test_simple_input(self):
        assert checkout('AB') == 80
        assert checkout('AC') == 70
        assert checkout('D') == 15
        assert checkout('ABCD') == 115
        assert checkout('ABCDE') == 155

    # def test_special_offers(self):
    #     assert checkout('BB') == 45
    #     assert checkout('AAA') == 130
    #     assert checkout('AAAB') == 160
    #     assert checkout('AAABCDCDCD') == 265
    #     assert checkout('AAABAAABCBA') == 405 # 2x3A and 2B + ABC

    def test_invalid_input(self):
        assert checkout(123) == -1
        assert checkout('random words') == -1
        assert checkout(None) == -1
        assert checkout(str) == -1
        assert checkout('EFGH') == -1

