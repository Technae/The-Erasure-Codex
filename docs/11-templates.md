# 11. Templates: Discord's DPO and data protection authorities

[← Legal reference](10-legal-reference.md) · [Contents](../README.md) · [Next: Deleted or banned accounts →](12-banned-accounts.md)

This page collects templates for the later stages: writing to **Discord's Data Protection Officer (DPO)**, and **complaining to a data protection authority**. For the first request, see [Step 4](04-send-the-request.md). For replies to Discord's support templates, see [Step 5](05-replies-decoded.md).

Fill in the parts in square brackets, and delete anything that doesn't apply to you.

**UK users:** the DPO templates use the EU wording for Article 12(4). Wherever a template says *"tell me that I can complain to a supervisory authority and seek a judicial remedy, as Article 12(4) requires"*, write instead:

```
tell me how I can complain (to you under section 164A of the Data
Protection Act 2018, and to the Information Commissioner) and seek a
judicial remedy, as Article 12(4) UK GDPR requires
```

Since 19 June 2026, UK Article 12(4) requires the company to mention both of those complaint routes. Also change "GDPR" to "UK GDPR" and the controller to "Discord Inc.".

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

If it gets a support template and a "solved" status, reply in the same thread if further contact is useful (see [Step 5](05-replies-decoded.md)), and keep the correspondence. The ticket may reopen, but its status doesn't reset or extend the legal deadline.

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
  relies on. Instead, it has relied on an undefined "accessible space"
  criterion, without explaining how that criterion fits the GDPR or why
  keeping the messages is necessary for the purposes concerned. Its
  privacy policy only says that users can delete their own messages "if
  you still have access to the space where you posted it"; it doesn't
  say that erasure requests exclude those spaces.
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
- **How many messages** you'd have to delete by hand: the "still present" figure from [Step 6](06-check-the-result.md)
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

[← Legal reference](10-legal-reference.md) · [Contents](../README.md) · [Next: Deleted or banned accounts →](12-banned-accounts.md)
