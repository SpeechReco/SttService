import json
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Analysis:
    id: int
    recordingID: int
    title: str
    textURI: str
    creationDate: str
    transcription: str

    def to_dict(self):
        return {
            "id": self.id,
            "recordingID": self.recordingID,
            "title": self.title,
            "textURI": self.textURI,
            "creationDate": self.creationDate,
            "transcription": self.transcription
        }
