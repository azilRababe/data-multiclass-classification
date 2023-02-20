from nbresult import ChallengeResultTestCase

class TestBaseline(ChallengeResultTestCase):

    def test_accuracy(self):
        self.assertGreater(self.result.accuracy, 0.14)
        self.assertLess(self.result.accuracy, 0.16)
