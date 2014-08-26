import unittest
from run import Run

class RunTestCase(unittest.TestCase):
    def runTest(self):
	run = Run()
	self.assertTrue(run.number == 10, 'number is not 10')
	self.assertTrue(run.name == "name", 'name is not name')

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_reports'))
