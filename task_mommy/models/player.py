from dataclasses import dataclass, field

from task_mommy.models.tag import Tag


@dataclass
class PlayerPreferences:
	# teasing_enjoyment: float
	tags: dict[Tag, float] = field(default_factory=dict)

@dataclass
class Player:
	# name: str
	preferences: PlayerPreferences
