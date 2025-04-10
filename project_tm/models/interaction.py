from dataclasses import dataclass, field
from typing import Callable

from task_mommy.models.session.context import SessionContext
from task_mommy.models.tag import Tag

@dataclass
class Interaction:
	id: str
	tags: list[Tag] = field(default_factory=list)
	on_attempt: None | Callable[[SessionContext], None] = None
	on_success: None | Callable[[SessionContext], None] = None
	condition: None | Callable[[SessionContext], bool] = None

@dataclass
class Task(Interaction):
	...
	# compatible_positions: list[Tag] = field(default_factory=list)





	# tags: list[Tag] = field(default_factory=list)

# @dataclass
# class DialogueMetadata:
# 	score: float = 0.0
# 	tags: list[Tag] = field(default_factory=list)

# class Dialogue(Enum):
# 	# Intros
# 	CHARACTER_INTRO = auto()
# 	TEASING_INTRO = auto()
# 	# Teasing
# 	TEASING_TASK_PUT_PRECUM_ON_LIPS = auto()
# 	TEASING_TASK_PUT_PRECUM_ON_TONGUE = auto()
# 	TEASING_TASK_PUT_PRECUM_ON_FINGER_AND_LICK = auto()
# 	TEASING_TASK_PUT_PRECUM_ON_DILDO_AND_LICK = auto()
# 	TEASING_RUB_PRECUM_ON_BUTTHOLE = auto()
# 	TEASING_LET_PRECUM_DRIP_ON_TONGUE = auto()
# 	TEASING_LET_PRECUM_DRIP_ON_FACE_MOUTH_CLOSED = auto()
# 	TEASING_LET_PRECUM_DRIP_ON_FACE_MOUTH_OPEN = auto()

# DIALOGUE_METADATA = {
# 	# Intros
# 	Dialogue.CHARACTER_INTRO: DialogueMetadata(),
# 	Dialogue.TEASING_INTRO: DialogueMetadata(),
# 	# Teasing
# 	Dialogue.TEASING_TASK_PUT_PRECUM_ON_LIPS: 				DialogueMetadata(4.5, tags=[Tag.TEASING, Tag.PRECUM]),
# 	Dialogue.TEASING_TASK_PUT_PRECUM_ON_TONGUE: 			DialogueMetadata(5.5, tags=[Tag.TEASING, Tag.PRECUM]),
# 	Dialogue.TEASING_TASK_PUT_PRECUM_ON_FINGER_AND_LICK: 	DialogueMetadata(5.5, tags=[Tag.TEASING, Tag.PRECUM]),
# 	Dialogue.TEASING_TASK_PUT_PRECUM_ON_DILDO_AND_LICK: 	DialogueMetadata(6.5, tags=[Tag.TEASING, Tag.PRECUM, Tag.TOY_DILDO]),
# 	Dialogue.TEASING_RUB_PRECUM_ON_BUTTHOLE: 				DialogueMetadata(7.7, tags=[Tag.TEASING, Tag.PRECUM, Tag.ANAL]),
# 	Dialogue.TEASING_LET_PRECUM_DRIP_ON_TONGUE: 			DialogueMetadata(9.3, tags=[Tag.TEASING, Tag.PRECUM, Tag.POSITION_LEGS_OVER_HEAD]),
# 	Dialogue.TEASING_LET_PRECUM_DRIP_ON_FACE_MOUTH_OPEN:	DialogueMetadata(9.5, tags=[Tag.TEASING, Tag.PRECUM, Tag.POSITION_LEGS_OVER_HEAD]),
# 	Dialogue.TEASING_LET_PRECUM_DRIP_ON_FACE_MOUTH_CLOSED:	DialogueMetadata(9.9, tags=[Tag.TEASING, Tag.PRECUM, Tag.POSITION_LEGS_OVER_HEAD]),
# }

# class DialogueTone(Enum):
# 	VERY_SWEET 		= 0
# 	SWEET 			= 1
# 	SLIGHTLY_SWEET 	= 2
# 	NEUTRAL 		= 3
# 	SLIGHTLY_CRUEL 	= 4
# 	CRUEL 			= 5
# 	VERY_CRUEL 		= 6

# @dataclass
# class DialogueLine():
# 	text: str
