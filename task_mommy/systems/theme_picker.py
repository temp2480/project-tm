import random

from task_mommy.models.character import CharacterPreferences
from task_mommy.models.player import PlayerPreferences
from task_mommy.models.tag import Tag
from task_mommy.models.theme import Theme


def pick_theme(
	character_prefs: CharacterPreferences,
	player_prefs: PlayerPreferences,
	themes: list[Theme],
) -> Theme:
	def get_all_required_tags(theme: Theme) -> set[Tag]:
		all_tags = set()
		for tags in theme.section_tags.values():
			all_tags.update(tags)
		return all_tags

	valid_themes = []
	weights = []

	for theme in themes:
		required_tags = get_all_required_tags(theme)

		if any(character_prefs.tags.get(tag, 0.0) == 0.0 for tag in required_tags):
			continue
		if any(player_prefs.tags.get(tag, 0.0) == 0.0 for tag in required_tags):
			continue

		char_values = [character_prefs.tags.get(tag, 0.5) for tag in required_tags]
		player_values = [player_prefs.tags.get(tag, 0.5) for tag in required_tags]

		char_score = sum(char_values) / len(char_values) if char_values else 0.5
		player_score = sum(player_values) / len(player_values) if player_values else 0.5

		combined_score = (char_score + player_score) / 2
		weights.append(combined_score)
		valid_themes.append(theme)

	if not valid_themes:
		raise Exception('No theme found matching the character and player preferences.')
	
	# pprint([f'{round(weights[n], 2)} | {valid_themes[n]}' for n in range(len(weights))])
	
	return random.choices(valid_themes, weights=weights, k=1)[0]
