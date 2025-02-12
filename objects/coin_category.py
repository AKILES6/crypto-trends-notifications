from dataclasses import dataclass
from typing import Optional
from dataclass_wizard import JSONWizard


@dataclass
class VolumeChangePercentage:
    h1: str
    h6: str
    h12: str
    h24: str


@dataclass
class Attributes:
    name: str
    description: Optional[str]
    volume_change_percentage: VolumeChangePercentage
    reserve_in_usd: str
    fdv_usd: str
    h24_volume_usd: str
    h24_tx_count: int


@dataclass
class Category(JSONWizard):
    id: str
    type: str
    attributes: Attributes
