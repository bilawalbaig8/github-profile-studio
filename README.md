# GitHub Profile Studio

An agent-neutral skill for creating personal GitHub profiles with illustrated characters, expressive layouts, and optional animation. It starts with your goals and references, develops a character and palette with you, then produces a checked README and reusable assets.

GPT-based agents are the preferred authoring experience when built-in image generation is available. Claude and other agents can follow the same Markdown workflow with their available tools. Image generation, previews, file access, and publishing depend on the host; this repository does not guarantee identical capabilities across agents.

## Install or use

1. Clone or download this repository.
2. **Codex:** copy `skills/github-profile-studio` into `.agents/skills/` in your project or `~/.agents/skills/` for your user, then start a new session and invoke `$github-profile-studio`. Confirm discovery in your host before assuming installation succeeded. See the [official Codex skills documentation](https://developers.openai.com/codex/skills).
3. **Claude Code:** copy that folder into `~/.claude/skills/` or a project `.claude/skills/`, then invoke `/github-profile-studio`. See the [official Claude Code skills documentation](https://code.claude.com/docs/en/skills) and confirm discovery in your installation.
4. **Any agent/manual:** attach or open [SKILL.md](skills/github-profile-studio/SKILL.md), ask the agent to follow it, and make the linked references and templates accessible. This does not install anything into an account.

No API key, framework, or dependency installation is required to read and use the workflow. The optional validator requires Python 3.10+ and only its standard library.

## Start here

> Use GitHub Profile Studio to create my illustrated profile. Start with targeted questions, then ask for my reference photos and LinkedIn link. Show me a character sheet and visible palette options before producing the final artwork. Do not publish until my authorization covers the exact destination and files.

For revisions:

> Update my existing profile using this approved character sheet and palette. Preserve my face likeness and approved pose, keep the character looking toward the text, and make a static version for reduced motion. Verify all career claims with me.

For a host without image generation:

> Follow the skill using my supplied artwork. Prepare a character-sheet brief for my designer, keep that approval pending, and work on the factual content and editable layout meanwhile. Do not pretend to have generated or reviewed an image.

Read the [workflow](docs/workflow.md) for deliverables, boundaries, and a fictional example. Run `python scripts/validate_project.py` to check this package. The script checks package structure and local links; it does not render or validate a finished GitHub profile.

## What you receive

- A personalized README with verified claims, useful links, and descriptive image alternatives.
- Approved character and color references, editable source art/layout, separate animation layers, and export files.
- An optional GIF with a static fallback and a recorded publication scope.

This is a workflow, not a gallery of someone else's identity or artwork. Photos, exports, and working files belong outside the public skill package. Check any assets' licensing before publication.

Contributions are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under [MIT](LICENSE).

## Creator and support

Created by [Bilawal Baig](https://github.com/bilawalbaig8). Generated profile READMEs include this visible footer by default, shown in the preview for both animated and static versions:

Built with [GitHub Profile Studio](https://github.com/bilawalbaig8/github-profile-studio) by [Bilawal Baig](https://github.com/bilawalbaig8).

You may explicitly opt out of the footer. It credits the workflow's creator, not ownership or authorship of your identity, artwork, or career. The MIT license requires preserving its copyright and permission notice in distributed copies or substantial portions of the covered software; it does not require this footer on every generated output. The [license](LICENSE) is unchanged.

If the workflow helps, you can optionally [star GitHub Profile Studio](https://github.com/bilawalbaig8/github-profile-studio). The agent may offer that invitation once at successful handoff. Stars are voluntary: no automatic starring, hooks, credentials, tracking, usage gates, or repeated requests.
