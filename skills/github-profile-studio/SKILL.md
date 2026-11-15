---
name: github-profile-studio
description: Create or redesign personalized GitHub README profiles with approved illustrated characters, palettes, editable artwork, and optional animation. Use for an individual profile design, not a generic repository README.
---

# GitHub Profile Studio

Create a profile that communicates the user's real work through a cohesive illustrated identity. Adapt to their taste and available tools; do not reuse another person's likeness, profile artwork, or career history.

## Start with intake

Begin with a compact set of targeted questions about goals, audience, GitHub username/repository, style, desired sections, existing assets, motion, accessibility, timeline, and publication constraints, before offering visual concepts. Use [the intake template](templates/intake.md), grouping questions to avoid an interrogation. Request user reference photos and consent for their use, retention, likeness treatment, and public visibility. Offer an abstract/no-face alternative if photos are declined. An existing complete, approved brief can satisfy questions already answered.

Request a LinkedIn link and read only public or explicitly authorized content using the host's available browser/connector. If blocked, request a permitted export or pasted facts; do not bypass login, scrape private content, or infer facts from a URL. Ask about missing or conflicting roles, dates, projects, handles, and links. Read [sources and privacy](references/sources-and-privacy.md) before drafting factual copy.

## Approve the visual identity

Read [design and animation](references/design-and-animation.md). For a portrait, produce a character sheet from permitted references and present it for explicit approval before final artwork. Include a face view, useful angle, and proposed pose/expression. Preserve face likeness and the approved pose across later work. Face the character toward the text unless the user chooses otherwise. For the abstract/no-face branch, show an identity board with the proposed symbol, shapes, texture, composition, and orientation; obtain approval of that board instead of a face sheet. Record portrait-only fields as not applicable rather than leaving an impossible approval pending. If image generation is unavailable, prepare a designer-ready brief and keep the chosen branch's artifact approval pending until an actual sheet or board is supplied and reviewed.

Present two or three **actual visible palette examples** (rendered swatches or miniature compositions) with hex values and text contrast examples. Palette names and hex lists alone do not satisfy this step. Offer options appropriate to the brief; do not default to neon purple/orange. Obtain a palette choice before final art. Record character, pose, palette, and publication approvals independently in [project state](templates/project-state.md).

## Build and verify

Use [the design brief](templates/design-brief.md). Make factual README copy and static layout first, then optional animation. Keep native editable text and isolated character/background layers in an editable source format the user can open. Preserve source files alongside exports in the deliverable, excluding private inputs from public assets.

Use built-in GPT image generation when available and suitable; otherwise use supplied assets, an available approved generator, or an explicit handoff. Consult [tool adapters](references/tool-adapters.md) when choosing tools. Do not silently call a paid external API or claim unsupported tools/capabilities. Do not fabricate assets or previews that were not generated or inspected.

Use [GitHub delivery checks](references/github-delivery.md) before completion. Inspect the real outputs, including mobile scale, links, text readability, file size, GitHub SVG limitations, static/reduced-motion alternatives, and animation loop behavior. Bound rendering attempts: at most three render/fix passes per issue, then explain the concrete blocker and offer a static deliverable or user decision. Never wait indefinitely on a render or claim a failed export succeeded.

## Deliver and publish within scope

Present the finished README, asset preview, editable sources, manifest, and any unresolved facts. Publication requires authorization covering the exact account/repository, files, visibility, and action. Use existing authorization when it covers this work; otherwise obtain it after preparing a reviewable result. Do not change account settings or credentials to enable publishing. Verify the destination after a write and report what was actually checked. Installing a folder locally is not installation into a GitHub or agent account; verify skill discovery before claiming it works.
