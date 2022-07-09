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

New offers:
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
+------+-------+------------------------+
'''


class TestCheckout():
    def skip_test_simple_input(self):
        assert checkout('AB') == 80
        assert checkout('AC') == 70
        assert checkout('D') == 15
        assert checkout('ABCD') == 115
        assert checkout('ABCDE') == 155

    def test_special_offers(self):
        assert checkout('BB') == 45
        assert checkout('AAA') == 130
        assert checkout('AAAB') == 160
        assert checkout('AAABCDCDCD') == 265
        assert checkout('AAAAAAAAA') == 380 # 9A = 200 + 130 + 50
        assert checkout('AAAAAAAAABB') == 425 # 9A, 2B = 380 + 45
        assert checkout('AAAAAAAAABBBBB') == 500 # 9A, 5B = 380 + 120
        assert checkout('EE') == 80
        assert checkout('EEB') == 80
        assert checkout('EEBB') == 110 # E rule is expected to work first
        assert checkout('FFF') == 20 
        assert checkout('FFFFF') == 40 
        assert checkout('FFFFFFF') == 50 # 7F, 2F + 1, 2F + 1 and + 1 more = 50

    def skip_test_invalid_input(self):
        assert checkout(123) == -1
        assert checkout('random words') == -1
        assert checkout(None) == -1
        assert checkout(str) == -1
        assert checkout('EFGH') == -1




