# Design and animation

## Identity and composition

Choose the portrait or abstract/no-face branch during intake. For the latter, do not request more photos or invent a face: present an identity board of proposed symbols, shapes, textures, layout, and orientation for approval. Mark likeness, facial pose, and photo permissions not applicable when no photos are processed. Preserve the approved board through revisions; material changes require renewed approval. Palette approval remains a separate step in both branches.

Use the approved references to maintain facial structure, hairstyle, skin tone, eyewear, and recognizable features. Stylization must not erase likeness. A character sheet should show the face clearly enough for a real approval decision, not only a tiny silhouette. Ask whether clothing, accessories, and setting represent the user's preferences. Do not make a fictional role or employer visual look factual.

Create two or three distinct palette boards with visible foreground/background blocks and sample text. Include hex codes and a legibility example; account for GitHub light/dark contexts. Possible directions include editorial cream/ink/teal, cool paper/navy/mint, or warm stone/forest/coral, but choose from the brief and show the colors. Avoid a fixed house style.

Establish layout side and text direction before posing the character. Keep gaze/body orientation directed toward the copy unless explicitly chosen otherwise. Record the approved pose and reference; do not let later animation change it without approval. Keep the face unobscured by text or motion props.

## Editable sources

Use a practical editable source format supported by the chosen tools, such as SVG with real text, a layered design file, or a documented composition project. Text should remain native and selectable in sources even when an export rasterizes it. Separate at least text, character, background, and moving effects. Where possible separate head/body/props only as needed for the planned motion; don't fabricate an unusable rig. Include dimensions, fonts and licensing/substitution notes, and export instructions.

## Motion

Prefer subtle blinking, breathing, a small prop motion, or sparse environmental movement. Preserve facial likeness and approved pose; avoid distracting flashing or large repeated movement. Plan a short seamless loop with a finite duration and bounded encoding process. Check loop seams and first/last frames; preview the actual GIF after encoding. Record frame rate, duration, dimensions, and bytes.

Provide a visually complete static PNG or safe SVG alongside every animated export. GitHub README images cannot reliably negotiate the viewer's reduced-motion preference, and an animated GIF cannot itself honor that preference. Use static artwork as the default when reduced motion is required, or provide a clearly labeled static view that works without executing scripts. Do not claim a CSS media query inside an image solves accessibility in every GitHub renderer.

Set an asset budget with the user or use a restrained initial target (for example a 1200px-wide static hero and a GIF under 5MB). Treat this as a design budget, not a GitHub platform limit. Reduce dimensions, frames, or effects when needed; preserve readable text and face detail. Avoid looping render retries beyond the skill's stopping rule.
