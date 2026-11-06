# 10. Legal reference

[← Case study](09-case-study.md) · [Contents](../README.md) · [Next: Templates →](11-templates.md)

A quick reference to the provisions this guide relies on. Most article numbers are the same in the GDPR and the UK GDPR, but UK law has since added some provisions and removed others. The differences that matter here are in the UK note below. Read the full text at [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj) (GDPR) or [legislation.gov.uk](https://www.legislation.gov.uk/eur/2016/679/contents) (UK GDPR).

## The articles

| Article | What it says, in short | Why it matters here |
|---|---|---|
| **4(1)** | Personal data is any information relating to an identified or identifiable person. Information can relate to you by its content, purpose or effect (*Nowak*, C-434/16) | Messages stored against your account are generally your personal data, whether or not they mention your name. Discord's "messages containing personally identifying information" is a narrower test than the law's |
| **6(1)(b)** | Processing necessary for a contract *with you* | Discord's privacy policy lists storing and displaying messages "as you direct" under its contract with you. If that's the basis, your ground is 17(1)(a). See [which ground applies](01-how-it-works.md#which-erasure-ground-applies) |
| **6(1)(f)** | Processing based on legitimate interests | What Discord's template replies suggest (other users' interest in reading your messages), though Discord hasn't formally said so. If that's the basis, you can object (Article 21) and rely on 17(1)(c) |
| **9** | Special categories of data (health, sex life or sexual orientation, religious or philosophical beliefs, political opinions, racial or ethnic origin, trade union membership, genetic and biometric data) can only be processed if one of the conditions in Article 9(2) applies, as well as a legal basis | If messages reveal these things, Discord needs an Article 9(2) condition to keep them. Whether it has one for private messages hasn't been decided; if it has none, keeping them may be unlawful (Article 17(1)(d)). That's an argument, not an established ruling |
| **12(1)** | Information must be concise, transparent, clear and easy to access | A first reply saying bulk deletion "isn't offered", when a CSV process exists, is hard to square with this |
| **12(2)** | The company must *facilitate* the exercise of your rights | Building your own CSV, or deleting hundreds of thousands of messages by hand, isn't much facilitation |
| **Recital 59** | Explains 12(2): there should be mechanisms to request and obtain erasure, free of charge, including electronically where data is processed electronically | Discord processes everything electronically, but has no electronic way to request erasure at scale |
| **12(3)** | Answer within one month; extend by two months only with notice and reasons within the first month | Your deadline |
| **12(4)** | If it doesn't act, it must say why and tell you about your right to complain and go to court | Template replies don't do this |
| **12(5)** | Requests are free; refusing as "manifestly unfounded or excessive" is possible, but the company has to prove it. In *Brillen Rottler* (C-526/24, 2026), the CJEU held that even a first request can be excessive if the company shows it was made with abusive intent, rather than to protect the person's rights. That case concerned an access request (Article 15); it isn't a ruling that an erasure request can be refused because the person also wants to understand or challenge the company's practices | Asking for your own messages to be erased is neither. Make each request about your own data, for your own reasons ([FAQ](08-faq.md)) |
| **12(6)** | It can ask for more information only if it has reasonable doubts about who you are | Writing from your registered email is normally enough |
| **15** | Right of access: a copy of your data and information about its use (purposes, recipients, retention, source, automated decisions) | Your data package, and questions about analytics data. Article 15 doesn't list the legal basis itself; the templates ask for it because Discord had to tell you it anyway (Articles 13(1)(c) and 14(1)(c)) |
| **17(1)** | Where a ground applies, the company must erase *without undue delay* | Separate from the 12(3) deadline to tell you what it has done |
| **17(1)(a)** | Erasure when the data is no longer necessary for the purpose it was collected or processed for | The question is whether keeping your messages is still necessary for Discord's purpose. Your request is relevant, but doesn't settle it alone |
| **17(1)(c)** | Erasure when you object under Article 21(1) and there are no overriding legitimate grounds for the processing | Discord's replies describe "legitimate interests" for keeping messages for others |
| **17(1)(d)** | Erasure when the data has been processed unlawfully | A fallback, if Discord has no valid legal basis at all |
| **17(3)** | The specific exceptions: freedom of expression and information, legal obligation or a public-interest or official-authority task, public interest in public health, archiving or research, legal claims | The replies quoted in the case study cite none of them. A company can also argue that no 17(1) ground applies |
| **21(1)** | Right to object, on grounds relating to your particular situation, to processing based on legitimate interests (or a public task); the company must stop unless it shows *compelling* legitimate grounds that override your interests, rights and freedoms, or that the processing is needed to establish, exercise or defend legal claims | Make the objection explicit, and give your own reasons briefly ([Step 4](04-send-the-request.md#why-you-object-in-your-own-words)) |
| **25** | Data protection by design and by default | The argument that a platform holding this much data should be designed so that erasure works at that scale. The law doesn't prescribe a particular feature, only that the right is effective |
| **38(4)** | You can contact the Data Protection Officer about your rights | Discord's DPO address feeds into its general support queue |
| **77** | Right to complain to a supervisory authority, in particular where you live, work or where the infringement took place (EU/EEA only; see the UK note below) | Step 7 |
| **78(2)** | Court remedy if the authority doesn't handle your complaint or tell you its progress within three months (EU/EEA; in the UK, see section 166 below) | A fallback |
| **79, 82** | Court action against the company; compensation | Costly; get advice |

**National restrictions:** EU and EEA countries can add limited restrictions to these rights (Article 23) and must reconcile data protection with freedom of expression (Article 85). Ireland's Data Protection Act 2018, for example, has provisions on both. This guide doesn't cover them country by country.

**UK only:** the UK complaints system changed on 19 June 2026 (Data (Use and Access) Act 2025, section 103).
- **Section 164A** of the Data Protection Act 2018 gives you the right to complain to the company. It must acknowledge your complaint within 30 days and tell you the outcome without undue delay. The 30 days is for the acknowledgement, not for resolving the complaint.
- **Article 77 has been removed from the UK GDPR.** Complaints to the ICO are now made under **section 165** of the Data Protection Act 2018. The ICO says you can complain to it at any time, but recommends giving the company the chance to finish its complaints process first, and in most cases it will ask you to do that. Its guidance also asks you to complain within three months of your last meaningful contact with the company; that's the ICO's expectation, not a statutory time limit.
- **Controller:** Discord's privacy policy names Discord Netherlands BV for the EEA and Discord Inc. for everyone else, including the UK. It names VeraSafe as its UK representative (contact details on Discord's [Information About Local Privacy Laws](https://discord.com/terms/local-laws) page).
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

[← Case study](09-case-study.md) · [Contents](../README.md) · [Next: Templates →](11-templates.md)
