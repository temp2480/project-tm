from task_mommy.models.character import Character, CharacterPreferences
from task_mommy.models.tag import Tag

DIALOGUES = { 
	'character_intro': "I don’t play nice. I take control, I make you beg. You’ll catch on soon enough.",
	'teasing_intro': "Look at you, already squirming. Adorable. But we’re doing this my way—let’s see how much you can handle.",
	'put_chastity_cage_on': "Put the chastity cage on. You don’t decide when it comes off. I do.",
	'put_precum_on_lips': "Smear your precum on your lips. Let it sit there. You’re wearing it now—like a mark of mine.",
	'put_precum_on_tongue': "Stick out your tongue. Let your precum pool there. Keep it there until I let you swallow.",
	'put_precum_on_finger_and_lick': "Coat your finger with precum. Slowly clean it off with your tongue. Savor it.",
	'put_precum_on_dildo_and_lick': "Drip your precum on your toy, then lick it off slowly. It’s for me, not you.",
	'rub_precum_on_butthole': "Rub your precum over your hole. Get dirty, make a mess. I’m in control here.",
	'let_precum_drip_on_tongue': "Legs up, mouth open. Let your precum drip on your tongue. Don’t swallow until I say.",
	'let_precum_drip_on_face': "Legs up. Chin high. Let your precum drip onto your face. Keep your mouth shut.",
	'hold_penis_and_breathe_deeply_for_duration': "Hold your little dick. Breathe deeply. You won’t be released until I say.",
	'pull_back_foreskin_and_hold_for_duration': "Pull back your foreskin and hold it. Don’t move until I tell you.",
	'rub_fingertip_around_genitalia_tip_slowly': "Rub your fingertip around your cock’s tip, slowly. You can’t rush this.",
	'lightly_tap_genitalia_tip_with_fingers': "Tap the tip of your cock lightly. Just enough to remind you who’s in charge.",
	'press_finger_gently_against_butthole': "Press your finger gently against your hole. Feel the pressure. You’re mine now.",
	'circle_finger_around_butthole': "Circle your finger around your hole. No rush. Take your time.",
	'rub_dildo_against_butthole': "Rub your dildo against your hole. Don’t insert it yet. I decide when.",
	'watch_porn_no_touching': "Watch the porn, but no touching. You’ll get nothing until I decide.",
	'tap_chastity_cage_lightly': "Tap your chastity cage lightly. Feel the reminder of who controls you.",
	'imagine_next_step_while_in_chastity_cage': "You’re locked up and aching… now imagine what I’d do next if you weren’t. Think hard. No touching.",
	'recall_favorite_orgasm_memory': "Think about the best orgasm you’ve ever had. Feel it creeping back into your mind. Now realize you’re not getting that today.",
	'denied_touch_while_watching_porn': "Start playing your filthiest porn. Hands behind your back. You’re going to sit there and ache while you watch what you *wish* you were allowed to do.",
	'lick_finger_and_imagine_your_taste': "Lick your finger. Pretend it’s you — like you just finished yourself off. How would you taste? Would I make you swallow?",
	'slowly_grip_and_release_genitalia_for_duration': "Wrap your hand around that pathetic thing. Grip it. Release. Slow. Repeating. But don’t you dare enjoy it.",
	'denied_touch_while_restrained': "All tied up, hmm? That’s cute. Now just sit there, aching and useless. No relief. Just thoughts.",
	'think_about_what_you_want_to_do': "Close your eyes and picture it — what would you do if I let you? Get yourself all worked up, just to stay still.",
	'rub_finger_lightly_against_dildo': "Just your finger. Just the tip. Tease that toy like you *wish* it was inside you. But not yet.",
	'imagine_using_a_toy_on_yourself': "Think about sliding it in. Think about how deep you’d go. How you’d moan. But it’s all just in your head, slut.",
}

FREYA_CHARACTER = Character(
	'Freya',
	DIALOGUES,
	CharacterPreferences(
		{
			Tag.ANAL: 0.7,
			Tag.ORAL: 0.65,
			Tag.DENIAL: 1.0,
			Tag.IMAGINATION: 0.8,
			Tag.PORN: 0.2,
			Tag.LICKING: 0.7,
			Tag.TOYS: 0.7,
			Tag.DILDO: 0.85,
			Tag.BUTTPLUG: 0.85,
			Tag.VIBRATING_TOY: 0.75,
			Tag.CHASTITY_CAGE: 0.95,
			Tag.PRECUM: 0.75,
			Tag.GENITALIA: 0.45,
			Tag.ASS_TO_MOUTH: 0.8,
			Tag.SELF_BONDAGE: 0.9,
		}
	)
)

# freya_character = Character(
# 	'Freya',
# 	DIALOGUES,
# 	CharacterPreferences(
# 		teasing_enjoyment=0.95,
# 		categories={
# 			CategoryTag.ANAL: 0.7,
# 			CategoryTag.ORAL: 0.65,
# 			CategoryTag.DENIAL: 1.0,
# 			CategoryTag.IMAGINATION: 0.8,
# 			CategoryTag.PORN: 0.2,
# 			CategoryTag.LICKING: 0.7,
# 			CategoryTag.TOYS: 0.7,
# 			CategoryTag.DILDO: 0.85,
# 			CategoryTag.VIBRATING_TOY: 0.75,
# 			CategoryTag.CHASTITY_CAGE: 0.95,
# 			CategoryTag.PRECUM: 0.75,
# 			CategoryTag.GENITALIA: 0.45,
# 			CategoryTag.A2M: 0.8,
# 			CategoryTag.SELF_BONDAGE: 0.9,
# 		},
# 		position={
# 			PositionTag.LEGS_OVER_HEAD: 0.9,
# 		}
# 	)
# )
