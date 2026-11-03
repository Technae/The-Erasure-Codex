# 4. Send the request

[← Build the CSV](03-build-the-csv.md) · [Contents](../README.md) · [Next: Discord's replies, decoded →](05-replies-decoded.md)

## Where to send it

- **Email:** `privacy@discord.com`, with `dpo@discord.com` (Discord's Data Protection Officer) in copy.
- **Send it from the email address registered to your Discord account.** Discord uses that to confirm the request is yours.
- **Address it to the right company.** Discord's privacy policy names **Discord Netherlands BV** as the data controller for users in the EEA, and its policies have also named it for the UK. Check the current policy at [discord.com/privacy](https://discord.com/privacy) if you're unsure.

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
Article 17(3). I am relying on Article 17(1)(a) and, as I object to the
continued processing of these messages under Article 21(1), on
Article 17(1)(c).

If you do not erase any of these messages, please tell me, as Article
12(4) requires, which messages you are keeping, the legal basis on which
you keep them, which exception under Article 17(3) or which compelling
legitimate grounds under Article 21(1) you rely on for them, and that I
can complain to a supervisory authority and seek a judicial remedy.

[Optional: I also object under Article 21(1) to the processing of the
analytics and other activity data linked to my account, including the
data in the Activity folder of my data package, and ask for its erasure
under Article 17(1)(c).]

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
Article 17(3). I am relying on Article 17(1)(a) and, as I object to the
continued processing of these messages under Article 21(1), on
Article 17(1)(c).

If you do not erase any of these messages, please tell me, as Article
12(4) requires, which messages you are keeping, the legal basis on which
you keep them, which exception under Article 17(3) or which compelling
legitimate grounds under Article 21(1) you rely on for them, and that I
can complain to the Information Commissioner's Office.

Please respond within one month of receiving this request, as
Article 12(3) requires, and confirm in writing which messages have been
erased. Please do not close this request until you have answered it.

Kind regards,
[name or username]
```

## Before you press send

- [ ] Sent **from your account's email address**
- [ ] The CSV is attached, or the link works in a private browser window
- [ ] The numbers in the email match the CSV (the `summary` command gives you both)
- [ ] You've saved a copy of the email, the CSV, and its hash (`sha256sum messages_to_delete.csv`)
- [ ] You've written down today's date. **The one-month deadline starts when Discord receives your request.**

## Tips

- **Write in plain, calm language.** You don't need legal jargon beyond the article numbers, and threats don't help. A clear, polite request makes any later complaint much stronger.
- **Don't send ID documents** unless Discord gives a real reason to doubt who you are. Sending from your registered email is normally enough.
- **One request, one thread.** If you want to add something later, reply in the same thread rather than starting a new ticket, so your deadline and history stay together.

[← Build the CSV](03-build-the-csv.md) · [Contents](../README.md) · [Next: Discord's replies, decoded →](05-replies-decoded.md)
