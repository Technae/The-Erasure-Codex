# 4. Send the request

[← Build the CSV](03-build-the-csv.md) · [Contents](../README.md) · [Next: Discord's replies, decoded →](05-replies-decoded.md)

## Where to send it

- **Email:** `privacy@discord.com`, with `dpo@discord.com` (Discord's Data Protection Officer) in copy.
- **Send it from the email address registered to your Discord account.** Discord uses that to confirm the request is yours.
- **Address it to the right company.** Discord's current privacy policy names **Discord Netherlands BV** as the data controller for users in the EEA, and **Discord Inc.** for everyone else, including users in the UK. It names VeraSafe as its UK representative. Check the current policy at [discord.com/privacy](https://discord.com/privacy) if you're unsure.

**By post:** Discord's [Information About Local Privacy Laws](https://discord.com/terms/local-laws) page also gives postal addresses (Discord Netherlands BV in Schiphol for the EEA, Discord Inc. in San Francisco for everyone else). Post is slower, but a tracked or registered letter gives you proof of when it arrived. That can help if your emails are going unanswered, or you can't send from your account's address.

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

The UK version follows the same structure, but cites the **UK GDPR**, says you're in the UK, and uses the UK complaint routes that amended Article 12(4) requires (a complaint to Discord under section 164A and to the Information Commissioner).

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

[← Build the CSV](03-build-the-csv.md) · [Contents](../README.md) · [Next: Discord's replies, decoded →](05-replies-decoded.md)
