from dataclasses import dataclass


@dataclass
class Recording:
    id: int
    userID: int
    title: str
    recordingURI: str
    creationDate: str
