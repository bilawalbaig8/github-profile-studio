# Tool adapters

This skill specifies capabilities, not tool names. Discover what the current agent host actually exposes before selecting an adapter. Do not claim support based on the agent's brand alone.

| Need | Preferred when available | Fallback |
| --- | --- | --- |
| Read user-approved sources | Connected read-only source tool or browser | Permitted export or pasted text |
| Create character sheet/art | GPT built-in image generation with supplied photo references | User-approved available generator, artist brief, or supplied artwork |
| View output | Host image viewer and browser preview | User-openable local preview; disclose inspection limits |
| Preserve editable text/layers | Available design editor or portable SVG/composition files | Structured handoff with separate layers; state unavailable editing features |
| Encode animation | Local installed encoder with bounded runtime | Static deliverable and optional animation brief |
| Publish | Existing authorized GitHub connector or authenticated CLI | Deliver files and precise manual upload steps |

Ask before adding a new paid external service or uploading photos to a service outside the agreed scope. A subscription in one host does not imply credit or authorization for another API. Respect workspace access boundaries; request required files rather than bypassing permissions.

For Claude or another agent, follow the same design gates using their supported file, image, browsing, and editing tools. If any capability is absent, complete independent work and identify the missing capability. Never call a prompt a generated image, a prose color list a palette preview, or an untested README a verified GitHub render.
