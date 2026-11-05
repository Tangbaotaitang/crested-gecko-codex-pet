# Animation and interaction

An An has nine animations: resting, moving right, moving left, waving, jumping, blocked, waiting, working, and reviewing. The artwork also includes sixteen look directions.

## An An on your desktop

An An can rest quietly on its branch, stand up, wave a little foot, or make a gentle hop. The Codex client chooses which animation to play based on task activity and interactions.

| Animation | Appearance |
| --- | --- |
| Resting | Relaxing on the cork branch |
| Moving right and left | Moving in the corresponding direction |
| Waving | Raising a front foot to say hello |
| Jumping | Making a gentle hop |
| Blocked | Showing a disappointed reaction |
| Waiting | Waiting for your response |
| Working | Standing up and focusing on work |
| Reviewing | Looking closely at the result |

## Playback behavior

The client handles pointer interactions, work animation duration, directional looking, and the system's reduced motion settings. Behavior may differ between client builds.

This repository provides animation artwork and an installation manifest. `animation.json` records the animation layout and reference timing; it does not add pointer events or task-state rules to the client.

If An An returns to a resting pose during a task or jumps when the pointer passes over it, that alone does not indicate an installation failure. First confirm that An An is selected in the pet picker, then see [Client playback behavior](CLIENT_BEHAVIOR.md).
