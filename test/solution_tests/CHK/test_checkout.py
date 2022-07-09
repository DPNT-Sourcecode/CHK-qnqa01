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

Even more prices: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+

and the final:
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+
'''


class TestCheckout():
    def test_simple_input(self):
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

    def test_offers_for_h(self):
        assert checkout('H' * 5) == 45
        assert checkout('H' * 10) == 80
        assert checkout('H' * 15) == 125
        assert checkout('H' * 16) == 135

    def test_offers_for_k(self):
        assert checkout('K') == 80
        assert checkout('K' * 2) == 150
        assert checkout('K' * 3) == 230

    def test_offers_for_n(self):
        assert checkout('NNN') == 120
        assert checkout('NNNM') == 120
        assert checkout('NNNMM') == 135

    def test_offers_for_p(self):
        assert checkout('P' * 4) == 200
        assert checkout('P' * 5) == 200
        assert checkout('P' * 6) == 250
        assert checkout('P' * 10) == 400
        assert checkout('P' * 11) == 450

    def test_offers_for_q(self):
        assert checkout('Q' * 2) == 60
        assert checkout('Q' * 3) == 80
        assert checkout('Q' * 4) == 110

    def test_offers_for_r(self):
        assert checkout('R' * 3) == 150
        assert checkout('RRRQ') == 150
        assert checkout('RRRQQ') == 180

    def test_offers_for_u(self):
        assert checkout('U' * 2) == 80
        assert checkout('U' * 3) == 120
        assert checkout('U' * 4) == 120
        assert checkout('U' * 8) == 240
        assert checkout('U' * 9) == 280

    def test_offers_for_v(self):
        assert checkout('V') == 50
        assert checkout('V' * 2) == 90
        assert checkout('V' * 3) == 130
        assert checkout('V' * 4) == 180
        assert checkout('V' * 6) == 260

    def test_invalid_input(self):
        assert checkout(123) == -1
        assert checkout('random words') == -1
        assert checkout(None) == -1
        assert checkout(str) == -1

