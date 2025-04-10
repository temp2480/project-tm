from dataclasses import dataclass, field

from task_mommy.models.tag import Tag


@dataclass
class CharacterPreferences:
	tags: dict[Tag, float] = field(default_factory=dict)

@dataclass
class Character:
	name: str
	dialogues: dict[str, str]
	preferences: CharacterPreferences

	def get_dialogue(self, key: str) -> str:
		return self.dialogues.get(key, f'<{key}>')
