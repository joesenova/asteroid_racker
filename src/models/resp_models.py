from __future__ import annotations
import typing as t
import pydantic


class Links(pydantic.BaseModel):
    next: t.Optional[str]
    prev: t.Optional[str]
    self: str


class Diameters(pydantic.BaseModel):
    estimated_diameter_min: float
    estimated_diameter_max: float


class EstimatedDiameter(pydantic.BaseModel):
    kilometers: Diameters
    meters: Diameters
    miles: Diameters
    feet: Diameters


class RelativeVelocity(pydantic.BaseModel):
    kilometers_per_second: str
    kilometers_per_hour: str
    miles_per_hour: str


class MissDistance(pydantic.BaseModel):
    astronomical: str
    lunar: str
    kilometers: str
    miles: str


class CloseApproach(pydantic.BaseModel):
    close_approach_date: str
    close_approach_date_full: str
    epoch_date_close_approach: int
    relative_velocity: RelativeVelocity
    miss_distance: MissDistance
    orbiting_body: str


class NearEarthObject(pydantic.BaseModel):
    links: Links
    id: str
    neo_reference_id: str
    name: str
    nasa_jpl_url: str
    absolute_magnitude_h: float
    estimated_diameter: EstimatedDiameter
    is_potentially_hazardous_asteroid: bool
    close_approach_data: t.List[CloseApproach]
    is_sentry_object: bool


class Feed(pydantic.BaseModel):
    links: Links
    element_count: int
    near_earth_objects: t.Dict[str, t.List[NearEarthObject]]


