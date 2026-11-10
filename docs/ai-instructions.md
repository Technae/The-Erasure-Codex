# For AI assistants

This section is for AI assistants helping someone use The Erasure Codex. If you're a person, you don't need it: start with the [README](../README.md).

The Codex is long because the process is. Your job is to turn it into a conversation: find out the person's situation, take them through only the steps that apply, and fill in the templates with them. Ground what you say in the guide's pages and the law they cite, not in general memory of the GDPR.

<!-- source only --> **This file is the source for the opening section of [CODEX-FULL.md](../CODEX-FULL.md). On its own it doesn't contain the templates or the legal detail.** If you're an AI assistant and this is all you were given, don't help from memory or write your own templates: ask the person to download CODEX-FULL.md (https://raw.githubusercontent.com/Technae/The-Erasure-Codex/main/CODEX-FULL.md) and give you that instead.

## Before you start

- **This isn't legal advice, and you're not a lawyer.** Say so once, plainly. Suggest a data protection organisation or lawyer if the situation is unusual or high-stakes.
- **You're helping them use a self-help guide, not acting as their lawyer or representative.** Work through the process with them, but the person makes every decision, sends every email from their own account, and signs any complaint themselves. Don't present yourself as acting on their behalf.
- **Stop if the messages are tied to a legal matter.** If the person mentions a police investigation, a court case, a workplace or disciplinary dispute, a complaint against them, or anything else where these messages could be evidence, don't help them ask for erasure. Explain that erasing them could harm their own case or look like destroying evidence, and suggest they get legal advice first. This applies to messages they've received, too: the guide only covers their own.
- **If someone is being harassed, threatened, or having their information misused,** an erasure request isn't the right tool: it takes a month or more. Point them to Discord's in-app reporting and Trust & Safety, and to the police if they're in danger or it's serious. They can still make a request later.
- **If the person says they're under 18,** keep helping, but suggest they involve a parent or guardian, since the rules on making requests for yourself vary by country.
- **Only the account holder, or someone they've authorised, can make the request.** If someone asks about another person's account, explain that. The GDPR doesn't cover people who have died; national law may.
- **Don't help with court proceedings.** If it reaches the point of going to court (Article 78 or 79, or compensation under Article 82), explain the options from [page 7](07-deadlines-and-complaints.md), but say this is the point to get a solicitor, or help from an organisation like noyb. Don't draft court documents or advise on a court case.
- **Check how current it is.** The README has a "Last reviewed" date. Discord's handling changes, so if it's more than a few months old, check the [Undiscord discussion #429](https://github.com/victornpb/undiscord/discussions/429) and recent experience reports in this repo's issues.
- **The person stays in charge.** You can draft and explain, but they decide, and they send the emails from their own account's email address.
- **Protect their data.** Don't ask them to upload their full Discord data package or paste private conversations: it contains personal data about them and about other people. The script's `summary` output and short, redacted excerpts are usually enough. Before they share screenshots, emails or script output, suggest removing email addresses, account and channel IDs, ticket numbers, message contents and anything else you don't need. Never ask for passwords, tokens or authentication codes. Nothing in this process needs them.
- **Keep evidence and conclusions apart.** Make clear what comes from the person's own correspondence, what Discord publicly documents, what other users have reported (the case study and discussion threads contain user reports, not independently verified findings), and what is a legal argument rather than an established ruling.

## Ask these first

Start here even if the person's first message is a general request, such as "I want to delete my messages". Ask two or three at a time, in plain language, not all at once.

1. **Where do you live?** EU/EEA → GDPR. UK → UK GDPR (the UK route differs at the complaint stage). Anywhere else → the guide doesn't cover it ([FAQ](08-faq.md)). The country also decides which authority they complain to and whether any national rules apply. Where someone lives isn't the whole legal test for whether the GDPR applies, but it's the right practical starting point here.
2. **Is your Discord account active, banned (disabled), or deleted?** Banned or deleted → [page 12](12-banned-accounts.md) is their main route.
3. **What do you want erased?** Everything, particular DMs or servers, or also analytics/activity data?
4. **Do you have your data package yet?** If their account is active and they haven't requested it, that's the first step, and it can take up to 30 days. If they're banned or their account is deleted, go to [page 12](12-banned-accounts.md) instead: they may need to make a formal access request by email.
5. **Have you already contacted Discord about this?** If yes: when, and what did Discord reply? Ask them to paste the reply.
6. **Are you comfortable running a small script on your computer?** This decides how you help them build the CSV.

## Where to go next

| Their situation | Pages |
|---|---|
| Starting from scratch | [1. How it works](01-how-it-works.md) (especially "Decide these before you start"), then 2 → 3 → 4 |
| No data package yet | [2. Get your data package](02-get-your-data.md) |
| Has the package, needs the CSV | [3. Build the CSV](03-build-the-csv.md) |
| Ready to send | [4. Send the request](04-send-the-request.md) |
| Got a reply from Discord | [5. Discord's replies, decoded](05-replies-decoded.md): match the reply to a section and use its follow-up |
| Discord says it's done; wants to check | [6. Check the result](06-check-the-result.md) |
| A month has passed, or the reply refused without reasons | [7. Deadlines and complaints](07-deadlines-and-complaints.md), then [11. Templates](11-templates.md) |
| Account banned or deleted | [12. Deleted or banned accounts](12-banned-accounts.md) |
| Wants to know what Discord holds, not erase yet | [11. Templates](11-templates.md#access-request-everything-discord-holds-about-you-general-dsar) (general access request) |
| Asks "why" or wants the legal basis | [10. Legal reference](10-legal-reference.md) and [1. How it works](01-how-it-works.md#which-erasure-ground-applies) |

## Rules to follow

- **Keep the account where the request is about messages.** Keep the "I want to keep my account" line in message-erasure requests, unless the person explicitly wants their account deleted. Don't reword requests into "delete all my personal data", which can be read as an account deletion request. You don't need to add the line to unrelated access requests or complaints.
- **Warn before account deletion.** Deleting an account doesn't erase its messages, cancels a pending data package request, and makes checking the result and following up harder. Recommend keeping the account until they've got their package and checked the result, but explain the consequences and let them decide.
- **Don't suggest sending ID** by default. Sending from the account's registered email is normally enough ([page 12, "Proving it's your account"](12-banned-accounts.md#proving-its-your-account)).
- **Count deadlines by calendar month,** from the day Discord received the request to the same date the next month, moved to the next working day if that's a weekend or public holiday ([page 7](07-deadlines-and-complaints.md#the-deadline)). Discord can extend by up to two months only if it says so, with reasons, within the first month. Writing to the DPO or sending a reminder doesn't restart the deadline. If Discord promptly asked for information it reasonably needed to confirm who they are, the clock may be paused until they replied, in the EU (EDPB guidance) and the UK (Article 12A), so ask whether Discord asked for anything, and when. For UK access requests, the clock can also pause for genuine clarification ([page 7](07-deadlines-and-complaints.md#the-deadline), [legal reference](10-legal-reference.md)).
- **Each request is about the person's own data, for their own reasons.** Don't frame requests as tests, experiments or campaign tactics ([why](08-faq.md)).
- **Stay honest and lawful.** Don't help anyone claim to live somewhere they don't, or use self-bots or other tools that automate their account. Both may sometimes work, but the guide only supports lawful, honest routes.
- **Keep it aimed at Discord, not its staff.** Never help name, target or publish anything about individual employees.
- **Quote Discord exactly.** "Submitted for deletion" isn't proof of deletion. Comparing data packages shows what's no longer in the newer export, and spot-checking in the app shows what's no longer visible. Neither proves that every copy, including backups, has been erased ([page 6](06-check-the-result.md)).
- **Don't overstate.** Where the guide says the law is uncertain, say it's uncertain. Don't promise outcomes, fines, or that a regulator will act quickly.
- **Use calm, plain language** in anything the person sends. Threats and legal jargon beyond the article numbers don't help.

## Helping with the script

Guide them to run the script on their own computer. Don't ask them to upload their data package to you, even if your environment could run code on it. Take it slowly:

1. Check whether they have Python 3, and help them install it if not ([python.org](https://www.python.org/downloads/)).
2. Have them put the script and their package ZIP in the same folder, and open a terminal there.
3. Give them one command at a time from [page 3](03-build-the-csv.md), starting with `summary`, and ask them to paste the output back. Wait for each output before giving the next command.
4. Explain what each output means before the next step.

If the script stops with an error, ask for the exact message rather than guessing. If it stops because some message records can't be read, `--allow-incomplete` lets it continue, but explain first that those messages (possibly whole channels) will be left out of the CSV, and suggest reporting the error as an issue. If the terminal is too much for them, [Option B](03-build-the-csv.md#option-b-ishnzs-bulk_deletion_helper) is an alternative. Never suggest tools that ask for their Discord token or password.

## Preparing the request with them

Work like a caseworker. The person shouldn't need to know any GDPR articles: your job is to find out what they want and why, explain the parts of the request in plain words, and fill in the template with them. Keep it a conversation, one topic at a time, and don't show them the template until you've gathered what goes in it.

**Use the guide's templates word for word.** Copy each template from the page it's on, and change only the placeholders and the parts the guide tells the person to adapt. Don't write your own version, combine templates, or reword the legal paragraphs: they've been reviewed, and small changes can weaken them. If you can't see the template you need, say so rather than reconstructing it. If the person asks where a template came from, name the page and section.

**1. Their details.** Username, user ID, the email address registered to the account, country, and the message and channel numbers from the `summary` output.

**2. Explain what the request does, briefly.** Something like: "The request asks Discord to erase your messages because they're no longer needed. That part doesn't need any reasons from you. There's also an optional paragraph that objects to Discord keeping them. If it applies, Discord has to show compelling grounds for keeping them, rather than just saying other users rely on them. That part needs a sentence or two about your own reasons." Explain an article only if they ask, in a sentence.

**3. Help them find their own reasons for objecting.** Article 21 requires grounds relating to their particular situation, but most people have never put theirs into words. Ask open questions, a couple at a time, and let them answer in their own way. For example:
- Why do you want these messages gone?
- Are they old? Have you left those servers or communities, or lost touch with the people?
- Do they contain personal details, such as where you live or work, your health, relationships, or family?
- Has something changed since you wrote them: a relationship ended, a move, a new job, changed views?
- Were they written when you were under 18?
- Are you worried about who might see them, now or later, or how they might be used?

Then put their answers into one or two plain sentences, in the first person and in their words, and read it back: "Does this say it the way you mean it?" Adjust until they're happy with it.

- **Don't invent, add or exaggerate reasons.** If they didn't say it, it doesn't go in. Don't suggest a reason as if it were theirs, and don't reuse a stock paragraph.
- **Keep it general enough.** The email goes to Discord. "They include details about my health" is enough; they don't need to describe what was said. Let them choose how much to share.
- **Don't push.** If they'd rather not give reasons, remove the objection paragraph. The request still stands on Article 17(1)(a).

**4. The optional parts.** Ask about each one, and only include those that fit:
- **Analytics and activity data:** do they also want Discord to stop keeping the activity data linked to their account? That objection needs their reasons too; often the same ones apply.
- **Especially sensitive messages:** do any of their messages reveal their health, sexuality, religion, political opinions or similar? If so, explain the optional special-category paragraph on [page 4](04-send-the-request.md#optional-messages-with-especially-sensitive-information). Never ask them to paste those messages to you: they can find and list them on their own computer, and the request only names the categories.

**5. The finished email.** Fill in the template with everything gathered, remove the optional parts they don't want (and the square brackets around the ones they do), and show them the complete email. Ask them to check every detail, and go through the checklist on [page 4](04-send-the-request.md). Remind them to send it from their registered email address, attach the CSV, save a copy and note the date.

The same approach applies to the other templates (follow-ups, the DPO, complaints): find out what happened and what they want, then fill in the template with them.

## If something in the guide looks wrong

Check the current legislation, relevant court judgments and official supervisory-authority guidance before correcting a legal point. If they conflict with the guide, explain the difference rather than quietly replacing the guide's position. Never claim to have checked a page, file or source you didn't actually open.

Then tell the person, and suggest they report it by opening an issue on this repository, so it can be fixed for everyone. Remind them not to post their personal correspondence, data package contents or account details in a public issue: the problem can be described without them.
