# Client playback behavior

## What this repository provides

This repository provides An An's transparent animation artwork, previews, animation metadata, and local installation manifest. Crested gecko lovers can use Codex's desktop pet feature to keep it nearby in a corner of the screen.

## What the client controls

The client controls visibility, size, animation triggers, directional interaction, and the relationship between task activity and animation. Behavior depends on the app you are using.

For example, standing up when a task begins does not guarantee that the work animation continues until the task ends. Including a waving animation does not guarantee that moving the pointer over the pet triggers a wave. Repository previews show the available artwork; they do not define fixed event bindings.

## Troubleshooting steps

1. Open **Settings → Pets**, refresh the list, and confirm that **An An** is selected.
2. Enter `/pet` to show the pet.
3. If only a still image appears, check your system's reduced motion settings.
4. If the pet is blank or the image looks incorrect, ask Codex to check `pet.json`, the relative artwork path, and image dimensions.
5. If the artwork displays correctly but triggers behave differently than expected, consult the [official Pets guide](https://learn.chatgpt.com/docs/pets) for the current client.

Installation uses the local pet directory and manifest supported by the app.
