from pprint import pprint
from task_mommy.data.interactions import INTERACTIONS
from task_mommy.models.interaction import Interaction
from task_mommy.models.session.context import SessionContext
from task_mommy.models.session.section import SessionSection
from task_mommy.data.themes import ANAL_TRAINING, BUTTPLUG_TRAINING, ORAL_TRAINING
from task_mommy.data.characters.freya import FREYA_CHARACTER
from task_mommy.data.player import test_player
from task_mommy.models.tag import Tag
from task_mommy.models.theme import Theme
from task_mommy.systems.interaction_picker import pick_interaction
from task_mommy.systems.theme_picker import pick_theme

def main():
	all_themes = [ANAL_TRAINING, ORAL_TRAINING, BUTTPLUG_TRAINING]
	mapped_interactions: dict[str, Interaction] = {interaction.id: interaction for interaction in INTERACTIONS}


	while True:
		character = FREYA_CHARACTER
		player = test_player

		disabled_tags = set(
			tag
			for prefs in [player.preferences.tags, character.preferences.tags]
			for tag, pref in prefs.items()
			if pref == 0.0
		)

		disabled_themes = [
			theme for theme in all_themes
			if any(
				tag in disabled_tags
				for section_tags in theme.section_tags.values()
				for tag in section_tags
			)
		]

		disabled_interactions = [
			interaction for interaction in INTERACTIONS
			if any(tag in disabled_tags for tag in interaction.tags)
		]

		available_themes = [theme for theme in all_themes if theme not in disabled_themes]

		theme = pick_theme(
			character.preferences,
			player.preferences,
			all_themes
		)
		
	# 	ctx = SessionContext(
	# 		theme,
	# 		player,
	# 		character,
	# 	)

	# 	print(ctx.character.get_dialogue('character_intro'))
	# 	# print(ctx.character.get_dialogue('teasing_intro'))
		
	# 	ctx.current_section = SessionSection.PREP

	# 	interaction = pick_interaction(
	# 		INTERACTIONS,
	# 		ctx,
	# 	)

		print('\n\n\n---------------------------------------')
		again = input()

