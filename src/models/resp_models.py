from __future__ import annotations

import dataclasses
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

    # Calculated Values
    num_asteroids: t.Optional[int]
    num_potentially_hazardous_asteroids: t.Optional[int]
    largest_diameter_meters: t.Optional[float]
    nearest_miss_kms: t.Optional[float]

    def calc_feed_stats(self) -> None:
        self.num_asteroids = self.element_count
        self.num_potentially_hazardous_asteroids: int = 0
        self.largest_diameter_meters: float = 0.0
        self.nearest_miss_kms: float = 0.0

        for near_objects in self.near_earth_objects.values():
            for near_object in near_objects:
                if near_object.is_potentially_hazardous_asteroid:
                    self.num_potentially_hazardous_asteroids += 1

                estimated_diameter_max = near_object.estimated_diameter.meters.estimated_diameter_max
                if self.largest_diameter_meters < estimated_diameter_max:
                    self.largest_diameter_meters = estimated_diameter_max

                miss_distance = float(near_object.close_approach_data[0].miss_distance.kilometers)
                if not self.nearest_miss_kms:
                    self.nearest_miss_kms = miss_distance
                else:
                    if self.nearest_miss_kms > miss_distance:
                        self.nearest_miss_kms = miss_distance


@dataclasses.dataclass
class Stats:
    start_date: str
    end_date: str
    num_asteroids: int
    num_potentially_hazardous_asteroids: int
    largest_diameter_meters: float
    nearest_miss_kms: float


@dataclasses.dataclass
class Details:
    code: int
    http_error: str
    error_message: str
    request: str


@dataclasses.dataclass
class Error:
    error: Details
