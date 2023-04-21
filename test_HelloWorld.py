import unittest
import HelloWorld

class TestHelloWorld(unittest.TestCase):
        
        def test_helloWorld(self):
        
            self.assertEqual(HelloWorld.helloWorld(), "HelloWorld")



if __name__ =='__main__':
      
      unittest.main()
        
        
        
