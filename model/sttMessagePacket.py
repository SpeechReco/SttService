from dataclasses import dataclass
from typing import Any, Dict

from model.recording import Recording


@dataclass
class SttMessagePacket:
    analysis_name: str
    language: str
    speaker_amount: int
    generate_summary: bool
    recording: Recording

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'SttMessagePacket':

        return SttMessagePacket(
            analysis_name=data['analysisName'],
            language=data['language'],
            speaker_amount=data['speakerAmount'],
            generate_summary=data['generateSummary'],
            recording=Recording.from_dict(data['recording'])
        )
