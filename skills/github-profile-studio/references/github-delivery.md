# GitHub delivery checks

Verify current GitHub documentation if a decision depends on renderer behavior or platform limits. These are design checks, not a guarantee of every client rendering identically.

- Confirm the user's actual profile repository and intended branch. A standard profile README uses a repository whose name matches the username; verify the destination rather than deriving account ownership from a name.
- Use repository-relative image paths with correct casing and committed assets, or explicitly approved stable public asset URLs. Avoid local machine paths and temporary signed URLs.
- Treat SVGs as passive image documents: no JavaScript, embedded web apps, `foreignObject`, required external fonts/images, or reliance on interactive links inside an image. Use basic shapes/text and self-contained permitted assets. Keep clickable navigation as normal Markdown/allowed HTML outside images. Inspect the SVG source and test actual GitHub rendering before calling it verified.
- Keep meaningful text in the README as real text even when the hero includes decorative text. Write useful alt text and a text equivalent for key facts. Check link labels and destinations.
- Preview the actual README at approximately 375px and desktop width. Confirm headings remain legible, images scale without overflow, important face features remain visible, and links are easy to use. Inspect light/dark backgrounds. Record when only a local preview was possible.
- Check all exported image dimensions, byte sizes, GIF duration/frame count and loop seams. Open both animated and static exports. Avoid live statistics that break without secrets, leak tokens in URLs, or misrepresent missing data.
- Resolve relative asset paths from the actual README location and verify external links without logging secrets. Confirm the final file list contains only approved public content and licensed assets.
- Before publication, show exact destination and files with a preview. After authorized publication, reopen the destination and verify README and assets. If credentials, permissions, or networking prevent this, deliver local files and state the remaining action accurately.

Do not use animated SVG features as the only motion deliverable; support varies across GitHub sanitization, proxies, and clients. Provide GIF where appropriate and retain a static fallback. Do not add executable widgets merely to obtain animation.

## Public-file privacy review

Before an upload or commit, inspect the complete public-file inventory and staged diff (or the equivalent exact upload selection). Do not rely only on ignore patterns. Confirm:

- Raw/reference photos and personal source exports are excluded unless their publication was explicitly approved.
- Public raster files have been checked for identifying EXIF/location or other unwanted metadata, and sanitized when needed.
- Editable sources contain no hidden photo layers, private text, embedded exports, or external links that expose private inputs; retain private originals outside public output.
- Private state records, consent evidence, source notes, contact details not approved for publication, temporary previews, credentials, and environment files are absent.
- Every included file is needed, licensed, and covered by the agreed visibility and publication scope; the diff contains no unrelated changes.

Record the reviewed inventory and outcome privately. The package validator checks structural invariants and local paths; it does **not** scan for private data, inspect EXIF, validate licenses, or replace this review.
