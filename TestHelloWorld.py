import unittest
from HelloWorld import HelloWorld

class TestHelloWorld(unittest.TestCase):
    
    def setUp(self):
        self.hello_world = HelloWorld()
    
    def test_helloWorld(self):
        self.assertEqual(self.hello_world.say_hello_world(), 'Hello World!')

if __name__ == '__main__':
    unittest.main()