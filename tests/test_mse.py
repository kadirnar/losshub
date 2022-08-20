import unittest

class TestMSE(unittest.TestCase):
    def test_mse(self):
        from  loss_hub.losses import Mse
        
        logits = [0.1, 0.2, 0.3, 0.4, 0.5]
        labels = [0.1, 0.3, 0.3, 0.4, 0.2]
        
        mse = Mse(labels, logits)
        self.assertEqual(mse, 0.0)

if __name__ == '__main__':
    unittest.main()
        