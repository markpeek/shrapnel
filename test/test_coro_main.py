import coro
import unittest

class CoroMain(unittest.TestCase):
    def test_coro_main(self):
        s = coro.tcp_sock()
        with self.assertRaises(coro.YieldFromMain):
            s.connect (('127.0.0.1', 80))

if __name__ == '__main__':
    unittest.main()
