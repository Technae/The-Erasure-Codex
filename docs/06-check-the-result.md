# 6. Check the result

[← Discord's replies, decoded](05-replies-decoded.md) · [Contents](../README.md) · [Next: Deadlines and complaints →](07-deadlines-and-complaints.md)

A confirmation email tells you what Discord *submitted*, not what it deleted. The only way to know is to compare a data package from before your request with one from afterwards.

## When to request the second package

Wait until Discord has confirmed processing, then give it a week or two before requesting a new package. Remember that you can usually only request one about every 30 days.

## Compare with the helper script

Put both ZIP files in the same folder as the script:

```bash
python3 erasure_helper.py compare package-before.zip package-after.zip
```

```
Old export: 762269 messages
New export: 640380 messages
No longer in export (in old, not in new): 121948
Present in both exports:                  640321
New in newer export:                      59
Share of old messages no longer exported: 16.0%
Note: this shows what Discord's export no longer includes.
It can't show whether every copy, including backups, has been erased.
```

(These are the real figures from the [case study](09-case-study.md).)

Two options make the result more useful:

```bash
python3 erasure_helper.py compare package-before.zip package-after.zip \
    --report per_channel.csv --remaining remaining.csv
```

- **`per_channel.csv`** shows, for every channel, how many messages are no longer in the export and how many are still there. It's the clearest way to see the "accessible space" rule at work: channels you'd left go to zero, channels you're still in don't change. **It includes channel names, so don't post it publicly.**
- **`remaining.csv`** lists every message that's in both exports, in the `channel_id,message_id` format, ready to send in your follow-up.

The script compares each message together with its channel, the same pairs as in the CSV. If it can't read a package reliably (for example, because Discord has changed the export format), it stops with an error rather than reporting a misleading count. It won't write its output over either package; add `--force` if you want it to overwrite an earlier report.

## Without the script

With extracted copies of both packages (not the originals), make a list of message IDs from each:

```bash
jq -r '.[].ID' Messages/c*/messages.json | sort -u > ids.txt
```

Then, in the folder above both:

```bash
comm -23 before/ids.txt after/ids.txt | wc -l   # removed
comm -12 before/ids.txt after/ids.txt | wc -l   # still present
```

## Things that can confuse the count

- **Messages you deleted yourself** in the meantime will show as "removed". If you've been deleting by hand, note roughly how many.
- **New messages** you've sent since the first package show up as "new", not as failures.
- **Missing messages:** some users report packages that seem to leave out messages. If a number looks odd, spot-check a few IDs in the app. With Developer Mode on, you can open a message directly at `https://discord.com/channels/@me/CHANNEL_ID/MESSAGE_ID` for a DM, or `https://discord.com/channels/SERVER_ID/CHANNEL_ID/MESSAGE_ID` for a server.

## What a comparison can and can't show

Three different things are easy to confuse:
1. **A message is missing from your new data package.** That's what the comparison shows: Discord's export no longer includes it.
2. **A message is gone from Discord's live systems.** That's what you see when it no longer appears in the app. It's the strongest practical check you have.
3. **Every copy is gone, including backups.** Backups are normally overwritten over a period of time, not instantly. A company may also keep some data for a limited time where an exception applies. You can't see backups. Discord's [retention article](https://support.discord.com/hc/en-us/articles/5431812448791) says its database backups are kept for 30–45 days and then deleted, and that clearing identifying information from backups after an account deletion can take up to 45 days. That's Discord's own published figure, not something you can check, but it gives you a specific point to ask about.

Discord's own pages don't fully agree here. Its [data package article](https://support.discord.com/hc/en-us/articles/360004957991) says a deleted message "is no longer stored in Discord". Its [retention article](https://support.discord.com/hc/en-us/articles/5431812448791) says public posts may be kept for 180 days to two years after deletion. So a message missing from your package may still exist in another Discord system. If that matters to you, ask, using the [general access request](11-templates.md#access-request-everything-discord-holds-about-you-general-dsar).

So report your results precisely: "these messages are no longer in my data package or visible in the app" is accurate. "Discord has erased every copy" is something only Discord can confirm.

## Keep the evidence

Record the hash of the new package (see [Step 2](02-get-your-data.md)), and keep the output of the comparison with the date. If you complain, these figures, alongside Discord's confirmation emails, are your strongest evidence.

[← Discord's replies, decoded](05-replies-decoded.md) · [Contents](../README.md) · [Next: Deadlines and complaints →](07-deadlines-and-complaints.md)
