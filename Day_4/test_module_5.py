'''
Created on 08/02/2018

@author: Utilizador
'''
import unittest
from module_5 import GetSeq

class Test(unittest.TestCase):


    def test_sequence(self):
        
        get_seq =GetSeq('ANAA', 'CYCC')
        self.assertEqual('TTTT', get_seq.get_seq_by_fasta('AAAATTTTCCCC'))
        self.assertEqual('TTTT', get_seq.get_seq_by_fasta('GGGGAAAATTTT'))
        self.assertEqual(None, get_seq.get_seq_by_fasta('GGGGAAAACTT'))
    
    def test_get_expansion_bases(self):
        
        get_seq = GetSeq ('AAAA', 'CCCC')
        self.assertEqual('[ACTG]', get_seq.get_expansion_bases('N'))
        self.assertEqual('CA[ACTG]TC', get_seq.get_expansion_bases('CANTC'))
        self.assertEqual('CA[ACTG]T[CT]', get_seq.get_expansion_bases('CANTY'))
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()