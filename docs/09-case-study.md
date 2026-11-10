# 9. Case study: one request in 2026

[← FAQ](08-faq.md) · [Contents](../README.md) · [Next: Legal reference →](10-legal-reference.md)

This is one user's request, from Ireland, with real figures and Discord's real replies. The user also [posted it in Undiscord discussion #429](https://github.com/victornpb/undiscord/discussions/429), where they're updating it as deadlines pass.

## Summary

- **762,269** messages in the February 2026 data package
- **121,948** removed by mid-March (16%), almost all in servers and group chats the user had already left
- **640,321** still present: everything the user could still open
- By September 2026, **99.3% of the messages still in the account (635,544 of 640,314) were in DMs**. Only 4,339 were left in server channels, 364 in group chats, 64 in threads and 3 in voice channels. You can't leave a DM, so the "access" rule spares almost nothing else
- Complaint filed with the Irish Data Protection Commission (DPC) in March/April 2026. In June it moved to the DPC's Cross Border Assessment team, and as of November 2026 it had no case officer
- Four formal requests were made to Discord's Data Protection Officer and privacy team in October 2026. The deadlines for three of them (4, 9 and 9 November) passed with no reply and no notice of an extension. The fourth is due on 23 November

## What Discord said, and what it did

The first reply (2 February 2026):

> We don't offer the ability to delete your messages in bulk right now.

It explained that other users "have a legitimate interest in having access to content sent to them", and that "Consistent with GDPR, Discord balances the privacy interests of the user against the interests other users have in a conversation". It cited no exception and didn't mention the right to complain.

Eight days later, after a follow-up, the same team wrote:

> If, however, you believe you have sent messages which include specific identifiable personal data and/or sensitive personal data - your name, or other information about you - we can certainly help you remove such information. […] Please provide us with a CSV file of the messages containing personally identifying information in the following format: channel_id, message_id

The user sent four CSVs between 7 and 25 February. The first went through Discord's support form on 7 February, attached directly, in a separate ticket. Discord confirmed it on 15 February as "submitted for deletion", except messages in spaces the user could still access, other users' messages, and invalid IDs. The other three were emailed in the original thread as file-host links, because the file was too big to attach. Discord answered the first two of those by asking for a CSV again, and confirmed the last on 2 March, with the same three exclusions.

So in the same week, the same team told the user in one ticket that bulk deletion wasn't offered, and confirmed a bulk deletion in another. One reason the support-form request went faster may be that the CSV was attached rather than linked. That's the user's experience, not something Discord has explained.

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

| Sent | Request | Deadline | Result |
|---|---|---|---|
| 4 Oct | Access to analytics data (purposes, legal basis, recipients, retention); objection to and erasure of it; the legal basis for keeping two specific DMs | 4 Nov | No reply, no extension notice |
| 8 Oct | Erase two DMs with deleted users, or state the exception and whose interests it protects | 9 Nov | No reply, no extension notice |
| 8 Oct | Access request for an account Discord deleted for inactivity in 2024 | 9 Nov | No reply, no extension notice |
| 21 Oct | Access: retention after account deletion, use for model training, recipients, transfers | 23 Nov | Pending |

Each result was checked the day after the deadline, after noon Irish time, so the deadline had passed in every time zone.

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

1. **Don't stop at the first reply.** In the same week, the same team said bulk deletion wasn't offered in one ticket and confirmed a bulk deletion in another.
2. **Check, don't trust.** "Submitted for deletion" covered messages that were never deleted.
3. **Ask the same question every time:** which exception? Months of unanswered questions are themselves the evidence.
4. **Keep everything,** with dates and hashes, from the start.
5. **Attach the CSV as a file,** not a link to a file host ([Build the CSV](03-build-the-csv.md#what-to-include)).

[← FAQ](08-faq.md) · [Contents](../README.md) · [Next: Legal reference →](10-legal-reference.md)
