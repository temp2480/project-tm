from dataclasses import dataclass

from task_mommy.models.session.section import SessionSection
from task_mommy.models.tag import Tag


@dataclass
class Theme:
	section_tags: dict[SessionSection, list[Tag]]
