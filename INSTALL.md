# Install An An

Give this little cream-colored crested gecko a home on your desktop.

## Recommended: give the ZIP file directly to Codex

1. Download this project's ZIP file. On the GitHub repository page, select **Code → Download ZIP**.
2. Drag the ZIP file directly into a Codex chat, or give Codex its full local path, and say:

   > Install the An An virtual pet from this ZIP file into Codex on this computer. Use the included artwork and verify that the installation succeeds.

3. Let Codex extract, validate, and install the pet locally.
4. After installation, open **Settings → Pets → Refresh** and select **An An**.
5. Enter `/pet` in Codex to show your desktop companion.

For more detailed installation instructions, also give Codex [INSTALL_PROMPT.txt](INSTALL_PROMPT.txt).

## Alternative: start from pet settings

1. Extract this project and open the extracted folder in Codex.
2. Open **Settings → Pets → Create pet** to load the app's bundled pet workflow.
3. Send the contents of [INSTALL_PROMPT.txt](INSTALL_PROMPT.txt) in that chat so Codex installs the existing artwork from this repository.
4. Return to **Settings → Pets → Refresh**, select **An An**, and enter `/pet` to show it.

Menu names may change with client updates. See the [official Pets guide](https://learn.chatgpt.com/docs/pets).

## Notes for the installation assistant

- Install a local desktop pet for Codex on this computer.
- Use `assets/anan.png` and `pet.json`. Preserve the transparent background, image dimensions, and existing animations.
- Place `pet.json` and `assets/anan.png`, with the same relative paths, inside the local `an-an-crested-gecko` pet directory. Use the pet directory location specified by the current app's bundled installation instructions.
- Preserve the value of `spriteVersionNumber` in `pet.json`; the app needs this format field to read the artwork.
- `animation.json` describes the animations and does not replace the installation manifest.
- Verify the installed files. Only report that An An is active in the interface after confirming that the user has refreshed the list and selected it.

## Troubleshooting

- **An An is missing from the pet list:** select Refresh first. If it is still missing, ask Codex to check the local installation directory and the artwork path in `pet.json`.
- **Unsupported dimensions or layout:** ask Codex to check the manifest's format field against the current app's pet requirements while preserving the original image dimensions.
- **A white rectangle appears around the pet:** make sure the installed file is `assets/anan.png`, rather than a preview GIF or screenshot.
- **The pet does not animate:** check whether your system has reduced motion enabled.
- **The pet rests during a task, or interactions behave differently than expected:** the client controls playback. See [Animation and interaction](INTERACTION.md).
- **Pet settings are unavailable:** check for client updates and whether the feature is available in your workspace.
