# The Erasure Codex

**A community guide to getting your Discord messages erased under the GDPR and UK GDPR.**

Discord has no button for bulk deleting your message history. If you live in the EU, the EEA or the UK, you have a legal right to ask for it to be erased anyway. This guide explains how that works in practice: what to send, what Discord will reply, how to check what was really deleted, and what to do when the replies stop making sense.

> **Last reviewed: November 2026.** Discord's handling changes, so check the [discussion](https://github.com/victornpb/undiscord/discussions/429) and recent experience reports for anything newer.
>
> **Independent project. Not legal advice.** Discord is a trademark of Discord Inc. This guide isn't affiliated with or endorsed by Discord. This is written by users, from real requests and Discord's real replies. Where the law is uncertain, the guide says so. If your situation is unusual, ask a lawyer or a data protection organisation.

---

## The short version

1. **Request your data package.** It lists the ID of every message you've sent. ([Step 2](docs/02-get-your-data.md))
2. **Turn it into a CSV** of `channel_id,message_id`. A script in this repo does that for you. ([Step 3](docs/03-build-the-csv.md))
3. **Email privacy@discord.com from your account's email address**, citing Article 17, with the CSV attached. ([Step 4](docs/04-send-the-request.md))
4. **Expect a template first.** Discord's first reply usually says bulk deletion isn't offered. It does have a CSV process, so keep going. ([Step 5](docs/05-replies-decoded.md))
5. **Check the result** by comparing an old and a new data package. A confirmation email isn't proof. ([Step 6](docs/06-check-the-result.md))
6. **Complain to your data protection authority** if Discord refuses without a legal reason or doesn't answer within a month. It's free. ([Step 7](docs/07-deadlines-and-complaints.md))

## What to expect

As of 2026, Discord's privacy team will process a CSV of message IDs, but in practice **it only deletes messages in spaces you can no longer access**: servers you've left, group chats you've left, deleted channels. Messages anywhere you can still open, including DMs, are usually left alone, and Discord won't define "access" beyond saying it's "managed dynamically". [Step 1](docs/01-how-it-works.md) explains what that means for you before you start, including what leaving a server or group chat costs you.

Discord's first answer usually says bulk deletion isn't offered. That isn't the whole story, and a template reply isn't a legal refusal. Your rights don't depend on Discord having a feature for them.

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

The helper script is in [`scripts/`](scripts/). It uses plain Python, reads your package without changing it, and doesn't connect to anything.

## Help keep this accurate

Discord's handling changes, sometimes month to month. If you've made a request, your experience helps others: open an issue using the **Experience report** template, or read [CONTRIBUTING.md](CONTRIBUTING.md). Corrections are just as welcome, especially from people who know the law better than we do.

## Background

This guide continues the work of the community [Discordomicon](https://web.archive.org/web/20260708064954/https://discordomicon.github.io/removal/overview/) guide, which went offline in 2026 (Wayback Machine copies exist from January 2025 to July 2026), and of the long-running [Undiscord discussion #429](https://github.com/victornpb/undiscord/discussions/429), where hundreds of users have compared notes since 2022. None of the Discordomicon's text is reused here.

## Licence

Guide text: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). You can copy, translate and adapt it if you credit this project and share alike. Scripts: MIT (see [`scripts/LICENSE`](scripts/LICENSE)). Details in [LICENSE.md](LICENSE.md).
