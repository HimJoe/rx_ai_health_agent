from typing import Tuple

EMERGENCY_KEYWORDS = ["chest pain", "difficulty breathing", "suicidal"]

class SafetyModule:
    @staticmethod
    def check_emergency(text: str) -> bool:
        lowered = text.lower()
        return any(kw in lowered for kw in EMERGENCY_KEYWORDS)

    @staticmethod
    def disclaimer(response: str) -> str:
        return response + "\n\n**Disclaimer:** I am not a medical professional. This is for general guidance only."
