# 11. Templates: Discord's DPO and data protection authorities

[← Legal reference](10-legal-reference.md) · [Contents](../README.md)

This page collects templates for the later stages: writing to **Discord's Data Protection Officer (DPO)**, and **complaining to a data protection authority**. For the first request, see [Step 4](04-send-the-request.md). For replies to Discord's support templates, see [Step 5](05-replies-decoded.md).

Fill in the parts in square brackets, and delete anything that doesn't apply to you.

---

## Why write to the DPO even if you don't expect an answer

Discord has a Data Protection Officer, and the GDPR gives you the right to contact them about your rights (Article 38(4)). In our experience, mail to `dpo@discord.com` ends up in Discord's ordinary support queue. The case study's email to the DPO got a support template and was marked "solved" the next day, with no reply from the DPO. Users in Undiscord #429 report the same.

**Write anyway.** A formal request to the DPO puts it on record that you went to the person responsible for data protection, asked for an answer under the GDPR, and gave Discord the full statutory time to reply. If the one-month deadline passes with no answer and no notice of extension, **that silence is itself an infringement by Discord** of Article 12(3), and if Discord refuses without giving reasons, of Article 12(4). Strictly speaking, the duty to answer belongs to Discord as the controller rather than to the DPO personally, but an unanswered request to the DPO is clear evidence of it. It's also some of the easiest evidence for an authority to act on, because it doesn't depend on any argument about what Discord may keep: either Discord answered in time, or it didn't.

**How to send it:**
- **To:** `dpo@discord.com`, **Cc:** `privacy@discord.com`
- **From** your account's registered email address
- **Mention your earlier ticket numbers,** so the DPO's office can't treat it as a new, unrelated query
- **One subject per email,** with the articles in the subject line. Several separate requests are harder to answer with a single template
- **Diary the deadline:** one month from the day you send it

If it gets a support template and a "solved" status, reply in the same thread (see [Step 5](05-replies-decoded.md)). That keeps the request open, and the deadline running.

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

Please either:
1. erase the remaining messages, which are listed in the attached file;
   or
2. tell me, for each group of messages you are keeping, which exception
   under Article 17(3) or which compelling legitimate grounds under
   Article 21(1) you rely on, and why it applies, and confirm that I can
   complain to a supervisory authority and seek a judicial remedy, as
   Article 12(4) requires.

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

1. the purposes for which Discord is keeping them, and the legal basis
   under Article 6 for each purpose (Article 15(1)(a));
2. if the legal basis is legitimate interests, what those interests are
   and how Discord balanced them against mine, including whether a
   written assessment exists;
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

2. Objection and erasure (Articles 21(1) and 17(1)(c)): I object to the
   continued processing of this data and ask for its erasure. If Discord
   declines, please state the compelling legitimate grounds or the
   exception under Article 17(3) relied on, as Article 12(4) requires.

Please respond within one month, as Article 12(3) requires.

Kind regards,
[name or username]
```

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

Most authorities have an online form. Paste the text below into its main box, adjusting it to your case, and attach your evidence. Find your authority in the [EDPB's list of members](https://www.edpb.europa.eu/about-edpb/about-edpb/members_en). You can write in your own language: the authority will deal with the others.

```
Complaint under Article 77 GDPR

Controller: Discord Netherlands BV (Discord's EEA controller, as named in
its privacy policy)

1. Summary
On [date] I asked Discord to erase my messages under Article 17 GDPR.
[Number] of the [number] messages I asked to be erased have not been
erased. Discord has not identified any exception under Article 17(3) or
any compelling legitimate grounds under Article 21(1) for keeping them,
and has not told me of my right to complain. [My request to Discord's
Data Protection Officer of [date] received no reply within the one-month
period.]

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
- Article 17: messages kept without any exception under Article 17(3),
  on the basis of an unpublished and undefined "accessible space" rule.
- Article 12(2) and Recital 59: no practical way to exercise the right.
  Discord offers no deletion option, requires users to build their own
  CSV from a data package that can take weeks to arrive, and tells them
  bulk deletion is "not offered". [Describe your burden: e.g. "It took me
  [number] emails over [number] weeks, and I had to follow a community
  guide to find out how the process works. Deleting the remaining
  [number] messages by hand would take [estimate] hours."]
[- Article 38(4): my email to Discord's Data Protection Officer was
  handled as an ordinary support ticket and closed without a reply.]

4. What I ask the authority to do
- Order Discord to comply with my request (Article 58(2)(c)).
- Consider ordering Discord to bring its handling of erasure requests
  into compliance, for example by providing a way for users to delete
  their messages in bulk (Article 58(2)(d)).
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

If you turn down a resolution that only deletes your own messages, your complaint may take longer, because it can then only end with a decision by the authority or a wider resolution. That's the trade-off: a faster personal outcome, or a better chance of changing the process. Both are reasonable choices.

**Why it can be worth it:** a complaint that isn't settled quietly keeps the wider problem in front of the authority. That's how investigations start. If an authority looks into Discord's practices, it has real powers:
- **It can order Discord to change how it handles erasure** (Article 58(2)(d)), for example to provide a proper way for users to delete their messages.
- **It can fine Discord.** For breaches of data subject rights, including the right to erasure and the rules on answering requests, fines can reach €20 million or 4% of worldwide annual turnover, whichever is higher (Article 83(5)).
- **It has happened before.** In 2022 France's CNIL fined Discord €800,000 over its data practices, including how long it kept data.

**Your own effort is evidence too.** Discord has to *facilitate* your rights (Article 12(2)), and the GDPR expects companies to make requests easy to make, including electronically (Recital 59). If getting your messages deleted means requesting a data package, waiting weeks, running a script, writing emails that cite law, decoding templates and following a guide like this one, just to *maybe* succeed, that burden is part of the problem. Say so in your complaint: how many steps it took, how long, and what you had to work out for yourself. The fact that a community had to write this guide at all says something.

None of this is guaranteed. The authority decides whether to investigate and what to do. But every complaint that states this position adds to the evidence that the problem is Discord's process, not one person's request.

If you do want your complaint to be about more than your own data, say so at the start:

```
I would like to state my position on amicable resolution for the record.
My complaint concerns not only my own data, but how Discord handles
erasure requests generally: the lack of any option to delete messages in
bulk, the undefined "accessible space" criterion, and the absence of
reasons when requests are refused. A resolution limited to deleting my
own messages would not address these issues, and I would not regard it
as resolving my complaint. I would be open to an amicable resolution that
addressed them, for example a commitment by Discord to give users an
option to delete all their messages, or all their messages in a given
conversation or server, and to publish how it handles erasure requests.
If that is not achievable, I ask the authority, or the lead supervisory
authority, to consider whether these issues warrant an inquiry.
```

You can't force an authority to open an inquiry, and how amicable resolution works varies between countries. Stating your position still makes it much harder for your complaint to be closed quietly.

---

## UK: complaining to Discord first (section 164A)

Since 19 June 2026, UK users generally need to complain to the company before going to the ICO. Reply in the same thread, or email `privacy@discord.com`:

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

**Then, if it isn't resolved,** complain to the ICO at [ico.org.uk/make-a-complaint](https://ico.org.uk/make-a-complaint/data-protection-complaints/). The EU complaint template above works as a starting point: change "GDPR" to "UK GDPR", remove the amicable-resolution paragraph unless it applies, and add your section 164A complaint and Discord's response (or the lack of one) to the timeline and the evidence.

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

[← Legal reference](10-legal-reference.md) · [Contents](../README.md)
