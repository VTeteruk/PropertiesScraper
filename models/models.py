from dataclasses import dataclass


@dataclass
class Property:
    url: str
    title: str
    region: str
    address: str
    description: str
    images: list[str]
    price: int
    rooms: int
    square: int
