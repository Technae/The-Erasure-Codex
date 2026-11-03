# 1. How it works

[← Contents](../README.md) · [Next: Get your data package →](02-get-your-data.md)

## Your rights

If you're in the **EU or EEA**, the GDPR applies. If you're in the **UK**, the UK GDPR applies, and it's nearly identical for this purpose. Both give you:

- **The right to erasure (Article 17).** You can ask for your personal data to be erased. The usual grounds are that Discord no longer needs it for the purpose it was collected for (17(1)(a)), or that you object to its processing and Discord has no overriding legitimate grounds to continue (17(1)(c), together with Article 21).
- **The right to object (Article 21).** Where a company relies on "legitimate interests", as Discord says it does when it keeps your messages for other users, you can object. It must then stop unless it can show *compelling* legitimate grounds that override yours.
- **The right to a proper answer (Article 12).** Discord must reply within one month. If it doesn't do what you asked, it must tell you why and that you can complain to a data protection authority or a court. Requests are free.

Article 17(3) lists the only situations where erasure can be refused: freedom of expression and information, a legal obligation, public health, archiving or research, and legal claims. "Other users would like to keep reading your messages" isn't on that list as such. Discord might try to argue that it falls under freedom of expression and information, or that it's a compelling ground under Article 21, but as of 2026 its replies don't cite any of these. They don't cite any article at all.

### Which erasure ground applies?

Article 17(1) lists several grounds for erasure. Which one fits depends on the **legal basis** Discord uses to keep your messages, and Discord hasn't said clearly which that is. Its own documents point two ways:

| If Discord keeps your messages on the basis of… | What points to this | Your ground for erasure | To refuse, Discord must show… |
|---|---|---|---|
| **Legitimate interests** (Article 6(1)(f)) | Template replies say other users "have a legitimate interest in having access to content sent to them" | Object under Article 21(1). Erasure then follows under **17(1)(c)** | Compelling legitimate grounds that override your interests, rights and freedoms, or an Article 17(3) exception |
| **Contract** (Article 6(1)(b)) | The privacy policy says messages are stored to display them "as you direct" | **17(1)(a):** the messages are no longer necessary. Once you ask for them to be erased, keeping them isn't needed to do what you directed | That keeping them is still necessary for its contract *with you*, or an Article 17(3) exception |

Three points follow from this:
- **Contract only covers the contract with you.** Article 6(1)(b) applies to a contract "to which the data subject is party", meaning you. Other users wanting to keep reading your messages isn't part of your contract. If that's Discord's reason, it's relying on legitimate interests, and you can object.
- **If Discord has no valid basis at all** for keeping a message, **17(1)(d)** applies (unlawful processing). That's a fallback, not something to lead with.
- **The Article 17(3) exceptions apply whichever basis it is,** and Discord has to say which one it relies on.

That's why the templates cite both 17(1)(a) and 17(1)(c): you don't know which basis Discord will rely on, and citing both covers each case. They also ask Discord to state the legal basis for anything it keeps, so it has to commit to one.

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

This "accessible space" rule is the core problem. It isn't in the GDPR, Discord doesn't publish it, and it's applied mechanically. In the [case study](09-case-study.md), it kept a DM between two accounts belonging to the same person, after **both** accounts asked for it to be erased. It also kept DMs with users who had already deleted their accounts, where nobody else is left to "keep access".

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
Your data package also contains analytics and other "activity" data, sometimes going back many years. You can object to and ask for erasure of that too (see [Step 4](04-send-the-request.md)). You can also limit future collection in **User Settings → Data & Privacy**.

## What you'll need

- Access to the **email address registered to your account**. Requests from other addresses get bounced or ignored.
- About an hour, spread over a few weeks, to request your data package, wait for it, build the CSV and send the request.
- Patience. Expect templates, and expect to reply more than once.

[← Contents](../README.md) · [Next: Get your data package →](02-get-your-data.md)
