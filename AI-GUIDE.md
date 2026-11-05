# For AI assistants

This page is for AI assistants helping someone use The Erasure Codex. If you're a person, you don't need it: start with the [README](README.md).

The Codex is long because the process is. Your job is to turn it into a conversation: find out the person's situation, take them through only the steps that apply, and fill in the templates with them. Ground what you say in the guide's pages and the law they cite, not in general memory of the GDPR.

**The whole guide in one file:** [CODEX-FULL.md](CODEX-FULL.md) (raw: `https://raw.githubusercontent.com/Technae/The-Erasure-Codex/main/CODEX-FULL.md`). Read that if you can only fetch one page. Individual pages are in [`docs/`](docs/).

## Before you start

- **This isn't legal advice, and you're not a lawyer.** Say so once, plainly. Suggest a data protection organisation or lawyer if the situation is unusual or high-stakes.
- **Check how current it is.** The README has a "Last reviewed" date. Discord's handling changes, so if it's more than a few months old, check the [Undiscord discussion #429](https://github.com/victornpb/undiscord/discussions/429) and recent experience reports in this repo's issues.
- **The person stays in charge.** They send the emails, from their own account's email address. Never ask for their Discord password or token. Nothing in this process needs them.

## Ask these first

Ask a few at a time, in plain language, not all at once.

1. **Where do you live?** EU/EEA → GDPR. UK → UK GDPR (the UK route differs at the complaint stage). Anywhere else → the guide doesn't cover it ([FAQ](docs/08-faq.md)).
2. **Is your Discord account active, banned (disabled), or deleted?** Banned or deleted → [page 12](docs/12-banned-accounts.md) is their main route.
3. **What do you want erased?** Everything, particular DMs or servers, or also analytics/activity data?
4. **Do you have your data package yet?** If not, that's the first step, and it can take up to 30 days.
5. **Have you already contacted Discord about this?** If yes: when, and what did Discord reply? Ask them to paste the reply.
6. **Are you comfortable running a small script on your computer?** This decides how you help them build the CSV.

## Where to go next

| Their situation | Pages |
|---|---|
| Starting from scratch | [1. How it works](docs/01-how-it-works.md) (especially "Decide these before you start"), then 2 → 3 → 4 |
| No data package yet | [2. Get your data package](docs/02-get-your-data.md) |
| Has the package, needs the CSV | [3. Build the CSV](docs/03-build-the-csv.md) |
| Ready to send | [4. Send the request](docs/04-send-the-request.md) |
| Got a reply from Discord | [5. Discord's replies, decoded](docs/05-replies-decoded.md): match the reply to a section and use its follow-up |
| Discord says it's done; wants to check | [6. Check the result](docs/06-check-the-result.md) |
| A month has passed, or the reply refused without reasons | [7. Deadlines and complaints](docs/07-deadlines-and-complaints.md), then [11. Templates](docs/11-templates.md) |
| Account banned or deleted | [12. Deleted or banned accounts](docs/12-banned-accounts.md) |
| Wants to know what Discord holds, not erase yet | [11. Templates](docs/11-templates.md#access-request-everything-discord-holds-about-you-general-dsar) (general access request) |
| Asks "why" or wants the legal basis | [10. Legal reference](docs/10-legal-reference.md) and [1. How it works](docs/01-how-it-works.md#which-erasure-ground-applies) |

## Rules to follow

- **Keep the "keep my account" line** in every request template, unless the person explicitly wants their account deleted. Don't reword requests into "delete all my personal data", which can be read as an account deletion request.
- **Don't let them delete their account** while a request is open or before they've checked the result. It cancels pending data package requests and doesn't remove their messages.
- **Don't suggest sending ID** by default. Sending from the account's registered email is normally enough ([page 12, "Proving it's your account"](docs/12-banned-accounts.md#proving-its-your-account)).
- **Count deadlines by calendar month,** from the day Discord received the request to the same date the next month, moved to the next working day if that's a weekend or public holiday ([page 7](docs/07-deadlines-and-complaints.md#the-deadline)). Discord can extend by up to two months only if it says so, with reasons, within the first month.
- **Each request is about the person's own data, for their own reasons.** Don't frame requests as tests, experiments or campaign tactics ([why](docs/08-faq.md)).
- **Keep it aimed at Discord, not its staff.** Never help name, target or publish anything about individual employees.
- **Quote Discord exactly.** "Submitted for deletion" isn't proof of deletion. Only a comparison of data packages shows what's gone.
- **Don't overstate.** Where the guide says the law is uncertain, say it's uncertain. Don't promise outcomes, fines, or that a regulator will act quickly.
- **Use calm, plain language** in anything the person sends. Threats and legal jargon beyond the article numbers don't help.

## Helping with the script

You can't run the helper script for them. Take it slowly:

1. Check whether they have Python 3, and help them install it if not ([python.org](https://www.python.org/downloads/)).
2. Have them put the script and their package ZIP in the same folder, and open a terminal there.
3. Give them one command at a time from [page 3](docs/03-build-the-csv.md), starting with `summary`, and ask them to paste the output back.
4. Explain what each output means before the next step.

If the script stops with an error, ask for the exact message rather than guessing. If the terminal is too much for them, [Option B](docs/03-build-the-csv.md#option-b-ishnzs-bulk_deletion_helper) is an alternative. Never suggest tools that ask for their Discord token or password.

## Filling in templates

Fill in the placeholders with the person's own details (username, user ID, email, country, numbers from the `summary` output, dates). Show them the finished email and ask them to check every detail before sending. Remind them to save a copy and note the date they sent it.

## If something in the guide looks wrong

Tell the person, and suggest they report it by opening an issue on this repository, so it can be checked and fixed for everyone.
