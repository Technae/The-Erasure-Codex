# The Erasure Codex: the whole guide in one file

This file joins every page of the guide so it can be read, or given to an AI assistant, in one go. It is generated from the individual pages by `scripts/build_full.py`; edit those pages, not this file. Each page starts with a `<!-- file: ... -->` marker.

Source: https://github.com/Technae/The-Erasure-Codex

---

<!-- file: AI-GUIDE.md -->

# For AI assistants

This page is for AI assistants helping someone use The Erasure Codex. If you're a person, you don't need it: start with the [README](https://github.com/Technae/The-Erasure-Codex/blob/main/README.md).

The Codex is long because the process is. Your job is to turn it into a conversation: find out the person's situation, take them through only the steps that apply, and fill in the templates with them. Ground what you say in the guide's pages and the law they cite, not in general memory of the GDPR.

**The whole guide in one file:** [CODEX-FULL.md](https://github.com/Technae/The-Erasure-Codex/blob/main/CODEX-FULL.md) (raw: `https://raw.githubusercontent.com/Technae/The-Erasure-Codex/main/CODEX-FULL.md`). Read that if you can only fetch one page. Individual pages are in [`docs/`](https://github.com/Technae/The-Erasure-Codex/blob/main/docs).

## Before you start

- **This isn't legal advice, and you're not a lawyer.** Say so once, plainly. Suggest a data protection organisation or lawyer if the situation is unusual or high-stakes.
- **Check how current it is.** The README has a "Last reviewed" date. Discord's handling changes, so if it's more than a few months old, check the [Undiscord discussion #429](https://github.com/victornpb/undiscord/discussions/429) and recent experience reports in this repo's issues.
- **The person stays in charge.** You can draft and explain, but they decide, and they send the emails from their own account's email address.
- **Protect their data.** Don't ask them to upload their full Discord data package or paste private conversations: it contains personal data about them and about other people. The script's `summary` output and short, redacted excerpts are usually enough. Before they share screenshots, emails or script output, suggest removing email addresses, account and channel IDs, ticket numbers, message contents and anything else you don't need. Never ask for passwords, tokens or authentication codes. Nothing in this process needs them.
- **Keep evidence and conclusions apart.** Make clear what comes from the person's own correspondence, what Discord publicly documents, what other users have reported (the case study and discussion threads contain user reports, not independently verified findings), and what is a legal argument rather than an established ruling.

## Ask these first

Ask a few at a time, in plain language, not all at once.

1. **Where do you live?** EU/EEA → GDPR. UK → UK GDPR (the UK route differs at the complaint stage). Anywhere else → the guide doesn't cover it ([FAQ](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/08-faq.md)). The country also decides which authority they complain to and whether any national rules apply. Where someone lives isn't the whole legal test for whether the GDPR applies, but it's the right practical starting point here.
2. **Is your Discord account active, banned (disabled), or deleted?** Banned or deleted → [page 12](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/12-banned-accounts.md) is their main route.
3. **What do you want erased?** Everything, particular DMs or servers, or also analytics/activity data?
4. **Do you have your data package yet?** If their account is active and they haven't requested it, that's the first step, and it can take up to 30 days. If they're banned or their account is deleted, go to [page 12](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/12-banned-accounts.md) instead: they may need to make a formal access request by email.
5. **Have you already contacted Discord about this?** If yes: when, and what did Discord reply? Ask them to paste the reply.
6. **Are you comfortable running a small script on your computer?** This decides how you help them build the CSV.

## Where to go next

| Their situation | Pages |
|---|---|
| Starting from scratch | [1. How it works](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/01-how-it-works.md) (especially "Decide these before you start"), then 2 → 3 → 4 |
| No data package yet | [2. Get your data package](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/02-get-your-data.md) |
| Has the package, needs the CSV | [3. Build the CSV](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md) |
| Ready to send | [4. Send the request](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/04-send-the-request.md) |
| Got a reply from Discord | [5. Discord's replies, decoded](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/05-replies-decoded.md): match the reply to a section and use its follow-up |
| Discord says it's done; wants to check | [6. Check the result](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md) |
| A month has passed, or the reply refused without reasons | [7. Deadlines and complaints](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/07-deadlines-and-complaints.md), then [11. Templates](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md) |
| Account banned or deleted | [12. Deleted or banned accounts](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/12-banned-accounts.md) |
| Wants to know what Discord holds, not erase yet | [11. Templates](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#access-request-everything-discord-holds-about-you-general-dsar) (general access request) |
| Asks "why" or wants the legal basis | [10. Legal reference](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/10-legal-reference.md) and [1. How it works](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/01-how-it-works.md#which-erasure-ground-applies) |

## Rules to follow

- **Keep the account where the request is about messages.** Keep the "I want to keep my account" line in message-erasure requests, unless the person explicitly wants their account deleted. Don't reword requests into "delete all my personal data", which can be read as an account deletion request. You don't need to add the line to unrelated access requests or complaints.
- **Warn before account deletion.** Deleting an account doesn't erase its messages, cancels a pending data package request, and makes checking the result and following up harder. Recommend keeping the account until they've got their package and checked the result, but explain the consequences and let them decide.
- **Don't suggest sending ID** by default. Sending from the account's registered email is normally enough ([page 12, "Proving it's your account"](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/12-banned-accounts.md#proving-its-your-account)).
- **Count deadlines by calendar month,** from the day Discord received the request to the same date the next month, moved to the next working day if that's a weekend or public holiday ([page 7](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/07-deadlines-and-complaints.md#the-deadline)). Discord can extend by up to two months only if it says so, with reasons, within the first month. Writing to the DPO or sending a reminder doesn't restart the deadline. UK only: if Discord reasonably asks for identity information, the month starts when it gets it, and for access requests the clock can pause for genuine clarification (Article 12A, [legal reference](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/10-legal-reference.md)).
- **Each request is about the person's own data, for their own reasons.** Don't frame requests as tests, experiments or campaign tactics ([why](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/08-faq.md)).
- **Keep it aimed at Discord, not its staff.** Never help name, target or publish anything about individual employees.
- **Quote Discord exactly.** "Submitted for deletion" isn't proof of deletion. Comparing data packages shows what's no longer in the newer export, and spot-checking in the app shows what's no longer visible. Neither proves that every copy, including backups, has been erased ([page 6](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md)).
- **Don't overstate.** Where the guide says the law is uncertain, say it's uncertain. Don't promise outcomes, fines, or that a regulator will act quickly.
- **Use calm, plain language** in anything the person sends. Threats and legal jargon beyond the article numbers don't help.

## Helping with the script

Guide them to run the script on their own computer. Don't ask them to upload their data package to you, even if your environment could run code on it. Take it slowly:

1. Check whether they have Python 3, and help them install it if not ([python.org](https://www.python.org/downloads/)).
2. Have them put the script and their package ZIP in the same folder, and open a terminal there.
3. Give them one command at a time from [page 3](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md), starting with `summary`, and ask them to paste the output back.
4. Explain what each output means before the next step.

If the script stops with an error, ask for the exact message rather than guessing. If it stops because some message records can't be read, `--allow-incomplete` lets it continue, but explain first that those messages will be left out of the CSV, and suggest reporting the error as an issue. If the terminal is too much for them, [Option B](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md#option-b-ishnzs-bulk_deletion_helper) is an alternative. Never suggest tools that ask for their Discord token or password.

## Filling in templates

Fill in the placeholders with the person's own details (username, user ID, email, country, numbers from the `summary` output, dates). The objection paragraph needs the person's own reasons for objecting (Article 21 requires grounds relating to their particular situation): ask them, and help them put it in a sentence or two, but don't invent reasons or reuse a stock paragraph. If they don't want to object, remove that paragraph. Show them the finished email and ask them to check every detail before sending. Remind them to save a copy and note the date they sent it.

## If something in the guide looks wrong

Check the current legislation, relevant court judgments and official supervisory-authority guidance before correcting a legal point. If they conflict with the guide, explain the difference rather than quietly replacing the guide's position. Never claim to have checked a page, file or source you didn't actually open.

Then tell the person, and suggest they report it by opening an issue on this repository, so it can be fixed for everyone. Remind them not to post their personal correspondence, data package contents or account details in a public issue: the problem can be described without them.

---

<!-- file: README.md -->

# The Erasure Codex

**A community guide to getting your Discord messages erased under the GDPR and UK GDPR.**

Discord has no button for bulk deleting your message history. If you live in the EU, the EEA or the UK, you have a legal right to ask for it to be erased anyway. This guide explains how that works in practice: what to send, what Discord will reply, how to check what was really deleted, and what to do when the replies stop making sense.

> **Last reviewed: November 2026.** Discord's handling changes, so check the [discussion](https://github.com/victornpb/undiscord/discussions/429) and recent experience reports for anything newer.
>
> **Independent project. Not legal advice.** Discord is a trademark of Discord Inc. This guide isn't affiliated with or endorsed by Discord. This is written by users, from real requests and Discord's real replies. Where the law is uncertain, the guide says so. If your situation is unusual, ask a lawyer or a data protection organisation.

> **Getting help from an AI assistant?** This guide is long, and an AI assistant can take you through just the parts that apply to you. Give it [AI-GUIDE.md](https://github.com/Technae/The-Erasure-Codex/blob/main/AI-GUIDE.md), or the whole guide in one file: [CODEX-FULL.md](https://github.com/Technae/The-Erasure-Codex/blob/main/CODEX-FULL.md). Check what it tells you against the pages here. Don't upload your whole data package or private conversations to it, and never give it, or anyone, your Discord password or token.

---

## The short version

1. **Request your data package.** It lists the IDs of the messages you've sent. ([Step 2](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/02-get-your-data.md))
2. **Turn it into a CSV** of `channel_id,message_id`. A script in this repo does that for you. ([Step 3](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md))
3. **Email privacy@discord.com from your account's email address**, citing Article 17, with the CSV attached. ([Step 4](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/04-send-the-request.md))
4. **Expect a template first.** Discord's first reply usually says bulk deletion isn't offered. It does have a CSV process, so keep going. ([Step 5](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/05-replies-decoded.md))
5. **Check the result** by comparing an old and a new data package. A confirmation email isn't proof. ([Step 6](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md))
6. **Optionally escalate to Discord's Data Protection Officer, then complain to your data protection authority** if Discord refuses without adequate reasons or doesn't answer within the deadline. It's free. ([Step 7](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/07-deadlines-and-complaints.md), [templates](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md))

## What to expect

As of 2026, Discord's privacy team will process a CSV of message IDs, but in practice **it only deletes messages in spaces you can no longer access**: servers you've left, group chats you've left, deleted channels. Messages anywhere you can still open, including DMs, are usually left alone, and Discord won't define "access" beyond saying it's "managed dynamically". [Step 1](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/01-how-it-works.md) explains what that means for you before you start, including what leaving a server or group chat costs you.

Discord's first answer usually says bulk deletion isn't offered. That isn't the whole story. A template reply isn't necessarily a complete or properly reasoned answer, even when it amounts to a refusal. Your rights don't depend on Discord having a feature for them.

If all this seems like a lot of work just to use a legal right, that's worth noticing. Discord is required to *make it easy* to exercise your rights (Article 12(2)). The effort this guide asks of you is itself something you can point out to a regulator ([Templates](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#your-effort-is-evidence)).

**What this guide is pushing for** isn't one particular feature. It's for Discord to *effectively facilitate* the erasure of your messages at scale, as the law requires: for example, a way to delete all your messages, or all your messages in a DM, group chat or server. A delete-all button is one way to do that. How Discord does it is up to Discord, as long as it works.

**What this guide is for:** helping you know your options and use your own rights. Make each request about your own data, for your own reasons ([why that matters](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/08-faq.md)).

**Keep it about Discord, not its staff.** Your request is with Discord as a company, and the people answering tickets don't set its policy. Don't name, harass or publish personal information about individual employees. It hurts real people, it can be unlawful, and it gives Discord and regulators a reason to look away from your complaint. Put your frustration into formal requests and complaints to your data protection authority. That's what gets results.

## Contents

| | Page | What it covers |
|---|---|---|
| 1 | [How it works](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/01-how-it-works.md) | Your rights, what Discord actually deletes, and decisions to make first |
| 2 | [Get your data package](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/02-get-your-data.md) | Requesting it, what's inside, keeping it as evidence |
| 3 | [Build the CSV](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md) | Using the helper script, or doing it by hand |
| 4 | [Send the request](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/04-send-the-request.md) | Where to send it, and templates for the EU and the UK |
| 5 | [Discord's replies, decoded](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/05-replies-decoded.md) | Each template you're likely to get, and how to answer it |
| 6 | [Check the result](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md) | Comparing packages to see what was really removed |
| 7 | [Deadlines and complaints](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/07-deadlines-and-complaints.md) | The one-month rule, and complaining to the EU authorities or the ICO |
| 8 | [FAQ](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/08-faq.md) | Scripts, account deletion, deleted users, servers you own, and more |
| 9 | [Case study](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/09-case-study.md) | One 2026 request in full: 762,269 messages, what was deleted, and what wasn't |
| 10 | [Legal reference](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/10-legal-reference.md) | The articles, precedents and guidance this guide relies on |
| 11 | [Templates](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md) | Writing to Discord's Data Protection Officer, a full access request, and complaining to an authority (EU and UK) |
| 12 | [Deleted or banned accounts](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/12-banned-accounts.md) | Getting your data and erasing your ordinary messages when your account is deleted or banned |

The helper script is in [`scripts/`](https://github.com/Technae/The-Erasure-Codex/blob/main/scripts). It uses plain Python, reads your package without changing it, and doesn't connect to anything.

## Help keep this accurate

Discord's handling changes, sometimes month to month. If you've made a request, your experience helps others: open an issue using the **Experience report** template, or read [CONTRIBUTING.md](https://github.com/Technae/The-Erasure-Codex/blob/main/CONTRIBUTING.md). Corrections are just as welcome, especially from people who know the law better than we do. What has changed, and why, is recorded in the [changelog](https://github.com/Technae/The-Erasure-Codex/blob/main/CHANGELOG.md).

## Background and credits

This guide builds on work by others. Thank you to:

- **No Text To Speech**, whose video [Fixing Discord's Biggest Privacy Flaw with a Loophole](https://www.youtube.com/watch?v=g5FbRfwMEuo) (September 2024) explained the GDPR route clearly enough for many people, including this guide's author, to try it.
- **[Undiscord discussion #429](https://github.com/victornpb/undiscord/discussions/429)**, "Bulk Deleting Discord Messages and GDPR Compliance", started by abigailwillow in 2022. The video links to it, and hundreds of users have compared requests, replies and results there since. Much of what this guide says about Discord's handling comes from their reports.
- **ishnz**, whose [bulk_deletion_helper](https://github.com/ishnz/bulk_deletion_helper) made the requests behind this guide possible ([Build the CSV](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md), Option B).
- The community **[Discordomicon](https://web.archive.org/web/20260708064954/https://discordomicon.github.io/removal/overview/)** guide, which went offline in 2026 (Wayback Machine copies exist from January 2025 to July 2026). None of its text is reused here.

## How this guide was made

This guide comes from my own erasure requests to Discord between February and November 2026: the emails, Discord's replies, and the data packages I compared before and after. I wrote it with help from Claude (Anthropic's AI assistant) for legal research, structure, drafting and checking claims against sources. I also used ChatGPT for a second opinion on the legal content and to audit the helper script. Every legal point links to the law or to Discord's own published pages, and the helper script was tested against real data packages. I maintain this guide and I'm responsible for what's in it. If you find something wrong, please [open an issue](https://github.com/Technae/The-Erasure-Codex/issues) so I can fix it.

## Licence

Guide text: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). You can copy, translate and adapt it if you credit this project and share alike. Scripts: MIT (see [`scripts/LICENSE`](https://github.com/Technae/The-Erasure-Codex/blob/main/scripts/LICENSE)). Details in [LICENSE.md](https://github.com/Technae/The-Erasure-Codex/blob/main/LICENSE.md).

---

<!-- file: docs/01-how-it-works.md -->

# 1. How it works


## Your rights

If you're in the **EU or EEA**, the GDPR applies. If you're in the **UK**, the UK GDPR applies, and it's nearly identical for this purpose. Both give you:

- **The right to erasure (Article 17).** You can ask for your personal data to be erased. The usual grounds are that Discord no longer needs it for the purpose it was collected for (17(1)(a)), or that you object to its processing and Discord has no overriding grounds to continue (17(1)(c), together with Article 21).
- **The right to object (Article 21).** Where a company relies on "legitimate interests", you can object, on grounds relating to your particular situation (say briefly why, in your own words). Discord's replies refer to other users' legitimate interests when it keeps your messages, though it hasn't clearly said which legal basis it relies on. It must then stop unless it can show *compelling* legitimate grounds that override your interests, rights and freedoms, or that the processing is needed to establish, exercise or defend legal claims.
- **The right to a proper answer (Article 12).** Discord must reply within one month. If it doesn't do what you asked, it must tell you why and that you can complain to a data protection authority or a court. Requests are free.

Article 17(3) lists specific exceptions to the right to erasure: freedom of expression and information, a legal obligation, public health, archiving or research, and legal claims. A company can also argue that none of the Article 17(1) grounds applies in the first place, and a few other rules can limit requests (for example, where a request is manifestly excessive). But an unpublished "accessible space" rule isn't a statutory exception. "Other users would like to keep reading your messages" isn't on that list as such. Discord might try to argue that it falls under freedom of expression and information, or that it's a compelling ground under Article 21, but the replies quoted in this guide's [case study](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/09-case-study.md) don't cite any of these, or any article at all.

### Which erasure ground applies?

Article 17(1) lists several grounds for erasure. Which one fits depends on the **legal basis** Discord uses to keep your messages, and Discord hasn't said clearly which that is. Different purposes can have different bases, and its own documents point two ways:

| If Discord keeps your messages on the basis of… | What points to this | Your ground for erasure | To refuse, Discord must show… |
|---|---|---|---|
| **Legitimate interests** (Article 6(1)(f)) | Template replies say other users "have a legitimate interest in having access to content sent to them". That suggests legitimate interests are part of Discord's justification, though it hasn't formally said so | Object under Article 21(1), giving your own reasons. Erasure then follows under **17(1)(c)** | Compelling legitimate grounds that override your interests, rights and freedoms, or that keeping them is needed for legal claims, or an Article 17(3) exception |
| **Contract** (Article 6(1)(b)) | The privacy policy lists storing and displaying your messages "as you direct" under fulfilling its contract with you | **17(1)(a):** the messages are no longer necessary for that purpose. Your erasure request is strong evidence of what you now direct, but it doesn't settle the question by itself: the test is whether keeping them is still necessary for the purpose Discord relies on | Why keeping them is still necessary for its contract *with you*, or an Article 17(3) exception |

Three points follow from this:
- **Contract only covers the contract with you.** Article 6(1)(b) applies to a contract "to which the data subject is party", meaning you. Other users wanting to keep reading your messages isn't part of your contract. If that's Discord's reason, it points to legitimate interests rather than contract, and you can object. Either way, the safest request is to ask Discord to state the purpose and legal basis for keeping each set of messages, and why keeping them is still necessary.
- **If Discord has no valid basis at all** for keeping a message, **17(1)(d)** applies (unlawful processing). That's a fallback, not something to lead with.
- **The Article 17(3) exceptions apply whichever basis it is.** If Discord relies on one, its reasons for refusing should say so.

That's why the templates cite both 17(1)(a) and 17(1)(c): you don't know which basis Discord will rely on, and citing both covers each case. They also ask Discord to state the legal basis and purpose for anything it keeps, so it has to commit to one. (Strictly, Article 12(4) requires *reasons* and a notice of your right to complain, not an article number. But asking for the basis and the exception makes vague reasons easy to spot.)

What's still uncertain is how authorities will treat conversations other people can still read. Discord could argue freedom of expression and information (17(3)(a)) for those. The clearest cases are ones where nobody else is left to read the messages, such as DMs with users who have deleted their accounts.

**The delete-button argument.** Discord's stated reason for keeping your messages is that other users rely on them, and that removing them would leave conversations "missing important context". But Discord already lets you delete any of those same messages yourself, one at a time, and that disrupts the conversation in exactly the same way. Discord's own CSV process also removes messages in bulk from servers you've left, where other members can still read the conversation. So conversation context can't explain why Discord refuses to process the messages you can still open. This doesn't prove Discord must build a bulk-delete tool. It does show that its justification is inconsistent, and that a refusal needs a better legal explanation than the one it gives.

**National rules.** The GDPR applies across the EU and EEA, but countries can add limited restrictions, for example to protect freedom of expression (Articles 23 and 85). This guide doesn't cover them country by country. If one might apply to you, your data protection authority can tell you.

**Are your messages personal data?** Generally yes, when they're linked to your account. Discord itself says so: its data package gives you your messages as part of your data, and one of its own template replies calls them "part of the sender's personal data". Some messages contain more about you than others, and that can matter if Discord argues about a specific message, but it isn't the test Discord applies in practice (see below).

## What Discord actually does (as of 2026)

| What you ask for | What usually happens |
|---|---|
| "Please delete all my messages" with no CSV | A template: "We don't offer the ability to delete your messages in bulk right now", the Shift-click tip, and a suggestion to delete your account |
| A CSV of `channel_id,message_id` | Processed, with a template confirmation that the IDs were "submitted for deletion" |
| Messages in **servers or group chats you've left**, or deleted channels | Usually deleted |
| Messages **anywhere you can still open** (current servers, DMs, group chats you're still in) | Usually **not** deleted. The confirmation says spaces you can access are excluded |
| A definition of "access" | "Access permissions are managed dynamically", and nothing more |
| The legal basis for keeping the rest | Usually no answer |

This "accessible space" rule is the core problem. It isn't in the GDPR, Discord doesn't publish it, and it's applied mechanically. In the [case study](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/09-case-study.md), it kept a DM between two accounts belonging to the same person, after **both** accounts asked for it to be erased. It also kept DMs with users who had already deleted their accounts, where nobody else is left to "keep access".

## Decide these before you start

**1. Do you want to leave servers and group chats first?**
Under Discord's current practice, leaving is what makes messages deletable. Leaving costs you:
- **Servers:** you can rejoin a public server, but not an invite-only one without a new invite.
- **Group chats:** once you leave, you can't get back in unless someone adds you. You lose the history.
- **DMs:** you can't really leave a DM. Closing it only hides it, and you can still open it. In practice, DMs stay "accessible".

Leaving isn't required to make a request, and you shouldn't have to do it. If you stay, you're asking Discord to apply the law rather than its rule, so expect a longer fight (Steps 5 and 7). Many people do both: leave what they don't need, and ask for everything.

**2. Do you want to delete your account?**
Deleting your account does **not** delete your messages. Discord says it anonymises them: your name is replaced with "Deleted User", and your email and IP addresses are removed. The messages stay visible. Once your account is gone, or "pending deletion", you can't make requests through it. **Make your erasure request first, and keep your account until you've checked the result.**

**3. Do you own any servers?**
As owner you can delete channels, or the whole server, and that removes your messages in them. It also removes everyone else's. Think about the other members, and give them a chance to save anything they need, before you do that.

**4. What else do you want erased?**
Your data package also contains analytics and other "activity" data, sometimes going back many years. You can object to and ask for erasure of that too (see [Step 4](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/04-send-the-request.md)). You can also limit future collection in **User Settings → Data & Privacy**.

## What you'll need

- Access to the **email address registered to your account**. Requests from other addresses get bounced or ignored.
- About an hour, spread over a few weeks, to request your data package, wait for it, build the CSV and send the request.
- Patience. Expect templates, and expect to reply more than once.

---

<!-- file: docs/02-get-your-data.md -->

# 2. Get your data package


Your data package is a ZIP file from Discord with a copy of your data. You need it for two reasons:

1. **It lists the IDs of the messages you've sent**, which Discord asks for in the CSV. (Some users report packages missing messages; see below.)
2. **It's your "before" picture.** Comparing it with a later package shows which messages are no longer in the export, and spot-checks in the app show whether they're still visible. Neither proves every copy is gone ([Step 6](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md)).

## How to request it

**Desktop or browser:** User Settings (the cog, bottom left) → **Data & Privacy** → **Request your data** → **Request Data**. Choose what to include, then **Request My Data**.

**Mobile:** your avatar → the cog → **Data & Privacy** → **Request all of my data**.

Tick **Messages** (and everything else, if you want the full picture). Discord says the package arrives within 30 days. It's often much sooner. The download link is sent to your account's email and stays valid for 30 days.

Things to know:
- **You can only have one request running at a time,** and users report waiting about a month before you can request another. Plan around that: you'll want a second package later to check the result.
- **Deleting or disabling your account before the link arrives cancels the request.**
- **Messages in servers you've left are still included.** The "Servers" folder only lists servers you're in now, but the "Messages" folder covers everything you've sent. Some users have reported packages that seem to be missing messages, so treat it as very good rather than perfect.
- **If you can't get into your account**, Discord's help page says to contact privacy@discord.com.
- **The package isn't everything Discord holds.** Discord's [data package article](https://support.discord.com/hc/en-us/articles/360004957991) says it leaves out support and Trust & Safety correspondence, and that a message you delete "is no longer stored in Discord", so it won't be in the package. But Discord's [retention article](https://support.discord.com/hc/en-us/articles/5431812448791) says public posts may be kept for 180 days to two years after deletion, for example to train safety models. If you want everything, use the [general access request](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#access-request-everything-discord-holds-about-you-general-dsar).

## What's inside

| Folder | What it holds |
|---|---|
| `Account/` | Your account details, settings, connections, sessions |
| `Activity/` | Analytics and other event data (subfolders such as reporting, analytics, modeling, tns). Discord says the tns (Trust & Safety) data "is retained for up to 2 years" |
| `Messages/` | One subfolder per channel or DM you've written in, plus an index of channel names |
| `Servers/` | Servers you're currently in |

Inside `Messages/`, each channel has its own folder (named like `c123456789012345678`) containing:
- `channel.json`: the channel ID and type (DM, group DM or server channel), and for server channels, the server
- `messages.json` (or `messages.csv` in older packages): your messages, each with an **ID**, a timestamp, the contents and any attachment links

Folder names and formats have changed over the years. The helper script handles both the JSON and the older CSV layout.

## Keep it as evidence

Treat the ZIP as evidence from day one:

1. **Don't edit it, and don't open the files in a text editor that might save changes.** If you want to look inside, use a viewer, the helper script, or the terminal (`less`, `jq`).
2. **Record its fingerprint.** A SHA-256 hash proves later that the file hasn't changed:
   - Linux: `sha256sum package.zip`
   - macOS: `shasum -a 256 package.zip`
   - Windows (PowerShell): `Get-FileHash package.zip`

   Save the result in a text file with the date, for example `hashes.txt`.
3. **Keep a copy somewhere safe**, and rename it with the date you received it, such as `package-2026-02-07.zip`.

---

<!-- file: docs/03-build-the-csv.md -->

# 3. Build the CSV


Discord asks for a CSV file with one line per message:

```
channel_id,message_id
111111111111111111,100000000000000000
111111111111111111,100000000000000001
```

You don't need to write it by hand. Use the helper script, or one of the alternatives below.

## Option A: the helper script (recommended)

[`scripts/erasure_helper.py`](https://github.com/Technae/The-Erasure-Codex/blob/main/scripts/erasure_helper.py) is a single file that uses only standard Python 3. It reads your package **directly from the ZIP**, without extracting or changing it, and doesn't connect to the internet. If it meets a file or message record it can't read reliably, it stops with an error instead of quietly giving you a smaller CSV, and it only puts the CSV in place once the whole run has succeeded, so a failed run never leaves a half-written file. Read it before running it if you like: it's short.

**1. Install Python 3** if you don't have it ([python.org](https://www.python.org/downloads/)). On Linux and macOS it's usually already there.

**2. Download the script** and put it in the same folder as your package.

**3. See what's in your package:**

```bash
python3 erasure_helper.py summary package.zip
```

Example output (yours will differ):

```
Channel type            Channels    Messages
GUILD_TEXT                   240       51200
DM                            35       20400
GROUP_DM                       6        3100
TOTAL                        281       74700
```

**4. Write the CSV:**

```bash
python3 erasure_helper.py csv package.zip -o messages_to_delete.csv
```

On Windows, use `python` or `py` instead of `python3` if that's what works.

### Useful options

| Option | What it does |
|---|---|
| `--exclude keep.txt` | Leave out the channels listed in `keep.txt` (one channel ID per line), e.g. chats you want to keep |
| `--only these.txt` | Include only the channels listed in `these.txt` |
| `--split 100000` | Split into several files of at most 100,000 messages each, plus the header line (`messages_to_delete_part1.csv`, `_part2`, …), if one file is too big to send |
| `--no-header` | Leave out the `channel_id,message_id` header line |
| `--force` | Overwrite an output file that already exists. Without it, the script won't replace an existing file, and it never writes over the package itself or over the `--only`/`--exclude` lists |
| `--allow-incomplete` | Only if the script stops because some message records can't be read: write the CSV anyway, leaving those records out. It warns you how many. Please also [open an issue](https://github.com/Technae/The-Erasure-Codex/issues) so the script can be fixed |

To find a channel's ID in Discord, turn on **User Settings → Advanced → Developer Mode**, then right-click the channel or DM and choose **Copy Channel ID**.

## Option B: ishnz's bulk_deletion_helper

[bulk_deletion_helper](https://github.com/ishnz/bulk_deletion_helper) by ishnz is the tool linked in No Text To Speech's video, and the one this guide's author used for the requests in the [case study](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/09-case-study.md). Without it, this guide probably wouldn't exist. It's a set of small Python scripts that read your package locally. They don't connect to the internet or ask for your token.

1. **Extract a copy** of your package (keep the original ZIP untouched).
2. Put `dumpallmessages.py` in the extracted folder, next to the `Messages` folder.
3. Run it:

```bash
python3 dumpallmessages.py
```

It writes `messages.csv` in the same folder, with one `channel_id,message_id` line per message (its header line reads `channelid,messageid`, which Discord has accepted). The repository also has scripts to include or leave out a list of channels; see its README.

Good to know: it expects the current package layout (a `Messages` folder with a `messages.json` in each channel folder), and it has no option to split large files, so see "How big is too big?" below if yours is large.

## Option C: jq and a terminal

If you have [`jq`](https://jqlang.org/) and an **extracted copy** of a recent package (not your original):

```bash
cd extracted-package/Messages
for d in c*/; do
  id="${d#c}"; id="${id%/}"
  jq -r --arg c "$id" '.[] | "\($c),\(.ID)"' "$d/messages.json"
done > ../../messages_to_delete.csv
```

Older packages use `messages/` and `messages.csv` instead, so the script in Option A is easier for those.

## Option D: other tools

Community tools that read data packages exist, such as [undiscord-package-util](https://github.com/dorifor/undiscord-package-util), which the old Discordomicon guide linked to. Check what any tool does before trusting it with your package, and never use one that asks for your Discord token or password. Building the CSV only needs the package.

## What to include

**Everything you want erased.** Don't pre-filter for "messages with personal information" unless you want to. Discord's templates sometimes say the CSV is for messages containing personally identifiable information, but in practice it filters by access, not content (see the [case study](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/09-case-study.md)), and all of your messages relate to you.

**How big is too big?** Hundreds of thousands of lines are fine for Discord's process, but your email provider may limit attachment size (often around 20–25 MB). A CSV of 760,000 messages is about 30 MB. If yours is too big, either use `--split` and send the files in separate replies in the same thread, or compress it, or upload it to a file host and send a link. Links can expire or need permissions, so check that it opens in a private browser window.

**A note on support attachments:** in 2025 a breach at a third-party customer support provider used by Discord exposed data from support tickets. A CSV of IDs reveals little on its own, but don't attach anything you don't need to, especially ID documents.

---

<!-- file: docs/04-send-the-request.md -->

# 4. Send the request


## Where to send it

- **Email:** `privacy@discord.com`, with `dpo@discord.com` (Discord's Data Protection Officer) in copy.
- **Send it from the email address registered to your Discord account.** Discord uses that to confirm the request is yours.
- **Address it to the right company.** Discord's current privacy policy names **Discord Netherlands BV** as the data controller for users in the EEA, and **Discord Inc.** for everyone else, including users in the UK. It names VeraSafe as its UK representative. Check the current policy at [discord.com/privacy](https://discord.com/privacy) if you're unsure.

You can also use Discord's support form, but email gives you your own dated copy of everything, which is what you'll want if you complain later. Either way, Discord's replies come through its ticket system, and each ticket has a number. Note it down.

**Keep everything in one thread.** Reply to Discord's emails rather than starting new ones, keep the quoted text, and don't delete the tag in square brackets (like `[ABC123-DEF45]`). That's how the ticket system matches your reply to the request.

## Template: EU / EEA

Fill in the parts in square brackets. Delete the optional paragraph if you don't want it.

```
Subject: Erasure request under Article 17 GDPR – [your username]

To: privacy@discord.com
Cc: dpo@discord.com

Dear Discord Netherlands BV,

I am making a request for erasure under Article 17 of the General Data
Protection Regulation (GDPR). I live in [country].

My account:
  Username: [username]
  User ID: [your user ID]
  Registered email: [this email address]

Please erase the [number] messages listed in the attached CSV file
(channel_id, message_id), sent from my account across [number] channels.
This includes messages in channels and direct messages that I can still
access: being able to access a channel is not an exception under
Article 17(3).

I rely on Article 17(1)(a), as these messages are no longer necessary
for the purposes for which they were collected or processed.

To the extent that you keep these messages on the basis of legitimate
interests (Article 6(1)(f)), I also object under Article 21(1), on
grounds relating to my particular situation: [in a sentence or two, in
your own words, why you object]. Where that objection applies, I rely on
Article 17(1)(c).

This request covers these messages only. I want to keep my account.
Please do not delete, deactivate or disable it as part of handling this
request.

If you do not take action on any part of this request, please give me
your reasons and tell me that I can complain to a supervisory authority
and seek a judicial remedy, as Article 12(4) requires.

To help me understand and, if necessary, challenge your decision, please
also identify the messages or groups of messages you are keeping, the
purposes and legal basis for keeping them, and whether you consider that
no Article 17(1) ground applies, or rely on an exception under Article
17(3) or another justification under Article 21(1) (including the
establishment, exercise or defence of legal claims), and why it applies
to those messages.

[Optional: To the extent that you process the analytics and other
activity data linked to my account, including the data in the Activity
folder of my data package, on the basis of legitimate interests, I also
object to that processing under Article 21(1), on grounds relating to my
particular situation: [why you object], and ask for its erasure under
Article 17(1)(c).]

Please respond within one month of receiving this request, as
Article 12(3) requires, and confirm in writing which messages have been
erased. Please do not close this request until you have answered it.

Kind regards,
[name or username]
```

## Template: UK

The UK version is the same, with two changes: cite the **UK GDPR**, and say you're in the UK.

```
Subject: Erasure request under Article 17 UK GDPR – [your username]

To: privacy@discord.com
Cc: dpo@discord.com

Dear Discord,

I am making a request for erasure under Article 17 of the UK General
Data Protection Regulation (UK GDPR). I live in the United Kingdom.

My account:
  Username: [username]
  User ID: [your user ID]
  Registered email: [this email address]

Please erase the [number] messages listed in the attached CSV file
(channel_id, message_id), sent from my account across [number] channels.
This includes messages in channels and direct messages that I can still
access: being able to access a channel is not an exception under
Article 17(3).

I rely on Article 17(1)(a), as these messages are no longer necessary
for the purposes for which they were collected or processed.

To the extent that you keep these messages on the basis of legitimate
interests (Article 6(1)(f)), I also object under Article 21(1), on
grounds relating to my particular situation: [in a sentence or two, in
your own words, why you object]. Where that objection applies, I rely on
Article 17(1)(c).

This request covers these messages only. I want to keep my account.
Please do not delete, deactivate or disable it as part of handling this
request.

If you do not take action on any part of this request, please give me
your reasons and tell me how I can complain (to you under section 164A
of the Data Protection Act 2018, and to the Information Commissioner)
and seek a judicial remedy, as Article 12(4) requires.

To help me understand and, if necessary, challenge your decision, please
also identify the messages or groups of messages you are keeping, the
purposes and legal basis for keeping them, and whether you consider that
no Article 17(1) ground applies, or rely on an exception under Article
17(3) or another justification under Article 21(1) (including the
establishment, exercise or defence of legal claims), and why it applies
to those messages.

Please respond within one month of receiving this request, as
Article 12(3) requires, and confirm in writing which messages have been
erased. Please do not close this request until you have answered it.

Kind regards,
[name or username]
```

## Before you press send

- [ ] Sent **from your account's email address**
- [ ] The email says you want to **keep your account** (the templates include this line; don't remove it)
- [ ] You've filled in **why you object** in your own words (see below), or removed the objection paragraph if you don't want to object
- [ ] The CSV is attached, or the link works in a private browser window
- [ ] The numbers in the email match the CSV (the `summary` command gives you both)
- [ ] You've saved a copy of the email, the CSV, and its hash (`sha256sum messages_to_delete.csv`)
- [ ] You've written down today's date. **The one-month deadline starts when Discord receives your request.**

## Why you object, in your own words

An objection under Article 21(1) has to be made "on grounds relating to your particular situation", so the template leaves a gap for you to fill in. Write a sentence or two about your own reasons. For example: the messages contain personal details you no longer want stored, they're years old and you've left those communities, or you're worried about what they reveal about you. Use your real reasons, not a stock paragraph. It doesn't need to be long or legal. If you'd rather not object, delete that paragraph: the request still stands on Article 17(1)(a).

## Tips

- **Ask for your messages, not "all your data".** Broad wording like "delete all my personal data" can be read as a request to delete your account. At least one user has reported an agent deleting their whole account partway through a message request without being asked. Keep the line saying you want to keep your account.
- **Write in plain, calm language.** You don't need legal jargon beyond the article numbers, and threats don't help. A clear, polite request makes any later complaint much stronger.
- **Don't send ID documents** unless Discord gives a real reason to doubt who you are. Sending from your registered email is normally enough.
- **One request, one thread.** If you want to add something later, reply in the same thread rather than starting a new ticket, so your deadline and history stay together.

---

<!-- file: docs/05-replies-decoded.md -->

# 5. Discord's replies, decoded


Discord's privacy team mostly replies with templates. Recognising them saves you a lot of frustration. **A template isn't necessarily a complete or properly reasoned answer**, though it may still be a refusal: look at what it actually says. Does it explain what Discord won't erase, why it's keeping it, and how you can challenge the decision? Each section below quotes the template as users have received it in 2026, explains what it means, and gives a reply you can adapt.

Always reply **in the same email thread**, keeping the quoted text and the `[XXXXXX-XXXXX]` tag.

---

## "We don't offer the ability to delete your messages in bulk right now"

**What it looks like:** a long reply saying bulk deletion isn't offered, that other users "have a legitimate interest in having access to content sent to them", that "Discord balances the privacy interests of the user against the interests other users have in a conversation", the tip to hold Shift while clicking the delete icon, and the note that deleting your account "anonymizes" your messages. Near the end there's often a line offering to help with "specific messages containing personally identifying information that you no longer have access to".

**What it means:** this is the standard first response. It's not accurate as a full answer: Discord's privacy team *does* process bulk deletions from a CSV, and the line at the end is pointing at that process. The reply cites no exception under Article 17(3) and doesn't mention your right to complain.

**Reply:**

```
Thank you for your reply.

This is a request for erasure under Article 17 GDPR, not a feature
request. Your reply mentions helping with specific messages; please
process the attached CSV (channel_id, message_id), which lists the
messages I want erased.

If you will not erase some or all of them, please give me your reasons
and tell me that I can complain to a supervisory authority and seek a
judicial remedy, as Article 12(4) requires. Please also say which
messages you are keeping and what exception or other justification you
rely on (for example under Article 17(3), or Article 21(1), including
legal claims).
```

---

## "Please provide us with a CSV file of the messages containing personally identifying information"

**What it looks like:** "If, however, you believe you have sent messages which include specific identifiable personal data and/or sensitive personal data – your name, or other information about you – we can certainly help you remove such information… Please provide us with a CSV file… channel_id, message_id".

**What it means:** this is the CSV route. In practice Discord processes the whole CSV and filters by whether you can still access the space, not by what the messages say.

**Reply:** send the CSV (again, if you already have), and say:

```
Please find attached the CSV of the messages I want erased. All of them
are my personal data: they were written by me, are linked to my account,
and are included in my data package as my data.
```

---

## "We have successfully submitted the message IDs … for deletion"

**What it looks like:** a confirmation that the IDs were "submitted for deletion", with three exclusions: messages in spaces you still have access to, messages sent by other users, and invalid IDs.

**What it means:** messages in servers and group chats you've left will probably be deleted. Messages anywhere you can still open, including DMs, probably won't. "Submitted" isn't "deleted", so check ([Step 6](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md)).

**Reply** (after checking):

```
Thank you. Comparing my data packages from [date] and [date],
[number] of the [number] messages I asked you to erase are still present.
They are listed in the attached file.

Please erase them, or explain your reasons for keeping each group of
messages, including any exception under Article 17(3) or other
justification under Article 21(1) (such as legal claims) that you rely
on. Please also explain what you
mean by spaces I "have access to", since that is not a ground for refusal
in the GDPR.
```

The helper script's `compare … --remaining remaining.csv` option writes that file for you.

---

## "Access permissions are managed dynamically"

**What it looks like:** "We are unable to provide further internal details, as access permissions are managed dynamically", usually with a suggestion to delete messages manually.

**What it means:** Discord won't define "access". This is the point where many people give up. Don't: you now have a clear record that Discord has refused part of your request without giving a legal reason.

**Reply:** send one final, short message, optionally escalate to the Data Protection Officer ([DPO template 1](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#dpo-template-1-escalating-an-erasure-request)), then move on to [Step 7](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/07-deadlines-and-complaints.md). Escalating doesn't restart the deadline on your original request.

```
Thank you. You have not erased [number] of the messages I asked you to
erase, and have not given reasons for keeping them: you have not identified
the purpose and legal basis, or explained why it applies to these
messages. Unless I
receive that information, or confirmation that they have been erased,
within the one-month period under Article 12(3), I will complain to
[your data protection authority].
```

UK users: the ICO recommends complaining to the company before you go to it, and in most cases will ask you to. Make it explicit: *"Please treat this as a data protection complaint under section 164A of the Data Protection Act 2018."* Discord then has 30 days to acknowledge it.

---

## The ticket is marked "solved" without an answer

**What it looks like:** an email saying your request has been solved, or a support-site ticket showing "Solved" when nothing was answered. Some replies come from a profile named "Clyde (Discord Support)", the name of Discord's system bot. Users widely report these as automated.

**What it means:** the ticket system closed it. It doesn't change your legal deadline, which runs from when Discord received your request.

**Reply:** reply in the same thread to reopen it. Screenshot the "Solved" status with the date first.

```
This request has been marked as solved, but it has not been answered.
Please reopen it. My request for erasure under Article 17 GDPR of
[date] is still outstanding, and the one-month deadline under
Article 12(3) runs from that date.
```

---

## Nothing at all

If a month passes with no reply and no notice of an extension, Discord has missed the deadline. See [Step 7](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/07-deadlines-and-complaints.md).

## General tips

- **Answer what they said, briefly.** Long replies get templated answers too.
- **Repeat the key question every time:** which exception do you rely on, and why does it apply to these messages? A refusal without real reasons (Article 12(4)) is the strongest thing you can show a regulator.
- **Save every reply,** with its date. Use your email client's "download message" or "show original" option to keep a full copy.
- **Stay calm.** Your messages may end up in front of a regulator, so write as if they'll read them.

---

<!-- file: docs/06-check-the-result.md -->

# 6. Check the result


A confirmation email tells you what Discord *submitted*, not what it deleted. Comparing a data package from before your request with one from afterwards shows which messages are no longer in the export, and spot-checking in the app shows whether they're still visible. Neither proves that every copy has been erased (see below).

## When to request the second package

Wait until Discord has confirmed processing, then give it a week or two before requesting a new package. Remember that you can usually only request one about every 30 days.

## Compare with the helper script

Put both ZIP files in the same folder as the script:

```bash
python3 erasure_helper.py compare package-before.zip package-after.zip
```

```
Old export: 762269 messages
New export: 640380 messages
No longer in export (in old, not in new): 121948
Present in both exports:                  640321
New in newer export:                      59
Share of old messages no longer exported: 16.0%
Note: this shows what Discord's export no longer includes.
It can't show whether every copy, including backups, has been erased.
```

(These are the real figures from the [case study](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/09-case-study.md), comparing the February and March 2026 packages. The case study's later figure of 640,314 comes from a September package.)

Two options make the result more useful:

```bash
python3 erasure_helper.py compare package-before.zip package-after.zip \
    --report per_channel.csv --remaining remaining.csv
```

- **`per_channel.csv`** shows, for every channel, how many messages are no longer in the export and how many are still there. It's the clearest way to see the "accessible space" rule at work: channels you'd left go to zero, channels you're still in don't change. **It includes channel names, so don't post it publicly.**
- **`remaining.csv`** lists every message that's in both exports, in the `channel_id,message_id` format, ready to send in your follow-up.

The script compares each message together with its channel, the same pairs as in the CSV. If it can't read a package reliably (for example, because Discord has changed the export format, or some message records have no readable ID), it stops with an error rather than reporting a misleading count. It won't write its output over either package, and a failed run leaves any earlier report untouched; add `--force` if you want it to overwrite an earlier report.

## Without the script

With extracted copies of both packages (not the originals), make a list of message IDs from each:

```bash
jq -r '.[].ID' Messages/c*/messages.json | sort -u > ids.txt
```

Then, in the folder above both:

```bash
comm -23 before/ids.txt after/ids.txt | wc -l   # removed
comm -12 before/ids.txt after/ids.txt | wc -l   # still present
```

## Things that can confuse the count

- **Messages you deleted yourself** in the meantime will show as "removed". If you've been deleting by hand, note roughly how many.
- **New messages** you've sent since the first package show up as "new", not as failures.
- **Missing messages:** some users report packages that seem to leave out messages. If a number looks odd, spot-check a few IDs in the app. With Developer Mode on, you can open a message directly at `https://discord.com/channels/@me/CHANNEL_ID/MESSAGE_ID` for a DM, or `https://discord.com/channels/SERVER_ID/CHANNEL_ID/MESSAGE_ID` for a server.

## What a comparison can and can't show

Three different things are easy to confuse:
1. **A message is missing from your new data package.** That's what the comparison shows: Discord's export no longer includes it.
2. **A message is gone from Discord's live systems.** That's what you see when it no longer appears in the app. It's the strongest practical check you have.
3. **Every copy is gone, including backups.** Backups are normally overwritten over a period of time, not instantly. A company may also keep some data for a limited time where an exception applies. You can't see backups. Discord's [retention article](https://support.discord.com/hc/en-us/articles/5431812448791) says its database backups are kept for 30–45 days and then deleted, and that clearing identifying information from backups after an account deletion can take up to 45 days. That's Discord's own published figure, not something you can check, but it gives you a specific point to ask about.

Discord's own pages don't fully agree here. Its [data package article](https://support.discord.com/hc/en-us/articles/360004957991) says a deleted message "is no longer stored in Discord". Its [retention article](https://support.discord.com/hc/en-us/articles/5431812448791) says public posts may be kept for 180 days to two years after deletion. So a message missing from your package may still exist in another Discord system. If that matters to you, ask, using the [general access request](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#access-request-everything-discord-holds-about-you-general-dsar).

So report your results precisely: "these messages are no longer in my data package or visible in the app" is accurate. "Discord has erased every copy" is something only Discord can confirm.

## Keep the evidence

Record the hash of the new package (see [Step 2](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/02-get-your-data.md)), and keep the output of the comparison with the date. If you complain, these figures, alongside Discord's confirmation emails, are your strongest evidence.

---

<!-- file: docs/07-deadlines-and-complaints.md -->

# 7. Deadlines and complaints


## The deadline

Under **Article 12(3)**, Discord must tell you what it has done about your request **within one month** of receiving it. It can extend that by up to two more months for complex requests, but **only if it tells you so, with reasons, within the first month**.

If the month ends and you have neither an answer nor a notice of extension, the deadline has been missed. If Discord refuses part of your request, Article 12(4) requires it to tell you why and that you can complain. A template that does neither isn't a valid answer.

Counting: a month runs from the day Discord received your request to the same date the following month. If that falls on a weekend or public holiday, it moves to the next working day.

In the UK, Article 12A counts the month from the latest of: when Discord receives your request, when it receives identity information it reasonably asked for, or when any fee is paid. For access requests only, the clock can also pause while Discord waits for information it reasonably needs to identify what you're asking for. See the [legal reference](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/10-legal-reference.md).

Keep a simple log:

| Date | What happened | Evidence |
|---|---|---|
| 2 Feb | Request sent to privacy@discord.com | Sent email |
| 2 Feb | Template: "we don't offer bulk deletion" | Email |
| … | … | … |

## Optional: write to the DPO

Writing to Discord's Data Protection Officer (`dpo@discord.com`) is optional, not a required step before you complain. It doesn't restart or extend the deadline on your original request: that still runs from when Discord received it. Only a genuinely new request (for example, an access request you hadn't made before) has its own one-month period. So far, mail to the DPO has only drawn support templates, but even silence is useful: an unanswered message to the person responsible for data protection adds to the evidence that Discord missed its deadline under Article 12(3). [Templates](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md) has ready-to-use DPO emails.

However frustrating the replies get, aim your complaint at Discord as a company, not at the individual staff who sent them. Name the company in your complaint, not the agent who signed a template; the regulator deals with Discord, not its employees.

## Complaining in the EU / EEA

You can complain to the data protection authority **in the country where you live** (or where you work, or where the infringement took place), even though Discord's EU company is in the Netherlands. In a cross-border case, the authorities involved coordinate under the GDPR's cooperation procedure, and the one you complain to isn't necessarily the one that leads. You don't need to work out which one leads yourself.

- **Find your authority:** the [European Data Protection Board's list of members](https://www.edpb.europa.eu/about-edpb/about-edpb/members_en) has the website for each country. Most have an online complaint form in your language.
- **It's free,** and you don't need a lawyer.
- **Expect it to take months.** Cross-border cases are slow. Authorities often don't acknowledge follow-up emails, and that's normal.

**What to include** (a ready-made version is in [Templates](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#complaint-template-eu--eea-data-protection-authority)):
1. Who you are, and your Discord username and user ID
2. The company: **Discord Netherlands BV**
3. What you asked for, and when (attach your request)
4. Every reply from Discord, word for word, with dates (attach the emails)
5. What happened: the before/after figures from [Step 6](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md), and a record of the effort involved (see [Your effort is evidence](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#your-effort-is-evidence))
6. What's wrong, in plain words. For example: no answer within a month; a refusal with no legal basis; no information about your right to complain; messages kept that you asked to be erased
7. What you want: the authority to require Discord to erase your messages and to answer your request properly. You can also ask it to look at whether Discord's process is lawful in general

**Optional:** if you want your complaint to push Discord to change its process for everyone, and not just get your own messages deleted, you can state your position on **amicable resolution** at the start. It may slow down your own result, so read [the note in Templates](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#amicable-resolution-stating-your-position) first.

Keep it factual. Let the evidence show the problem. Words like "malicious" don't help, while dates, quotes and numbers do.

**After you complain:** you can still write to Discord, and anything new it sends is worth forwarding to the authority with your case reference. In the EU/EEA, if the authority hasn't handled your complaint, or told you how it's progressing, within three months, Article 78(2) lets you take the authority to court. That's rarely needed, but worth knowing. (UK: see section 166 below.)

## Complaining in the UK

The process changed on **19 June 2026**. Under section 164A of the Data Protection Act 2018, you can complain to the company itself. The ICO says you can complain to it at any time, but recommends **complaining to the company first**, and in most cases will ask you to:

1. Write to Discord (reply in the same thread) saying clearly that it's **a data protection complaint under section 164A of the Data Protection Act 2018**, and what you're complaining about.
2. Discord must **acknowledge it within 30 days**, investigate, and tell you the outcome without undue delay.
3. If you're not satisfied with the outcome, or Discord doesn't respond, complain to the **Information Commissioner's Office (ICO)**: [ico.org.uk/make-a-complaint](https://ico.org.uk/make-a-complaint/data-protection-complaints/). Include the same evidence as above, plus your section 164A complaint and Discord's response. The ICO's guidance asks you to complain within three months of your last meaningful contact with the company. That's the ICO's expectation, not a legal time limit, but it's worth keeping to.
4. If the ICO doesn't take appropriate steps on your complaint, or doesn't tell you how it's progressing within three months (and every three months after that while it's unresolved), section 166 of the Data Protection Act 2018 lets you apply to the tribunal for an order requiring it to.

## Other options

- **Data protection organisations** such as [noyb](https://noyb.eu/) in Europe sometimes take up cases that affect many people. Their membership schemes can include legal advice.
- **Courts:** you can take Discord to court yourself (Article 79), and claim compensation for harm (Article 82). That costs money and carries risk, so get advice first.

## Why complaining matters

Each complaint is a data point. A regulator that receives one complaint can treat it as one person's problem. Many complaints, each with clear evidence of the same templates and the same unexplained refusals, show a pattern. That's what gets a process changed.

---

<!-- file: docs/08-faq.md -->

# 8. FAQ


**Can't I just use a script to delete my messages myself?**
Tools that automate your account (often called self-bots) exist, but Discord's terms don't allow automating user accounts, and Discord can terminate accounts for it. [Undiscord](https://github.com/victornpb/undiscord)'s own README warns that using it could get your account terminated. The GDPR route puts the work on Discord, which is where the law puts it.

**Will an erasure request delete my account?**
It shouldn't. A request under Article 17 covers what you ask for and nothing more, so ask for your messages, not "all your personal data", and say plainly that you want to keep your account. The templates in this guide include that line. It matters because at least one user has reported an agent deleting their whole account partway through a message request without being asked, which also left them unable to follow up. If it happens to you, reply in the same thread straight away, point to the line in your request, and include it in any complaint.

**Does deleting my account delete my messages?**
No. Discord says it anonymises them: your username is replaced with "Deleted User", and your email and IP addresses are removed. The messages stay. Make your erasure request, and check the result, **before** you delete your account. Once your account is deleted or pending deletion, you can't make requests through it. You can still make them by email (see [Deleted or banned accounts](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/12-banned-accounts.md)), but it's harder.

**What about DMs with people who've deleted their accounts?**
You can usually still open them, so under Discord's "access" rule they tend to be kept. But nobody else is left to benefit from keeping them, which makes "other users have a legitimate interest" hard to apply. Point that out in your follow-up, and list those channel IDs separately.

**I want to help change how Discord handles this. Can I make a request for that reason?**
Make each request about **your own data, for your own reasons**: you want your messages erased, or you want to know what Discord holds about you. Those are the purposes the rights exist for. In 2026 the EU's Court of Justice held that a company can refuse even a first request if it shows the request was made with abusive intent rather than to protect the person's rights (Brillen Rottler, C-526/24). That case was about an access request, not erasure, but the principle is worth keeping in mind. A real request about your own messages is nothing like that. So keep requests to your own data, ask for what you actually want, and don't send requests just to test Discord or to build a case. If you later share your result, that helps other people know their options, but it should be a side effect, not the reason for the request.

**Does my data package include messages I deleted?**
No. Discord's [data package article](https://support.discord.com/hc/en-us/articles/360004957991) says a message you delete is "no longer stored in Discord" and won't be in your package. But Discord's [retention article](https://support.discord.com/hc/en-us/articles/5431812448791) says some public posts may be kept for 180 days to two years after deletion. If Discord still holds any deleted messages, your package won't show them. To ask about them, use item 1(e) of the [general access request](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#access-request-everything-discord-holds-about-you-general-dsar).

**Will Discord ban me for making a request?**
Exercising your legal rights isn't against Discord's rules, and we know of no case where a request led to a ban.

**Do I have to leave servers first?**
No. The law doesn't require it. In practice, leaving is what currently gets messages deleted. See [Step 1](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/01-how-it-works.md) for what leaving costs you.

**What about servers I own?**
You can delete channels, or the whole server, yourself. That removes everyone's messages, not just yours, so warn other members first. For servers you own but want to keep, include those channels in your CSV like any other.

**Does this cover other people's messages to me?**
Mostly not. This guide's CSV process covers messages you sent. You can't ask for someone else's messages to be erased just because they were sent to you. But a message written by someone else can contain personal data about *you*, for example your name, address or photo. You can ask for that to be erased, subject to the same Article 17 conditions and the rights of the person who wrote it.

**Discord asked me for ID. Should I send it?**
Article 12(6) lets a company ask for more information if it has *reasonable doubts* about who you are. If you're writing from your account's registered email, that's normally enough. Ask why they doubt it before sending any documents. An EDPB-commissioned case digest on erasure says that requiring ID by default isn't acceptable. There are better ways to show the account is yours, and what to do if Discord insists: see [Proving it's your account](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/12-banned-accounts.md#proving-its-your-account).

**My data package seems to be missing messages.**
Others have reported the same. Note what seems to be missing and how you know (for example, a message you can see in the app that isn't in the package), and mention it in your follow-up. You also have a right of access under Article 15 to a complete copy of your data ([general access request](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#access-request-everything-discord-holds-about-you-general-dsar)).

**Can I ask about the other data in my package?**
Yes. The `Activity` folders can contain years of analytics events with device, network and location details. You can ask what it's used for, the legal basis and how long it's kept (Article 15), object to it (Article 21), and ask for it to be erased (Article 17). You can also limit future collection in **User Settings → Data & Privacy**.

**How long does all this take?**
Building and sending the request takes an hour or two. Expect a few weeks of back and forth with Discord, a month or so between data packages, and months if you complain to a regulator.

**My account is deleted or banned. Can I still do this?**
Yes. Deletion or a ban doesn't end your GDPR rights. You can ask for your data and for your ordinary messages to be erased by email. If you're banned, erasure isn't an appeal, and the two can conflict. See [Deleted or banned accounts](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/12-banned-accounts.md).

**I'm not in the EU, EEA or UK.**
This guide only covers the GDPR and UK GDPR. Some other places, such as California, have their own deletion rights with different rules. If you know them well, consider contributing a section.

**Is any of this legal advice?**
No. It's what users have learned from their own requests. For anything important, get advice from a lawyer or a data protection organisation.

---

<!-- file: docs/09-case-study.md -->

# 9. Case study: one request in 2026


This is one user's request, from Ireland, with real figures and Discord's real replies. The user also [posted it in Undiscord discussion #429](https://github.com/victornpb/undiscord/discussions/429), where they're updating it as deadlines pass.

## Summary

- **762,269** messages in the February 2026 data package
- **121,948** removed by mid-March (16%), almost all in servers and group chats the user had already left
- **640,321** still present: everything the user could still open
- By September 2026, **99.3% of the messages still in the account (635,544 of 640,314) were in DMs**. Only 4,339 were left in server channels, 364 in group chats, 64 in threads and 3 in voice channels. You can't leave a DM, so the "access" rule spares almost nothing else
- Complaint filed with the Irish Data Protection Commission (DPC) in March/April 2026. In June it moved to the DPC's Cross Border Assessment team, and as of November 2026 it had no case officer
- Four formal requests to Discord's Data Protection Officer were open in November 2026, with deadlines of 4, 9, 9 and 23 November

## What Discord said, and what it did

The first reply (2 February 2026):

> We don't offer the ability to delete your messages in bulk right now.

It explained that other users "have a legitimate interest in having access to content sent to them", and that "Consistent with GDPR, Discord balances the privacy interests of the user against the interests other users have in a conversation". It cited no exception and didn't mention the right to complain.

Eight days later, after a follow-up, the same team wrote:

> If, however, you believe you have sent messages which include specific identifiable personal data and/or sensitive personal data - your name, or other information about you - we can certainly help you remove such information. […] Please provide us with a CSV file of the messages containing personally identifying information in the following format: channel_id, message_id

The user sent CSVs listing every message in the data package, four in all, between 7 and 25 February. Discord confirmed each batch as "submitted for deletion", except messages in spaces the user could still access, other users' messages, and invalid IDs.

**So bulk deletion exists:** Discord removed 121,948 messages from CSVs, with no sign of a per-message review for personal data. What decided deletion was access, not content.

On 10 March, asked to define "access", Discord replied that it was "unable to provide further internal details, as access permissions are managed dynamically".

## The case that shows the rule

The user has two accounts. Both accounts asked for the DM *between them* to be erased. Both accounts belong to the same person, so there's no separate human counterparty to the conversation. **Both accounts received "submitted for deletion" confirmations (12 and 18 March 2026). Nothing was deleted.** Its 2,509 messages were still present in a September 2026 package.

The same happened with DMs where the other person had deleted their account: 32,515 messages in one, 8,214 in another, and 165 in a third. Nobody else is left to "keep access" to those.

## The questions that were never answered

Between February and March 2026, the user asked, in writing:
- which data (metadata, logs, IP addresses, analytics) would be erased or kept, and on what legal basis (3 and 11 February, 11 March)
- for a justification for each message not deleted (16 February)
- for escalation to the Data Protection Officer (25 February)
- what "access" means, and which Article 17(3) exception applies (3 March)
- how the legitimate-interest balancing test was carried out for analytics data kept for years (21 March)

None got a substantive answer. Tickets were marked "solved".

## Writing to the Data Protection Officer

On 27 September 2026 the user wrote to dpo@discord.com. The email became an ordinary support ticket, got a template reply signed "Clyde (Discord Support)" pointing to help articles, and was marked "solved" the next day. By November, the same reply showed on the support site as "Discord Support". The original email notification still shows "Clyde".

The user then turned the questions into formal requests in the same ticket, which reopened it:

| Sent | Request | Deadline |
|---|---|---|
| 4 Oct | Access to analytics data (purposes, legal basis, recipients, retention); objection to and erasure of it; the legal basis for keeping two specific DMs | 4 Nov |
| 8 Oct | Erase two DMs with deleted users, or state the exception and whose interests it protects | 9 Nov |
| 8 Oct | Access request for an account Discord deleted for inactivity in 2024 | 9 Nov |
| 21 Oct | Access: retention after account deletion, use for model training, recipients, transfers | 23 Nov |

## The same template, elsewhere

This isn't one person's experience. In Undiscord #429:
- [**A user in France (June 2026)**](https://github.com/victornpb/undiscord/discussions/429#discussioncomment-17448893) got the same first reply, almost word for word. They asked twice which GDPR provision Discord relied on. The second reply repeated "As previously stated…", dropped the line about helping with personal information, and cited nothing. After they said they'd complained to the CNIL, the ticket was marked solved.
- [**Another user (July 2026)**](https://github.com/victornpb/undiscord/discussions/429#discussioncomment-17536812) got the same "not offered" answer and the Shift-click tip, and their follow-up ticket was closed.

## How Discord's handling has changed

From reports in Undiscord #429 (user reports, not verified):
- **2022 and 2024:** a few users got whole channels, or most of their messages, deleted after involving a regulator (the Dutch authority in one 2022 case).
- **Mid-2024 to early 2025:** CSV requests mostly worked, including some of several hundred thousand messages.
- **Late 2024:** Discord started insisting on a CSV, without publishing a format.
- **February 2025:** the first reports of refusals for spaces the user can still access.
- **May 2025 onwards:** Discord declines to define "access", using the same "managed dynamically" wording quoted above.
- **2026:** first replies routinely say bulk deletion isn't offered.

## Lessons

1. **Don't stop at the first reply.** The CSV route only appeared after pushing back.
2. **Check, don't trust.** "Submitted for deletion" covered messages that were never deleted.
3. **Ask the same question every time:** which exception? Months of unanswered questions are themselves the evidence.
4. **Keep everything,** with dates and hashes, from the start.

---

<!-- file: docs/10-legal-reference.md -->

# 10. Legal reference


A quick reference to the provisions this guide relies on. Most article numbers are the same in the GDPR and the UK GDPR, but UK law has since added some provisions and removed others. The differences that matter here are in the UK note below. Read the full text at [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj) (GDPR) or [legislation.gov.uk](https://www.legislation.gov.uk/eur/2016/679/contents) (UK GDPR).

## The articles

| Article | What it says, in short | Why it matters here |
|---|---|---|
| **6(1)(b)** | Processing necessary for a contract *with you* | Discord's privacy policy lists storing and displaying messages "as you direct" under its contract with you. If that's the basis, your ground is 17(1)(a). See [which ground applies](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/01-how-it-works.md#which-erasure-ground-applies) |
| **6(1)(f)** | Processing based on legitimate interests | What Discord's template replies suggest (other users' interest in reading your messages), though Discord hasn't formally said so. If that's the basis, you can object (Article 21) and rely on 17(1)(c) |
| **12(1)** | Information must be concise, transparent, clear and easy to access | A first reply saying bulk deletion "isn't offered", when a CSV process exists, is hard to square with this |
| **12(2)** | The company must *facilitate* the exercise of your rights | Building your own CSV, or deleting hundreds of thousands of messages by hand, isn't much facilitation |
| **Recital 59** | Explains 12(2): there should be mechanisms to request and obtain erasure, free of charge, including electronically where data is processed electronically | Discord processes everything electronically, but has no electronic way to request erasure at scale |
| **12(3)** | Answer within one month; extend by two months only with notice and reasons within the first month | Your deadline |
| **12(4)** | If it doesn't act, it must say why and tell you about your right to complain and go to court | Template replies don't do this |
| **12(5)** | Requests are free; refusing as "manifestly unfounded or excessive" is possible, but the company has to prove it. In *Brillen Rottler* (C-526/24, 2026), the CJEU held that even a first request can be excessive if the company shows it was made with abusive intent, rather than to protect the person's rights. That case concerned an access request (Article 15); it isn't a ruling that an erasure request can be refused because the person also wants to understand or challenge the company's practices | Asking for your own messages to be erased is neither. Make each request about your own data, for your own reasons ([FAQ](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/08-faq.md)) |
| **12(6)** | It can ask for more information only if it has reasonable doubts about who you are | Writing from your registered email is normally enough |
| **15** | Right of access: a copy of your data and information about its use (purposes, recipients, retention, source, automated decisions) | Your data package, and questions about analytics data. Article 15 doesn't list the legal basis itself; the templates ask for it because Discord had to tell you it anyway (Articles 13(1)(c) and 14(1)(c)) |
| **17(1)** | Where a ground applies, the company must erase *without undue delay* | Separate from the 12(3) deadline to tell you what it has done |
| **17(1)(a)** | Erasure when the data is no longer necessary for the purpose it was collected or processed for | The question is whether keeping your messages is still necessary for Discord's purpose. Your request is relevant, but doesn't settle it alone |
| **17(1)(c)** | Erasure when you object under Article 21(1) and there are no overriding legitimate grounds for the processing | Discord's replies describe "legitimate interests" for keeping messages for others |
| **17(1)(d)** | Erasure when the data has been processed unlawfully | A fallback, if Discord has no valid legal basis at all |
| **17(3)** | The specific exceptions: freedom of expression and information, legal obligation, public interest in public health, archiving or research, legal claims | The replies quoted in the case study cite none of them. A company can also argue that no 17(1) ground applies |
| **21(1)** | Right to object, on grounds relating to your particular situation, to processing based on legitimate interests (or a public task); the company must stop unless it shows *compelling* legitimate grounds that override your interests, rights and freedoms, or that the processing is needed to establish, exercise or defend legal claims | Make the objection explicit, and give your own reasons briefly ([Step 4](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/04-send-the-request.md#why-you-object-in-your-own-words)) |
| **25** | Data protection by design and by default | The argument that a platform holding this much data should be designed so that erasure works at that scale. The law doesn't prescribe a particular feature, only that the right is effective |
| **38(4)** | You can contact the Data Protection Officer about your rights | Discord's DPO address feeds into its general support queue |
| **77** | Right to complain to a supervisory authority, in particular where you live, work or where the infringement took place (EU/EEA only; see the UK note below) | Step 7 |
| **78(2)** | Court remedy if the authority doesn't handle your complaint or tell you its progress within three months (EU/EEA; in the UK, see section 166 below) | A fallback |
| **79, 82** | Court action against the company; compensation | Costly; get advice |

**National restrictions:** EU and EEA countries can add limited restrictions to these rights (Article 23) and must reconcile data protection with freedom of expression (Article 85). Ireland's Data Protection Act 2018, for example, has provisions on both. This guide doesn't cover them country by country.

**UK only:** the UK complaints system changed on 19 June 2026 (Data (Use and Access) Act 2025, section 103).
- **Section 164A** of the Data Protection Act 2018 gives you the right to complain to the company. It must acknowledge your complaint within 30 days and tell you the outcome without undue delay. The 30 days is for the acknowledgement, not for resolving the complaint.
- **Article 77 has been removed from the UK GDPR.** Complaints to the ICO are now made under **section 165** of the Data Protection Act 2018. The ICO says you can complain to it at any time, but recommends giving the company the chance to finish its complaints process first, and in most cases it will ask you to do that. Its guidance also asks you to complain within three months of your last meaningful contact with the company; that's the ICO's expectation, not a statutory time limit.
- **Controller:** Discord's privacy policy names Discord Netherlands BV for the EEA and Discord Inc. for everyone else, including the UK. It names VeraSafe as its UK representative.
- **Response times (Article 12A):** since 5 February 2026, the UK GDPR sets out how the one-month period is counted. It starts from the latest of: when the company receives your request, when it receives information it reasonably asked for to confirm who you are (Article 12(6)), or when any fee is paid. For **access requests (Article 15) only**, the clock can also pause while the company waits for information it reasonably needs to identify what your request covers, for example where it holds a large amount of information about you. This isn't a general pause for any question the company asks, and none of it applies to EU/EEA requests.
- **Article 12(4) (UK version):** when a company doesn't act on a request, it must now tell you about complaining to it under section 164A and to the ICO under section 165, as well as seeking a judicial remedy.
- **Section 166** of the Data Protection Act 2018 is the UK route if the ICO doesn't take appropriate steps on your complaint or keep you informed of its progress (within three months, and every three months after that while it's unresolved): you can apply to the tribunal for an order requiring it to. Use this instead of Article 78(2) in the UK.

## Decisions and guidance worth knowing

- **CNIL fine against Discord (November 2022):** France's authority fined Discord €800,000. The failings included not having a written data retention policy.
- **Irish DPC decision on Twitter (April 2022):** the DPC found Twitter had breached Articles 12(3) and 17 in handling an erasure request, and ordered it to change its erasure procedures. It's a useful example of a regulator acting on how requests are handled, not just on the outcome.
- **One-stop-shop case digest on the rights to object and to erasure (2022, updated May 2026):** a summary of decisions by European authorities, commissioned by the EDPB through its Support Pool of Experts and written by external experts. It isn't an official EDPB position or binding guidance, but the decisions it summarises are real. It says controllers must facilitate erasure without creating cumbersome procedures, and that demanding ID by default isn't acceptable. One example it gives is a useful analogy for Discord's handling of mail to its DPO, though the facts aren't identical: a company gave an email address for rights requests, but an automated reply sent people to its "Contact us" form instead (French decision FR:OSS:D:2022:326). The digest calls that a cumbersome procedure. [Read it on the EDPB site](https://www.edpb.europa.eu/documents/support-pool-of-experts/one-stop-shop-case-digest-on-right-to-object-and-right-to-erasure_en).
- **EDPB Guidelines 03/2022 on deceptive design patterns (adopted February 2023):** for exercising rights such as erasure, the number of steps "should therefore be as low as possible", and too many steps infringes the fairness principle and Articles 12(1) and (2). A "dead end", where users have no way to exercise a right, directly infringes Article 12(2). These passages are about the design of social-media interfaces and settings. They support the general point that exercising rights should be easy, but don't set a maximum number of steps for every request.
- **EDPB coordinated enforcement report on the right to erasure (February 2026):** the result of a coordinated review by 32 European data protection authorities, carried out during 2025, of how organisations handle erasure requests. Many of the problems it describes are the ones in this guide.

## Discord's own statements

- Its privacy policy names **Discord Netherlands BV** as the data controller for users in the EEA.
- Its [Terms of Service](https://discord.com/terms) (effective 29 September 2025) say you have "certain rights that, by law, can't be limited by these terms", and that Discord doesn't intend to restrict them. So nothing in Discord's terms or help pages can take away your GDPR rights.
- Its help article on data retention says content is kept after account deletion so that other users keep access to it.
- Its template replies say Discord "balances the privacy interests of the user against the interests other users have in a conversation". As far as we know, it has never published that balancing assessment or given one to a user who asked.
- Its template replies also describe your messages as "part of the sender's personal data".

## Not legal advice

This page summarises the law for orientation. It doesn't cover every exception or national variation, and the law changes. If you're making decisions that matter, check the source text and get advice.

---

<!-- file: docs/11-templates.md -->

# 11. Templates: Discord's DPO and data protection authorities


This page collects templates for the later stages: writing to **Discord's Data Protection Officer (DPO)**, and **complaining to a data protection authority**. For the first request, see [Step 4](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/04-send-the-request.md). For replies to Discord's support templates, see [Step 5](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/05-replies-decoded.md).

Fill in the parts in square brackets, and delete anything that doesn't apply to you.

---

## Why write to the DPO even if you don't expect an answer

Discord has a Data Protection Officer, and the GDPR gives you the right to contact them about your rights (Article 38(4)). In our experience, mail to `dpo@discord.com` ends up in Discord's ordinary support queue. The case study's email to the DPO got a support template and was marked "solved" the next day, with no reply from the DPO. Users in Undiscord #429 report the same.

**Writing is optional, but useful.** It puts on record that you went to the person responsible for data protection and asked for an answer under the GDPR. It doesn't restart or extend the deadline on your original request, which still runs from when Discord received it. A genuinely new request in the same email (for example, an access request you hadn't made before) has its own one-month period.

If the original deadline passes without an adequate response or a valid extension notice, that may be a failure to comply with Article 12(3) and, if Discord refuses without giving reasons, Article 12(4). The duty to answer belongs to Discord as the controller rather than to the DPO personally. An unanswered DPO escalation is useful extra evidence, but it doesn't create a separate deadline. A missed deadline is some of the easiest evidence for an authority to act on, because it doesn't depend on any argument about what Discord may keep: either Discord answered in time, or it didn't.

**How to send it:**
- **To:** `dpo@discord.com`, **Cc:** `privacy@discord.com`
- **From** your account's registered email address
- **Mention your earlier ticket numbers,** so the DPO's office can't treat it as a new, unrelated query
- **One subject per email,** with the articles in the subject line. Several separate requests are harder to answer with a single template
- **Diary the original deadline:** one month from when Discord received your original request. A genuinely new request has its own deadline, from when Discord receives it

If it gets a support template and a "solved" status, reply in the same thread if further contact is useful (see [Step 5](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/05-replies-decoded.md)), and keep the correspondence. The ticket may reopen, but its status doesn't reset or extend the legal deadline.

---

## DPO template 1: Escalating an erasure request

Use this when Discord's privacy team has refused part of your request, or answered with templates, and you want the DPO to deal with it.

```
Subject: Erasure request under Article 17 GDPR – escalation to the Data
Protection Officer – [ticket number(s)]

To: dpo@discord.com
Cc: privacy@discord.com

Dear Data Protection Officer,

I am contacting you under Article 38(4) GDPR about my request for
erasure under Article 17, which has not been dealt with.

My account: [username], user ID [user ID], registered email [address].
Earlier tickets: [ticket numbers], from [date of first request].

On [date] I asked Discord to erase the [number] messages listed in the
attached CSV file (channel_id, message_id). Comparing my data packages
of [date] and [date], [number] of them have not been erased. The replies
I received said that messages in spaces I "have access to" are excluded,
and that access permissions are "managed dynamically". Being able to
access a channel is not an exception under Article 17(3), and "managed
dynamically" is not a reason under Article 12(4).

Discord's stated reason is that other users rely on these messages for
context. But Discord lets me delete each of the same messages myself,
one at a time, which affects other users in exactly the same way, and
it has already erased messages in bulk from servers that other members
can still read. Please explain why conversation context justifies
refusing my request, but not individual deletion or the erasure you have
already carried out.

Please either:
1. erase the remaining messages, which are listed in the attached file;
   or
2. give me your reasons, and tell me that I can complain to a
   supervisory authority and seek a judicial remedy, as Article 12(4)
   requires. To help me understand your decision, please also say, for
   each group of messages you are keeping, whether you consider that no
   Article 17(1) ground applies, or which exception under Article 17(3)
   or other justification under Article 21(1) (including legal claims)
   you rely on, and why it applies.

As in my original request, I am asking for my messages to be erased,
not my account. Please do not delete, deactivate or disable my account.

The one-month period under Article 12(3) ran from my original request
on [date]. Please reply in writing.

Kind regards,
[name or username]
```

---

## DPO template 2: Asking how your request was handled (access request)

An access request under Article 15 can't be answered with "we don't offer that": it asks for information Discord must give you. Use it to make Discord put its reasons in writing.

```
Subject: Access request under Article 15 GDPR – retention of my messages
– [ticket number(s)]

To: dpo@discord.com
Cc: privacy@discord.com

Dear Data Protection Officer,

This is a request for access under Article 15 GDPR.

My account: [username], user ID [user ID], registered email [address].
Earlier tickets: [ticket numbers].

On [date] I asked Discord to erase my messages. [Number] of them were not
erased. For those messages, please tell me:

1. the purposes for which Discord is keeping them (Article 15(1)(a)),
   and the legal basis under Article 6 for each purpose, which Discord
   must in any case tell me (Article 13(1)(c));
2. if the legal basis is legitimate interests, what those interests are
   (Article 13(1)(d)), how Discord balanced them against mine, and
   whether a written assessment exists;
3. how long Discord will keep them, or the criteria used to decide
   (Article 15(1)(d));
4. the recipients or categories of recipients (Article 15(1)(c));
5. what Discord means by a space I "have access to", and how that
   criterion was applied to my request.

Please respond within one month, as Article 12(3) requires.

Kind regards,
[name or username]
```

---

## DPO template 3: Objecting to analytics and activity data

Your data package's `Activity` folders can hold years of analytics events. This asks Discord to explain them and to stop.

```
Subject: Access request and objection under Articles 15 and 21 GDPR –
analytics data

To: dpo@discord.com
Cc: privacy@discord.com

Dear Data Protection Officer,

My account: [username], user ID [user ID], registered email [address].

1. Access (Article 15): for the analytics and activity data linked to my
   account, including the data in the Activity folder of my data
   package, please tell me the purposes and legal basis, the recipients,
   and the retention period or the criteria used to decide it.

2. Objection and erasure (Articles 21(1) and 17(1)(c)): to the extent
   that you process this data on the basis of legitimate interests, I
   object to that processing, on grounds relating to my particular
   situation: [in a sentence or two, in your own words, why you object].
   I ask for its erasure. If you do not act on this, please give me your
   reasons and tell me that I can complain to a supervisory authority
   and seek a judicial remedy, as Article 12(4) requires, and say what
   compelling legitimate grounds, legal claims or Article 17(3)
   exception you rely on.

Please respond within one month, as Article 12(3) requires.

Kind regards,
[name or username]
```

---

## Access request: everything Discord holds about you (general DSAR)

The data package is Discord's own export, and it isn't the same as your full right of access. It mostly covers what you created. Your right under Article 15 covers **all** personal data Discord holds about you, plus information about how it's used. Discord's own [data package article](https://support.discord.com/hc/en-us/articles/360004957991) says the package leaves out support and Trust & Safety correspondence, and messages you've deleted, even though its [retention article](https://support.discord.com/hc/en-us/articles/5431812448791) says deleted public posts may be kept for up to two years. Your right also covers other things the package may leave out, such as security and login logs, and anything Discord has inferred about you or received from elsewhere.

Use this when you want the full picture. Keep it to **your own** data. Asking about Discord's systems in general is easy to brush aside, while asking what it does with *your* data isn't. A very broad request can take Discord longer, and it may extend the deadline by up to two months for complex requests, but only if it tells you so within the first month.

```
Subject: Access request under Article 15 GDPR – [username]

To: privacy@discord.com
Cc: dpo@discord.com

Dear Discord Netherlands BV,

I am making a request for access under Article 15 of the General Data
Protection Regulation (GDPR). I live in [country].

My account: [username], user ID [user ID], registered email [this
address].

1. A copy of my personal data (Article 15(3))
Please provide a copy of all personal data you hold about me, in a
commonly used electronic format. I understand that the standard data
package does not include everything, so please make sure the copy also
covers, where you hold them:
  a) records about me held by your support and Trust & Safety teams,
     including reports, warnings, decisions and correspondence;
  b) security, login and device records, including IP addresses and
     device identifiers;
  c) analytics, activity and event data, and any inferences, scores,
     segments or classifications derived from my data;
  d) personal data about me that you received from other sources, such
     as connected accounts, partners or other users' reports;
  e) messages or other content I sent that is no longer visible in the
     app, because I deleted it or because you deleted it after an
     erasure request, but that you still hold in any system (for
     example for safety, model-training or legal reasons). For each
     item, please give the message ID, the channel ID and the date it
     was deleted, and tell me the purpose, legal basis and retention
     period for keeping it. If you hold none, please say so;
  f) any other personal data about me not included in the data package.

2. Information about the processing (Article 15(1) and (2))
For each category of personal data, please tell me:
  a) the purposes of the processing, and the legal basis relied on
     (which you must tell me under Articles 13(1)(c) and 14(1)(c));
  b) the recipients or categories of recipients, including processors
     and any recipients outside the EEA, and the safeguards for those
     transfers (Article 15(2));
  c) the retention period, or the criteria used to determine it;
  d) where data was not collected from me, its source;
  e) whether any automated decision-making, including profiling, is
     applied to me, and if so meaningful information about the logic
     involved and its significance and envisaged consequences.

Please respond within one month, as Article 12(3) requires. This request
is free of charge (Article 12(5)).

Kind regards,
[name or username]
```

UK users: change "GDPR" to "UK GDPR", "the EEA" to "the UK", and "Discord Netherlands BV" to "Discord Inc." (the controller its privacy policy names outside the EEA).

---

## DPO template 4: The deadline has passed

Send this the day after the deadline, in the same thread. It's short on purpose: it records the date, and gives Discord one last, clear chance.

```
Dear Data Protection Officer,

My request of [date] has not been answered, and I have received no
notice of an extension. The one-month period under Article 12(3) ended
on [date].

Unless I receive a full response, I will include this in my complaint to
[your data protection authority].

Kind regards,
[name or username]
```

---

## Complaint template: EU / EEA data protection authority

Most authorities have an online form. Paste the text below into its main box, adjusting it to your case, and attach your evidence. Find your authority in the [EDPB's list of members](https://www.edpb.europa.eu/about-edpb/about-edpb/members_en). You can write in your own language: if the case is cross-border, the authority coordinates with the others.

```
Complaint under Article 77 GDPR

Controller: Discord Netherlands BV (Discord's EEA controller, as named in
its privacy policy)

1. Summary
On [date] I asked Discord to erase my messages under Article 17 GDPR.
[Number] of the [number] messages I asked to be erased have not been
erased. Discord has not explained why it is keeping them: whether it
considers that no Article 17(1) ground applies, or which exception under
Article 17(3) or other justification under Article 21(1) it relies on.
It has not told me of my right to complain. [My escalation to Discord's
Data Protection Officer of [date] also went unanswered.]

2. What happened
[A short timeline: date, what you sent, what Discord replied. Quote
Discord's replies exactly. For example:
- [date]: request for erasure sent to privacy@discord.com (attached)
- [date]: reply: "We don't offer the ability to delete your messages in
  bulk right now"
- [date]: CSV of [number] messages sent
- [date]: confirmation that the IDs were "submitted for deletion",
  excluding spaces I can still access
- [date]: data package shows [number] messages still present
- [date]: request to the Data Protection Officer; no reply by [date]]

3. Why I believe Discord has infringed the GDPR
- Article 12(3): no response [or no complete response] within one month,
  and no notice of an extension.
- Article 12(4): no reasons given for not erasing [number] messages, and
  no information about my right to complain.
- Articles 17 and 12(4): Discord has not explained whether it considers
  the Article 17(1) grounds inapplicable or, if a ground applies, which
  exception under Article 17(3) or justification under Article 21(1) it
  relies on. Instead, it has relied on an unpublished and undefined
  "accessible space" criterion, without explaining how that criterion
  fits the GDPR or why keeping the messages is necessary for the
  purposes concerned.
- Article 12(2) and Recital 59: no practical way to exercise the right.
  Discord offers no deletion option, requires users to build their own
  CSV from a data package that can take weeks to arrive, and tells them
  bulk deletion is "not offered". [Describe your burden: e.g. "It took me
  [number] emails over [number] weeks, and I had to follow a community
  guide to find out how the process works. Deleting the remaining
  [number] messages by hand would take [estimate] hours."]
- Inconsistent justification: Discord says other users rely on these
  messages for context, but lets me delete each of them myself, and has
  already erased messages in bulk from servers other members can still
  read. Context therefore can't explain the refusal.
- EDPB material: the EDPB-commissioned one-stop-shop case digest on
  erasure says controllers must facilitate erasure without cumbersome
  procedures, and the EDPB's Guidelines 03/2022 say the steps to exercise
  rights should be as few as possible.
[- Article 38(4): my email to Discord's Data Protection Officer was
  handled as an ordinary support ticket and closed without a reply. The
  same case digest describes a comparable case (an automated reply
  redirecting rights requests to a contact form, FR:OSS:D:2022:326) as a
  cumbersome procedure.]

4. What I ask the authority to do
- Order Discord to comply with my request (Article 58(2)(c)).
- Consider ordering Discord to bring its handling of erasure requests
  into compliance (Article 58(2)(d)), so that users have an effective
  way to have their messages erased in bulk, whether all of them or all
  of them in a given conversation or server. I am not asking for a
  particular feature, only for the right to work in practice at the
  scale of the data Discord holds.
- Where the authority considers it appropriate, investigate whether this
  is how Discord handles erasure requests generally.

5. Amicable resolution (optional)
[Only if you want your complaint to push for change for everyone. It may
slow down your own result. See the next section before including it.]

6. Evidence attached
- My request of [date] and every reply from Discord, with dates
- Comparison of my data packages of [date] and [date]
- [Screenshots of the ticket marked "solved"]
- [My email to the Data Protection Officer, and the deadline that passed]
```

**Tips:**
- **Keep it factual.** Dates, quotes and numbers carry weight. Words like "malicious" don't.
- **Keep copies** of everything you submit, and the authority's reference number.
- **Expect months.** If Discord sends anything new later, forward it to the authority with your reference number.

---

## Amicable resolution: stating your position

> **This is optional.** Only include it if you want your complaint to push Discord to change how it handles erasure for everyone, so other people don't have to go through this. If your main goal is to get your own messages deleted as quickly as possible, leave it out.

Some authorities try to settle complaints by agreement between you and the company, which is called an "amicable resolution". Often that's the quickest way to get your own messages deleted: Discord agrees to erase them, and the complaint is closed. The catch is that nothing changes for anyone else.

If you turn down a resolution that only deletes your own messages, your complaint may take longer. Declining doesn't oblige the authority to open a wider inquiry, and it can still close the complaint on another lawful basis. That's the trade-off: a faster personal outcome, or a better chance of changing the process. Both are reasonable choices.

**Why it can be worth it:** a complaint that isn't settled with a personal fix keeps the wider problem in front of the authority, and complaints are one of the ways investigations start. If an authority looks into Discord's practices, it has real powers:
- **It can order Discord to change how it handles erasure** (Article 58(2)(d)), for example to provide an effective way for users to have their messages erased at scale. The authority decides how; it doesn't have to be a particular button.
- **It can fine Discord.** For breaches of data subject rights, including the right to erasure and the rules on answering requests, fines can reach €20 million or 4% of worldwide annual turnover, whichever is higher (Article 83(5)).
- **It has happened before.** In 2022 France's CNIL fined Discord €800,000 over its data practices, including how long it kept data.

**Your own effort is evidence too:** see [Your effort is evidence](#your-effort-is-evidence) below.

None of this is guaranteed. The authority decides whether to investigate and what to do. But every complaint that states this position adds to the evidence that the problem is Discord's process, not one person's request.

If you do want your complaint to be about more than your own data, say so at the start:

```
I would like to state my position on amicable resolution for the record.
My complaint concerns not only my own data, but how Discord handles
erasure requests generally: the lack of any effective way to have
messages erased in bulk, the undefined "accessible space" criterion, and the absence of
reasons when requests are refused. A resolution limited to deleting my
own messages would not address these issues, and I would not regard it
as resolving my complaint. I would be open to an amicable resolution that
addressed them: a commitment by Discord to provide an effective way for
users to have all their messages, or all their messages in a given
conversation or server, erased (an option in the app would be one
example), and to publish how it handles erasure requests.
If that is not achievable, I ask the authority, or the lead supervisory
authority, to consider whether these issues warrant an inquiry.
```

You can't force an authority to open an inquiry, and how amicable resolution works varies between countries. (In Ireland, for example, a complaint resolved amicably is treated as withdrawn.) Stating your position helps the authority understand that deleting your messages alone doesn't address your complaint. The authority still decides what to investigate and what to do.

---

## Your effort is evidence

Discord has to *facilitate* your rights (Article 12(2)), and the GDPR expects requests to be easy to make and to act on, including electronically (Recital 59). An EDPB-commissioned case digest says cumbersome procedures fall short of this, and the EDPB's guidelines on deceptive design say the steps needed to exercise a right should be as few as possible. If getting your messages deleted means requesting a data package, waiting weeks, running a script, writing emails that cite law, decoding templates and following a guide like this one, just to *maybe* succeed, that burden is part of the problem. The fact that a community had to write this guide at all says something.

A regulator can only act on what it can see, so record it as you go:
- **How many messages** you'd have to delete by hand: the "still present" figure from [Step 6](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md)
- **How long one deletion takes:** time yourself deleting a few hundred messages in one sitting, and note any slowdowns, errors or rate limits. A short screen recording with personal details hidden is even better
- **The total:** messages × seconds per message, in hours. Present it as a minimum, since real deletion is slower than a timed test
- **Every step you took:** data package request, waiting time, building the CSV, each email and reply, with dates
- **Discord's refusal:** the exact words it used to decline bulk processing
- **What Discord did process:** for example, the messages it removed in bulk from spaces you'd left. That shows a bulk process exists

Put the figures in your complaint under Article 12(2). Specific numbers are much harder to dismiss than "it's a lot of work".

## UK: complaining to Discord first (section 164A)

Since 19 June 2026, UK users can complain to the company under section 164A. The ICO says you can complain to it at any time, but recommends complaining to the company first, and in most cases will ask you to. The company must acknowledge the complaint within 30 days and tell you the outcome without undue delay. Reply in the same thread, or email `privacy@discord.com`:

```
Subject: Data protection complaint under section 164A of the Data
Protection Act 2018 – [ticket number(s)]

Dear Discord,

This is a data protection complaint under section 164A of the Data
Protection Act 2018.

My account: [username], user ID [user ID], registered email [address].

On [date] I asked you to erase my messages under Article 17 UK GDPR.
[Number] of them have not been erased, and you have not given a reason
under Article 12(4) or identified an exception under Article 17(3).
[You did not respond within one month, as Article 12(3) requires.]

Please acknowledge this complaint within 30 days, as section 164A
requires, and tell me the outcome. If it is not resolved, I will
complain to the Information Commissioner's Office.

Kind regards,
[name or username]
```

**Then, if it isn't resolved,** complain to the ICO at [ico.org.uk/make-a-complaint](https://ico.org.uk/make-a-complaint/data-protection-complaints/). The EU complaint template above works as a starting point, with these changes: replace "Complaint under Article 77 GDPR" with "Complaint under section 165 of the Data Protection Act 2018" (Article 77 no longer applies in the UK); change "GDPR" to "UK GDPR" and the controller to "Discord Inc."; remove the amicable-resolution paragraph unless it applies; and add your section 164A complaint and Discord's response (or the lack of one) to the timeline and the evidence.

---

## Template: updating the authority later

If Discord replies late, misses another deadline, or something else changes after you've complained:

```
Subject: [Authority's reference number] – update on my complaint about
Discord Netherlands BV

Dear [authority],

I am writing with an update on my complaint, reference [number].

On [date], [what happened: e.g. "my request to Discord's Data Protection
Officer of [date] reached its one-month deadline without any reply or
notice of extension" / "Discord replied as follows: …"].

The relevant emails are attached. I would be grateful if you could add
them to my complaint.

Kind regards,
[name]
```

One update with everything new is more useful to a case officer than several partial ones.

---

<!-- file: docs/12-banned-accounts.md -->

# 12. Deleted or banned accounts


This page is for you if you can no longer log in to Discord because your account was **deleted**, whether by you or by Discord (for example, for inactivity), or **banned** (Discord calls this "disabled"). You still have rights under the GDPR and UK GDPR. Losing the account ends your use of the service. It doesn't end Discord's obligations about your personal data. This page explains how to get a copy of your data and ask for your ordinary messages to be erased without logging in.

The steps are the same for both. Where something applies only to deleted or only to banned accounts, the page says so.

> **If your account is banned: erasure is not an appeal.**
> Erasing what's left of your messages is a different thing from getting unbanned, and the two can conflict. If you want your account back, appeal first, and think carefully before asking for erasure: Discord could treat an erasure request as closing the account, and you may want your data intact while an appeal is open. If you're unsure, make the **access request** below first. It gets you a copy of your data and commits you to nothing.

> **If you haven't deleted your account yet, don't do it to get rid of your messages.** Deleting an account doesn't delete its messages: Discord says it anonymises them and keeps them. It also makes requests harder. Make your requests, and check the result, while you can still log in ([FAQ](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/08-faq.md)).

## What this covers, and what it doesn't

**It covers your ordinary messages:** everyday conversations in servers, group chats and DMs.

**If you're banned, it doesn't cover whatever Discord says you were banned for.** Discord may be able to keep particular records connected to a ban where they're needed to comply with a legal obligation (Article 17(3)(b)) or to establish, exercise or defend legal claims (Article 17(3)(e)). Records genuinely needed to deal with an actual or reasonably expected appeal may also be kept where there's a legal basis for it. But the mere possibility of an appeal doesn't automatically justify keeping everything connected with a ban. The templates below have an optional line that leaves ban-related content out, so your request is about ordinary messages only.

Many people in ban-appeal communities report bans they believe were automated mistakes. If that's you, you can also ask Discord, as part of the access request, whether the decision was automated (Article 15(1)(h)). That information can help an appeal too. But the appeal itself is a separate process, outside this guide.

## Deleted accounts: can Discord still identify you?

Discord's data package tool only works from a logged-in account, and deleting an account cancels any package request that's still pending. That's a limit of Discord's app, not of the law. Discord's policies can't override the GDPR, and its own [Terms of Service](https://discord.com/terms) say so: under "More important stuff", they say you have "certain rights that, by law, can't be limited by these terms", and that Discord doesn't intend to restrict them.

The legal test is whether Discord can still identify you:
- **If Discord can still link your messages to your old account,** for example because they still exist, shown as "Deleted User", but are tied to the account record, it can identify you. Then it must act on your request. Under Articles 11(2) and 12(2), it can refuse only if it *demonstrates* that it can't identify you, and you can give it extra information so that it can.
- **The "Deleted User" label doesn't settle it either way.** What matters is whether the messages, any identifiers Discord kept, or their context still make you identifiable by means reasonably likely to be used.
- **If Discord has truly anonymised the data,** so it can no longer be linked to you by any reasonably likely means, the GDPR no longer applies to that data. But Discord should then be able to tell you so.

**Make a clear Article 15 access request.** Say that you want a copy of your personal data, and what you need. You don't have to cite Article 15 or use legal wording for a request to count. But making it explicit, and separate from a question about Discord's data package tool, makes it harder to misread as an ordinary support question. The one-month deadline runs from when Discord receives it, and if Discord ignores it or refuses without reasons, you have a clear complaint.

Add this paragraph to the templates below, where they say so:

```
I understand that my account has been deleted. Under Articles 11(2) and
12(2) GDPR, you may refuse to act on this request only if you
demonstrate that you are not in a position to identify me. To help you
identify me, I am writing from the email address registered to the
account and have provided [the account details above / Discord's
emails about the account, attached]. If you need more information,
please tell me what you need.
```

The [case study](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/09-case-study.md) includes an access request for an account Discord deleted for inactivity in 2024, due in November 2026. We'll add the result when it arrives.

## Why your request should be straightforward

Discord's stated practice is to delete messages in spaces you "no longer have access to", and to keep messages in spaces you can still open. A deleted or banned account can't open anything. So by Discord's own criterion, every ordinary message from your account should be processed.

So if you want your ordinary messages erased, Discord's own rule supports your request. If Discord refuses anyway, ask it to explain why, since its usual reason doesn't apply to you. If you'd like to help others know what to expect, you can share your result in an [experience report](https://github.com/Technae/The-Erasure-Codex/issues/new/choose).

## Before you start

- [ ] **If you're banned, decide: appeal or erasure** (see the box above)
- [ ] **Make sure you can use the email address registered to the account.** That's your main proof that the account is yours
- [ ] **Save Discord's emails about the account,** with their dates: the ban notice and any appeal emails, or deletion and inactivity notices
- [ ] **Write down what identifies the account:** username, user ID if you know it, roughly when you created it, and any earlier ticket numbers

## Proving it's your account

**Don't send ID documents by default.** Discord can ask for more information only if it has *reasonable doubts* about who you are (Article 12(6)), and an EDPB-commissioned case digest on erasure says that requiring ID by default isn't acceptable. An ID document also isn't much use here: Discord usually doesn't know your legal name, so a passport shows who you are, not that you own the account.

**Better ways to show the account is yours**, roughly strongest first:
1. **Write from the account's registered email.** That's how Discord itself identifies you: it sends data packages and account notices there.
2. **Attach Discord's own emails to that address,** such as the ban notice, verification emails or deletion notices. Save them as original messages (`.eml`, via "download message" or "show original") so the headers show Discord really sent them.
3. **Give the account details:** username, user ID if you know it, roughly when you created it, and any earlier ticket numbers.
4. **Other details only the owner would know,** if Discord asks for more: for example, the date and amount of a Nitro payment, the last four digits of the card used (never the full number), or accounts you connected, such as Steam.
5. **Offer to confirm a code** that Discord sends to the registered email.

**If Discord still insists on ID:**
- Ask what its specific doubt is, and why the details above don't resolve it.
- If you decide to send a document, send only what's needed. Black out the document number and anything else Discord doesn't need, and write "Copy for Discord data protection request [ticket number], [date]" across it.
- Send it in the ticket thread, not through a third-party link. Ask how long Discord will keep it, and ask for it to be deleted once your identity is confirmed.

## How to use the templates

Choose the words in square brackets that fit, such as **[disabled/deleted]**, and delete the rest. Lines marked **[Banned accounts: …]** or **[Deleted accounts: …]** are only for that case. UK users: change "GDPR" to "UK GDPR" and "Discord Netherlands BV" to "Discord Inc.", and for complaints see the [UK steps](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#uk-complaining-to-discord-first-section-164a) (complaints to the ICO are now under section 165 of the Data Protection Act 2018, not Article 77).

## Step 1: Ask for your data (access request)

You can't use **Settings → Data & Privacy** while banned, or once your account is deleted. Discord's [help page](https://support.discord.com/hc/en-us/articles/360004957991) says that if you've permanently lost access to your account, you can contact `privacy@discord.com`. This template does that formally under Article 15, which gives Discord one month to respond.

```
Subject: Access request under Article 15 GDPR – [banned/deleted]
account – [username]

To: privacy@discord.com
Cc: dpo@discord.com

Dear Discord Netherlands BV,

I am making a request for access under Article 15 of the General Data
Protection Regulation (GDPR). I live in [country].

My Discord account was [disabled/deleted] on [date], so I cannot use
the data request option in the app. I am writing from the email address
registered to the account.

Account details:
  Username: [username]
  User ID: [user ID, if known]
  Registered email: [this address]
  Approximate creation date: [month/year]
  [Ban/deletion] notice received: [date] (attached)

[Deleted accounts: the identification paragraph above.]

Please provide:
1. a copy of all personal data you hold about me, including all messages
   I sent, with each message's ID and the ID of the channel it was sent
   in, in the same format as the standard data package, delivered to
   this email address;
2. the information listed in Article 15(1), including the purposes of
   processing, the recipients, and the retention period or the criteria
   used to determine it;
3. whether you still hold any messages I sent that are no longer
   visible in the app, because I deleted them or because they were
   deleted later, and if so a copy of them, with the purpose, legal
   basis and retention period for keeping them. If you hold none,
   please say so;
4. [Banned accounts, optional: whether the decision to disable my
   account involved automated decision-making, and if so, meaningful
   information about the logic involved (Article 15(1)(h)).]

Please respond within one month, as Article 12(3) requires. If you need
more information to confirm my identity, please tell me what your
reasonable doubt is (Article 12(6)).

Kind regards,
[name or username]
```

**Diary the deadline:** one month from when Discord receives it. If the package arrives, keep it as evidence ([Get your data package](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/02-get-your-data.md)) and use it to build your CSV ([Build the CSV](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md)).

## Step 2: Ask for your ordinary messages to be erased

Once you have your data package, build the CSV as usual ([Build the CSV](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md)). If you're banned and know which channel or messages your ban relates to, leave them out with the script's `--exclude` option. That makes it clear you're not asking for those to be erased.

```
Subject: Erasure request under Article 17 GDPR – [banned/deleted]
account – [username]

To: privacy@discord.com
Cc: dpo@discord.com

Dear Discord Netherlands BV,

I am making a request for erasure under Article 17 GDPR. My account
([username], user ID [user ID], registered email [this address]) was
[disabled/deleted] on [date]. [Banned accounts: I understand this
request concerns erasure of my data, not the reinstatement of my
account.]

[Deleted accounts: the identification paragraph above.]

Please erase the [number] messages listed in the attached CSV file
(channel_id, message_id). I rely on Article 17(1)(a), as these messages
are no longer necessary for the purposes for which they were collected
or processed.

To the extent that you keep these messages on the basis of legitimate
interests, I also object under Article 21(1), on grounds relating to my
particular situation: [in a sentence or two, in your own words, why you
object]. Where that objection applies, I rely on Article 17(1)(c).

[Banned accounts: This request covers my ordinary messages only. It
does not cover any content you rely on in connection with the decision
to disable my account, which you may need to keep under Article 17(3).
I have left out the channels concerned. Please do not delete my
account as part of handling this request.]

Your replies to other users say that you process deletion for spaces a
user no longer has access to. Because my account is [disabled/deleted],
I no longer have access to any space on Discord, so on your own
criterion all of these messages should be processed.

If you do not take action on any part of this request, please give me
your reasons and tell me that I can complain to a supervisory authority
and seek a judicial remedy, as Article 12(4) requires. To help me
understand your decision, please also identify the messages you are
keeping, the purposes and legal basis for keeping them, and any
exception under Article 17(3) or justification under Article 21(1)
(including legal claims) you rely on.

Please respond within one month, as Article 12(3) requires.

Kind regards,
[name or username]
```

**Checking the result:** without account access, the only way to check is to make another access request later and compare the two packages ([Check the result](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md)). Some users have reported that messages from banned accounts disappear on their own over time, so compare carefully and note the dates.

## Step 3: If Discord doesn't answer

Send a short deadline notice in the same thread the day after the month runs out ([DPO template 4](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#dpo-template-4-the-deadline-has-passed)). Then complain to your data protection authority ([Deadlines and complaints](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/07-deadlines-and-complaints.md)). UK users: the ICO recommends complaining to Discord first under section 164A, and in most cases will ask you to ([template](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#uk-complaining-to-discord-first-section-164a)).

### Complaint template: access request ignored

Paste this into your authority's complaint form and adjust it to your case.

```
Complaint under Article 77 GDPR

Controller: Discord Netherlands BV

1. Summary
My Discord account was [disabled/deleted] on [date]. On [date] I made a
request for access under Article 15 GDPR from the email address
registered to the account, because I cannot use the in-app data request
without access to my account. Discord has not provided my data [and has
not replied / has replied only with a template], and gave no notice of
an extension within one month.

2. What happened
- [date]: account [disabled/deleted] ([ban/deletion] notice attached)
- [date]: access request sent to privacy@discord.com, cc dpo@discord.com
  (attached)
- [date]: [any reply, quoted exactly, or "no reply"]
- [date]: one-month deadline passed
- [date]: deadline notice sent (attached)

3. Why I believe Discord has infringed the GDPR
- Article 15: I have not received a copy of my personal data or the
  information I am entitled to.
- Article 12(3): no response within one month, and no notice of an
  extension.
- Article 12(2): users who can no longer log in have no way to obtain
  their data except by writing to Discord, and that route has not
  worked.
[- Deleted accounts: Articles 11(2) and 12(2): Discord has not
  demonstrated that it cannot identify me, although I wrote from the
  registered email address and provided the account details.]
[- Article 12(6): Discord asked for identity documents without stating
  any reasonable doubt, although I wrote from the registered email
  address.]

4. What I ask the authority to do
- Order Discord to comply with my access request (Article 58(2)(c)).
- Consider whether Discord's handling of data requests from users who
  can no longer log in complies with the GDPR more generally.

5. Evidence attached
- [Ban/deletion] notice
- My access request and any replies, with dates
- Deadline notice
```

### Complaint: erasure refused

Use the general [EU complaint template](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#complaint-template-eu--eea-data-protection-authority), and add these points to section 3:

```
- My account is [disabled/deleted], so I cannot access any space on
  Discord. Discord's stated practice is to process deletion for spaces a
  user no longer has access to, yet it has not erased [number] of my
  ordinary messages, and has not identified any exception under Article
  17(3) for them.
[- Banned accounts: My request expressly excluded any content connected
  with the decision to disable my account. The messages concerned are
  ordinary messages.]
```

## Questions

**I deleted my account myself. Does all of this apply to me?** Yes. Use the same templates, choosing "deleted", and add the identification paragraph. The ban-related lines don't apply to you.

**Will this get me unbanned?** No. It's about your data, not your account. See the box at the top.

**Can't I just delete my banned account instead?** You can't delete a banned account from the app, and this guide doesn't recommend deleting accounts anyway. A ban already has the same effect from the outside: you can't access anything. The difference is that Discord may keep content related to the ban.

**Discord refused my access request, citing Article 15(4).** Article 15(4) says that getting a *copy* of your data mustn't adversely affect the rights and freedoms of others. It lets Discord hold back or redact parts that would harm someone else, such as another user's personal data or a report someone made about you. It isn't a reason to refuse the whole request. You're still entitled to the rest of your data, and to the Article 15(1) information (purposes, recipients, retention and so on), which Article 15(4) doesn't cover. If Discord relies on it, ask which data it's holding back and why it can't simply redact it. A bare "this would affect others" isn't the reason Article 12(4) requires. UK users: UK law also has specific exemptions, for example where disclosure would prejudice preventing or detecting crime (Schedule 2 of the Data Protection Act 2018). Even then, Discord must tell you it has refused and how to complain.

**Do I need the full access request, or just the data package?** For erasure, the data package is enough, because it lists your message IDs. If you also want to know what else Discord holds about you, such as safety records, logs or anything inferred about you, use the [general access request](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/11-templates.md#access-request-everything-discord-holds-about-you-general-dsar).

**What if I no longer have access to the registered email?** It's harder, but still possible. Give Discord as much as you can to show the account is yours: earlier emails from Discord, the ban or deletion notice, payment receipts for Nitro, or the account's creation date. Expect Discord to ask for more.

**Is this worth doing if I only have a few messages?** Yes, if you want them gone. The right doesn't depend on how many messages there are. Make the request because you want your data erased, not to test Discord (see the [FAQ](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/08-faq.md)).

---

<!-- file: scripts/README.md -->

# erasure_helper.py

A small, dependency-free Python 3 script for working with a Discord data package when making an erasure request.

- Reads the package **directly from the .zip** (or an extracted folder) and never changes it: it refuses to write output over the package or into an extracted package folder
- Stops with a clear error if a file or message record isn't in a format it recognises, rather than reporting a smaller count (`--allow-incomplete` overrides this for unreadable records, and says so)
- Writes output to a temporary file and only puts it in place once the whole run has succeeded, so a failed run never leaves a partial CSV or damages an earlier one
- Works with both the current JSON layout and older CSV layouts
- Doesn't connect to the internet, and never needs your token or password

| Command | What it does |
|---|---|
| `python3 erasure_helper.py summary package.zip` | Count your messages by channel type |
| `python3 erasure_helper.py csv package.zip -o messages_to_delete.csv` | Write the `channel_id,message_id` CSV Discord asks for |
| `python3 erasure_helper.py compare old.zip new.zip` | Show how many messages are no longer in the newer export |

Options for `summary`: `--allow-incomplete`.
Options for `csv`: `--exclude FILE`, `--only FILE` (channel IDs, one per line), `--split N` (messages per file, plus the header), `--no-header`, `--force`, `--allow-incomplete`.
Options for `compare`: `--report FILE` (per-channel counts, includes channel names, keep private), `--remaining FILE` (IDs in both exports, ready to resend), `--force`, `--allow-incomplete`.

The comparison counts `(channel_id, message_id)` pairs. It shows what Discord's export no longer includes, not whether every copy has been erased.

**Tests:** `python3 -m unittest test_erasure_helper -v` (run from this folder) checks the script against small mock packages, including malformed ones. Please run it before submitting changes.

**For maintainers:** `python3 scripts/build_full.py` (run from the repository root) rebuilds [`CODEX-FULL.md`](https://github.com/Technae/The-Erasure-Codex/blob/main/CODEX-FULL.md), the whole guide in one file, from the individual pages. Run it after changing any page.

See [Step 3](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/03-build-the-csv.md) and [Step 6](https://github.com/Technae/The-Erasure-Codex/blob/main/docs/06-check-the-result.md) for a walkthrough. Licence: MIT.
