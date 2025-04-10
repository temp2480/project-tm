import random
from task_mommy.models.character import CharacterPreferences
from task_mommy.models.interaction import Interaction
from task_mommy.models.player import PlayerPreferences
from task_mommy.models.session.context import SessionContext
from task_mommy.models.session.section import SessionSection
from task_mommy.models.theme import Theme

def pick_interaction(
	interactions: list[Interaction],
	ctx: SessionContext,
):
	interactions = interactions.copy()

	# Remove hard "absolutely not" tasks
	interactions = _filter_out_hard_no_cases(ctx, interactions)

	# Remove tasks that have already been used
	interactions = [task for task in interactions if task.id not in ctx.already_used_interactions]

	# Remove tasks based on requirements & conditions
	interactions = _filter_out_by_requirements(ctx, interactions)

	# Remove tags that don't appear in the required tags of the theme
	if ctx.current_section != SessionSection.NONE:
		interactions = [
			interaction for interaction in interactions
			if any(tag in ctx.theme.section_tags[ctx.current_section] for tag in interaction.tags)
		]

	if not interactions:
		raise Exception('No interactions available to pick from.')

	# Step 5: Weigh tasks based on character mood
	picked_interaction = _pick_random_interaction_by_preferences(ctx, interactions)

	return picked_interaction

def _pick_random_interaction_by_preferences(ctx: SessionContext, interactions: list[Interaction]) -> Interaction:
	weights = []

	for interaction in interactions:
		char_values = [ctx.character.preferences.tags.get(tags, 0.5) for tags in interaction.tags]
		player_values = [ctx.player.preferences.tags.get(tags, 0.5) for tags in interaction.tags]

		char_pref = sum(char_values) / len(char_values) if char_values else 0.5
		player_pref = sum(player_values) / len(player_values) if player_values else 0.5

		combined_pref = (char_pref + player_pref) / 2
		weights.append(combined_pref)

	return random.choices(interactions, weights=weights, k=1)[0]

def _filter_out_hard_no_cases(ctx: SessionContext, interactions: list[Interaction]) -> list[Interaction]:
	def is_excluded(interaction: Interaction) -> bool:
		for category in interaction.tags:
			char_pref = ctx.character.preferences.tags.get(category, 0.0)
			player_pref = ctx.player.preferences.tags.get(category, 0.0)
			if char_pref == 0.0 or player_pref == 0.0:
				return True
		return False

	return [task for task in interactions if not is_excluded(task)]

def _filter_out_by_requirements(ctx: SessionContext, tasks: list[Interaction]) -> list[Interaction]:
	return [task for task in tasks if task.condition is None or task.condition(ctx)]

