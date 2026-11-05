# The Erasure Codex

**A community guide to getting your Discord messages erased under the GDPR and UK GDPR.**

Discord has no button for bulk deleting your message history. If you live in the EU, the EEA or the UK, you have a legal right to ask for it to be erased anyway. This guide explains how that works in practice: what to send, what Discord will reply, how to check what was really deleted, and what to do when the replies stop making sense.

> **Last reviewed: November 2026.** Discord's handling changes, so check the [discussion](https://github.com/victornpb/undiscord/discussions/429) and recent experience reports for anything newer.
>
> **Independent project. Not legal advice.** Discord is a trademark of Discord Inc. This guide isn't affiliated with or endorsed by Discord. This is written by users, from real requests and Discord's real replies. Where the law is uncertain, the guide says so. If your situation is unusual, ask a lawyer or a data protection organisation.

> **Getting help from an AI assistant?** This guide is long, and an AI assistant can take you through just the parts that apply to you. Give it [AI-GUIDE.md](AI-GUIDE.md), or the whole guide in one file: [CODEX-FULL.md](CODEX-FULL.md). Check what it tells you against the pages here, and never give it, or anyone, your Discord password or token.

---

## The short version

1. **Request your data package.** It lists the IDs of the messages you've sent. ([Step 2](docs/02-get-your-data.md))
2. **Turn it into a CSV** of `channel_id,message_id`. A script in this repo does that for you. ([Step 3](docs/03-build-the-csv.md))
3. **Email privacy@discord.com from your account's email address**, citing Article 17, with the CSV attached. ([Step 4](docs/04-send-the-request.md))
4. **Expect a template first.** Discord's first reply usually says bulk deletion isn't offered. It does have a CSV process, so keep going. ([Step 5](docs/05-replies-decoded.md))
5. **Check the result** by comparing an old and a new data package. A confirmation email isn't proof. ([Step 6](docs/06-check-the-result.md))
6. **Write to Discord's Data Protection Officer, then complain to your data protection authority** if Discord refuses without a legal reason or doesn't answer within a month. It's free. ([Step 7](docs/07-deadlines-and-complaints.md), [templates](docs/11-templates.md))

## What to expect

As of 2026, Discord's privacy team will process a CSV of message IDs, but in practice **it only deletes messages in spaces you can no longer access**: servers you've left, group chats you've left, deleted channels. Messages anywhere you can still open, including DMs, are usually left alone, and Discord won't define "access" beyond saying it's "managed dynamically". [Step 1](docs/01-how-it-works.md) explains what that means for you before you start, including what leaving a server or group chat costs you.

Discord's first answer usually says bulk deletion isn't offered. That isn't the whole story, and a template reply isn't a legal refusal. Your rights don't depend on Discord having a feature for them.

If all this seems like a lot of work just to use a legal right, that's worth noticing. Discord is required to *make it easy* to exercise your rights (Article 12(2)). The effort this guide asks of you is itself something you can point out to a regulator ([Templates](docs/11-templates.md#your-effort-is-evidence)).

**What this guide is pushing for** isn't one particular feature. It's for Discord to *effectively facilitate* the erasure of your messages at scale, as the law requires: for example, a way to delete all your messages, or all your messages in a DM, group chat or server. A delete-all button is one way to do that. How Discord does it is up to Discord, as long as it works.

**What this guide is for:** helping you know your options and use your own rights. Make each request about your own data, for your own reasons ([why that matters](docs/08-faq.md)).

**Keep it about Discord, not its staff.** Your request is with Discord as a company, and the people answering tickets don't set its policy. Don't name, harass or publish personal information about individual employees. It hurts real people, it can be unlawful, and it gives Discord and regulators a reason to look away from your complaint. Put your frustration into formal requests and complaints to your data protection authority. That's what gets results.

## Contents

| | Page | What it covers |
|---|---|---|
| 1 | [How it works](docs/01-how-it-works.md) | Your rights, what Discord actually deletes, and decisions to make first |
| 2 | [Get your data package](docs/02-get-your-data.md) | Requesting it, what's inside, keeping it as evidence |
| 3 | [Build the CSV](docs/03-build-the-csv.md) | Using the helper script, or doing it by hand |
| 4 | [Send the request](docs/04-send-the-request.md) | Where to send it, and templates for the EU and the UK |
| 5 | [Discord's replies, decoded](docs/05-replies-decoded.md) | Each template you're likely to get, and how to answer it |
| 6 | [Check the result](docs/06-check-the-result.md) | Comparing packages to see what was really removed |
| 7 | [Deadlines and complaints](docs/07-deadlines-and-complaints.md) | The one-month rule, and complaining to the EU authorities or the ICO |
| 8 | [FAQ](docs/08-faq.md) | Scripts, account deletion, deleted users, servers you own, and more |
| 9 | [Case study](docs/09-case-study.md) | One 2026 request in full: 762,269 messages, what was deleted, and what wasn't |
| 10 | [Legal reference](docs/10-legal-reference.md) | The articles, precedents and guidance this guide relies on |
| 11 | [Templates](docs/11-templates.md) | Writing to Discord's Data Protection Officer, a full access request, and complaining to an authority (EU and UK) |
| 12 | [Deleted or banned accounts](docs/12-banned-accounts.md) | Getting your data and erasing your ordinary messages when your account is deleted or banned |

The helper script is in [`scripts/`](scripts/). It uses plain Python, reads your package without changing it, and doesn't connect to anything.

## Help keep this accurate

Discord's handling changes, sometimes month to month. If you've made a request, your experience helps others: open an issue using the **Experience report** template, or read [CONTRIBUTING.md](CONTRIBUTING.md). Corrections are just as welcome, especially from people who know the law better than we do.

## Background and credits

This guide builds on work by others. Thank you to:

- **No Text To Speech**, whose video [Fixing Discord's Biggest Privacy Flaw with a Loophole](https://www.youtube.com/watch?v=g5FbRfwMEuo) (September 2024) explained the GDPR route clearly enough for many people, including this guide's author, to try it.
- **[Undiscord discussion #429](https://github.com/victornpb/undiscord/discussions/429)**, "Bulk Deleting Discord Messages and GDPR Compliance", started by abigailwillow in 2022. The video links to it, and hundreds of users have compared requests, replies and results there since. Much of what this guide says about Discord's handling comes from their reports.
- **ishnz**, whose [bulk_deletion_helper](https://github.com/ishnz/bulk_deletion_helper) made the requests behind this guide possible ([Build the CSV](docs/03-build-the-csv.md), Option B).
- The community **[Discordomicon](https://web.archive.org/web/20260708064954/https://discordomicon.github.io/removal/overview/)** guide, which went offline in 2026 (Wayback Machine copies exist from January 2025 to July 2026). None of its text is reused here.

## How this guide was made

This guide comes from my own erasure requests to Discord between February and November 2026: the emails, Discord's replies, and the data packages I compared before and after. I wrote it with help from Claude (Anthropic's AI assistant) for legal research, structure, drafting and checking claims against sources. I also used ChatGPT for a second opinion on the legal content and to audit the helper script. Every legal point links to the law or to Discord's own published pages, and the helper script was tested against real data packages. I maintain this guide and I'm responsible for what's in it. If you find something wrong, please [open an issue](https://github.com/Technae/The-Erasure-Codex/issues) so I can fix it.

## Licence

Guide text: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). You can copy, translate and adapt it if you credit this project and share alike. Scripts: MIT (see [`scripts/LICENSE`](scripts/LICENSE)). Details in [LICENSE.md](LICENSE.md).
