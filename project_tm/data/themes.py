from task_mommy.models.session.section import SessionSection
from task_mommy.models.tag import Tag
from task_mommy.models.theme import Theme


ANAL_TRAINING = Theme(
	{
		SessionSection.TEASING: [Tag.DILDO],
		SessionSection.MAIN_ACTION: [Tag.DILDO, Tag.ANAL],
		SessionSection.ORGASM: [],
	}
)

ORAL_TRAINING = Theme(
	{
		SessionSection.TEASING: [Tag.ORAL],
		SessionSection.MAIN_ACTION: [Tag.ORAL],
		SessionSection.ORGASM: [],
	}
)

BUTTPLUG_TRAINING = Theme(
	{
		SessionSection.TEASING: [],
		SessionSection.MAIN_ACTION: [Tag.BUTTPLUG, Tag.ANAL],
		SessionSection.ORGASM: [],
	}
)
