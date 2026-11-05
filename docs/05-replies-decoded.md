# 5. Discord's replies, decoded

[← Send the request](04-send-the-request.md) · [Contents](../README.md) · [Next: Check the result →](06-check-the-result.md)

Discord's privacy team mostly replies with templates. Recognising them saves you a lot of frustration. **A template isn't necessarily a complete or properly reasoned answer**, though it may still be a refusal: look at what it actually says. Does it explain what Discord won't erase, why it's keeping it, and how you can challenge the decision? Each section below quotes the template as users have received it in 2026, explains what it means, and gives a reply you can adapt.

Always reply **in the same email thread**, keeping the quoted text and the `[XXXXXX-XXXXX]` tag.

**UK users:** these templates use the EU wording for Article 12(4). Wherever a template says *"tell me that I can complain to a supervisory authority and seek a judicial remedy, as Article 12(4) requires"*, write instead:

```
tell me how I can complain (to you under section 164A of the Data
Protection Act 2018, and to the Information Commissioner) and seek a
judicial remedy, as Article 12(4) UK GDPR requires
```

Since 19 June 2026, UK Article 12(4) requires the company to mention both of those complaint routes.

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

**What it means:** messages in servers and group chats you've left will probably be deleted. Messages anywhere you can still open, including DMs, probably won't. "Submitted" isn't "deleted", so check ([Step 6](06-check-the-result.md)).

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

**Reply:** send one final, short message, optionally escalate to the Data Protection Officer ([DPO template 1](11-templates.md#dpo-template-1-escalating-an-erasure-request)), then move on to [Step 7](07-deadlines-and-complaints.md). Escalating doesn't restart the deadline on your original request.

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

If a month passes with no reply and no notice of an extension, Discord has missed the deadline. See [Step 7](07-deadlines-and-complaints.md).

## General tips

- **Answer what they said, briefly.** Long replies get templated answers too.
- **Repeat the key question every time:** which exception do you rely on, and why does it apply to these messages? A refusal without real reasons (Article 12(4)) is the strongest thing you can show a regulator.
- **Save every reply,** with its date. Use your email client's "download message" or "show original" option to keep a full copy.
- **Stay calm.** Your messages may end up in front of a regulator, so write as if they'll read them.

[← Send the request](04-send-the-request.md) · [Contents](../README.md) · [Next: Check the result →](06-check-the-result.md)
