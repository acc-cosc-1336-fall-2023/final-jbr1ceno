#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
#from src.question_a.question_a import test_config
from src.question_c.question_c import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus(self):
        dna_string1 = "GATATATGCATATACTT" #result should be (2,4,10)
        dna_string2 = "ATAT"

        #dna_string3 = "GAAATATGCATATACTT" #secondary test just incase
        #dna_string4 = "ATAT"
        print(str(get_most_likely_ancestor_consensus(dna_string1, dna_string2)))

        #print(str(get_most_likely_ancestor_consensus(dna_string3, dna_string4)))
        self.assertEqual((2,4,10), get_most_likely_ancestor_consensus(dna_string1, dna_string2))
        
        #self.assertEqual((4,10), get_most_likely_ancestor_consensus(dna_string3, dna_string4)) #secondary test just incase
