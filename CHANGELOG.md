# Changelog

Notable changes to The Erasure Codex, newest first, with the reason for each. Small wording fixes and typos aren't listed. The full history is in the repository's commits.

Entries before 5 November 2026 were written up afterwards from the working notes, so they're grouped by day rather than by commit.

**If you used an older version:** check the entries after the date you sent your request. The most important one for anyone with a request still open is on 4 November: the request templates now say you want to keep your account.

---

## 5 November 2026

### Added
- **[AI-GUIDE.md](AI-GUIDE.md)**, a page for AI assistants helping someone use the guide: which questions to ask first, which pages fit each situation, and rules to follow. *Why:* the guide is long, and many people will use it with an AI assistant. Without instructions, assistants tend to summarise from memory or overwhelm people with the whole process.
  - Includes rules on protecting the person's data (no uploading the full data package or private conversations), keeping evidence and legal arguments apart, and not claiming to have checked sources they didn't open. *Why:* suggested by an independent review; helping someone shouldn't mean disclosing their conversations again.
- **[CODEX-FULL.md](CODEX-FULL.md)**, the whole guide in one file, and `scripts/build_full.py` to rebuild it. *Why:* AI tools often read only the first page of a link, and one file is easier to upload.
- **"How this guide was made"** section in the README. *Why:* the guide was written with help from AI tools (Claude for research, structure and drafting; ChatGPT for a second legal review and a script audit), and readers should know that, along with how claims were checked and who is responsible for them.
- **This changelog.** *Why:* to keep a record of what changed and why, and so people who followed an older version can see what's different.

### Changed: legal accuracy
- **UK Article 12A** is now described correctly: the month starts from the latest of receiving the request, receiving requested ID information, or a fee being paid, and the clock can pause for clarification only for access requests. *Why:* the earlier wording made it sound like a general pause for any question.
- **UK complaints:** the ICO says you can complain to it at any time, but recommends complaining to the company first, and in most cases will ask you to. Added its three-month window after your last contact with the company. *Why:* the earlier wording said you "need" to complain to the company first, which overstated it.
- **UK section 166** added as the route if the ICO doesn't progress your complaint; Article 78(2) is now marked EU/EEA only. *Why:* 78(2) isn't the UK route.
- **Writing to the DPO** is now described as optional, and the guide says it doesn't restart the deadline on your original request. *Why:* "give it the full month" could be read as having to wait another month.
- **Legal reference introduction** no longer says the article numbers are identical in the GDPR and UK GDPR. *Why:* the UK has since added Article 12A and removed Article 77.
- **Brillen Rottler (C-526/24)** is now noted as an access-request case. *Why:* so it isn't read as a ruling about erasure requests.
- **Legal basis (page 1):** other users' interests now "point to" legitimate interests rather than proving Discord relies on them. *Why:* a fair inference, not a certainty.
- **Compare example (page 6)** now says which packages its figures come from. *Why:* it looked inconsistent with the case study's later figure.

### Changed: helper script
- **Output is written to a temporary file first** and only put in place once the whole run succeeds. *Why:* a run that failed halfway could leave a partial CSV that looked complete, or replace an earlier file with an incomplete one.
- **Unreadable message records now stop the run** instead of being skipped with a warning; `--allow-incomplete` continues knowingly and says so. *Why:* an erasure request or comparison built from an incomplete export shouldn't look finished.
- **Other fixes:** CSV headers with spaces are read correctly; the `--only`/`--exclude` lists can't be overwritten; unrecognised message files and folders with messages but no channel ID are errors; other unrecognised folders get a warning; unreadable folders and corrupt ZIPs give a clean error. *Why:* all found in an independent code review.
- `--split` is now described as messages per file, plus the header. Tests increased from 21 to 30.

---

## 4 November 2026

### Added
- **"Keep my account" wording** in every message-erasure request template, a checklist item, a tip against "delete all my personal data" wording, and an FAQ entry ("Will an erasure request delete my account?"). *Why:* a user reported a support agent deleting their whole account partway through a message request, without being asked.
- **"Keep it about Discord, not its staff"** note in the README and the complaints page. *Why:* some people in community threads have targeted individual employees. That hurts real people, can be unlawful, and distracts from complaints that work.
- **ishnz's bulk_deletion_helper** as Option B on the Build the CSV page. *Why:* it's the tool linked in the No Text To Speech video and the one used for the requests behind this guide.
- **Credits** for No Text To Speech's video, the Undiscord discussion #429, ishnz and the Discordomicon. *Why:* the guide builds on their work.

---

## 3 November 2026

### Added
- **"Which erasure ground applies?"** on page 1: how the ground for erasure depends on the legal basis Discord relies on (contract or legitimate interests). Templates now ask Discord to state its legal basis for anything it keeps. *Why:* Discord's documents point both ways, and "I wrote it" isn't a ground in itself.
- **Make each request about your own data, for your own reasons** (FAQ, README, legal reference). *Why:* the CJEU's Brillen Rottler judgment held that a request made with abusive intent can be refused.
- **Proving it's your account** (page 12): no ID by default, and better ways to show ownership. *Why:* sending ID documents by default isn't required and adds risk.
- **Deleted messages and the data package:** a message you delete yourself isn't in the package, even though Discord's retention page says some public posts are kept for a period. *Why:* people assumed the package shows everything Discord holds.
- **Account status** field in the experience report template. *Why:* results differ for active, banned and deleted accounts.

### Changed
- **Page 12 renamed and rewritten as "Deleted or banned accounts"**, with access and erasure templates for both. *Why:* people with deleted accounts had no clear route.
- **UK law updates:** the June 2026 changes (section 164A complaints to the company, section 165 complaints to the ICO, Article 77 removed), Discord Inc. as the UK controller, and Article 12A. *Why:* UK law changed after the guide was first drafted.
- **Legal wording softened or corrected** after an independent review, including: Article 12(4) requires reasons and a complaint notice, not article numbers; Article 15 doesn't itself cover the legal basis (that's Articles 13 and 14); the EDPB-commissioned case digest isn't an official EDPB position. *Why:* to avoid overstating the law.
- **Helper script rewritten:** compares channel-and-message pairs, stops with an error on files it can't read, won't overwrite the package or existing files without `--force`, and has tests. Checked against real data packages. *Why:* an independent audit found it could miscount or overwrite files.
- **Case study heading** changed from "The test that shows the rule" to "The case that shows the rule". *Why:* requests are made for their own purpose, not as tests.

---

## 2 November 2026

- **First published.**
