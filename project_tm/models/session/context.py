from dataclasses import dataclass, field
from enum import Enum, auto

from task_mommy.models.character import Character
from task_mommy.models.player import Player
from task_mommy.models.session.section import SessionSection
from task_mommy.models.theme import Theme


@dataclass
class SessionContext:
	theme: Theme
	player: Player
	character: Character
	current_section: SessionSection = SessionSection.NONE
	already_used_interactions: list[str] = field(default_factory=list)

	# core_category: CategoryTag = None
	# teasing_satisfaction_threshold: float = 0.0
	# teasing_satisfaction: float = 0.0
	# skipped_teasing: bool = False
	# is_booty_clean: bool = False
	# is_booty_plugged: bool = True
	# is_wearing_chastity_cage: bool = False

	# def set_field(self, **fields):
	# 	for key, value in fields.items():
	# 		setattr(self, key, value)

