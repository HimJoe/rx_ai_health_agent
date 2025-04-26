from fhirclient import client
from fhirclient.models.patient import Patient
from fhirclient.models.observation import Observation

# Simple local store for demonstration
_user_profiles = {}

class ProfileManager:
    @staticmethod
    def get_profile(user_id: str) -> dict:
        return _user_profiles.get(user_id, {})

    @staticmethod
    def update_profile(user_id: str, data: dict):
        _user_profiles[user_id] = data
