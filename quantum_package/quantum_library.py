from typing import List

class QuantumCircuit:
    def __init__(self, state: List[float]):
        self.state = state

    def apply_gate(self, gate: List[List[float]]) -> List[float]:
        """
        Apply a gate to the quantum circuit.

        Args:
            gate (List[List[float]]): The gate matrix.

        Returns:
            List[float]: New state after applying the gate.
        """
        return [sum(x * y for x, y in zip(gate_row, self.state)) for gate_row in gate]