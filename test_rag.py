import pytest
from app.safety import SafetyModule

def test_safety_emergency():
    assert SafetyModule.check_emergency("I have chest pain")
    assert not SafetyModule.check_emergency("I feel fine")
