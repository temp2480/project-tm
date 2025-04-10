from task_mommy.models.player import Player, PlayerPreferences
from task_mommy.models.tag import Tag


test_player = Player(PlayerPreferences(
	# teasing_enjoyment=1.0,
	tags={
		Tag.ANAL: 0.8,
		Tag.ORAL: 0.73,
		Tag.DENIAL: 0.9,
		Tag.IMAGINATION: 0.4,
		Tag.PORN: 0.5,
		Tag.LICKING: 0.75,
		Tag.TOYS: 0.9,
		Tag.DILDO: 0.8,
		Tag.BUTTPLUG: 0.7,
		Tag.VIBRATING_TOY: 0.6,
		Tag.CHASTITY_CAGE: 0.9,
		Tag.SELF_BONDAGE: 0.5,
		Tag.PRECUM: 0.85,
		Tag.GENITALIA: 0.5,
		Tag.ASS_TO_MOUTH: 0.0,
	},
	# position={
	# 	PositionTag.LEGS_OVER_HEAD: 0.9,
	# }
))