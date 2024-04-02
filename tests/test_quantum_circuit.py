import sys
import unittest
from quantum_package.quantum_library import QuantumCircuit
from quantum_package.config import load_config

class TestQuantumCircuit(unittest.TestCase):
    """
    Test case for the QuantumCircuit class.
    """

    def setUp(self):
        """
        Set up testing environment. This method is called before each test.
        """
        self.qubit = QuantumCircuit([1, 0])

    def test_apply_pauli_gate(self):
        """
        Test the apply_gate method of the QuantumCircuit class.
        """
        pauli_x = [[0, 1], [1, 0]]
        self.assertEqual(self.qubit.apply_gate(pauli_x), [0, 1])

class TestLoadConfig(unittest.TestCase):
    """
    Test case for the load_config function.
    """

    def test_load_config(self):
        """
        Test the load_config function.
        """
        config = load_config('/Users/afnanarshad/Desktop/Practice 2/input_parameters.yaml')
        self.assertEqual(config, {'initial_state': [1, 0], 'pauli_x': [[0, 1], [1, 0]]})

if __name__ == '__main__':
    unittest.main()
