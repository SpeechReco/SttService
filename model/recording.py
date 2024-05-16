from dataclasses import dataclass
import json
from typing import Any, Dict

@dataclass
class Recording:
    id: int
    userID: int
    title: str
    recordingURI: str
    creationDate: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Recording':
        return Recording(
            id=data['id'],
            userID=data['userID'],
            title=data['title'],
            recordingURI=data['recordingURI'],
            creationDate=data['creationDate']
        )