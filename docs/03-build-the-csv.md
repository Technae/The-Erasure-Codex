# 3. Build the CSV

[← Get your data package](02-get-your-data.md) · [Contents](../README.md) · [Next: Send the request →](04-send-the-request.md)

Discord asks for a CSV file with one line per message:

```
channel_id,message_id
111111111111111111,100000000000000000
111111111111111111,100000000000000001
```

You don't need to write it by hand. Use the helper script, or one of the alternatives below.

## Option A: the helper script (recommended)

[`scripts/erasure_helper.py`](../scripts/erasure_helper.py) is a single file that uses only standard Python 3. It reads your package **directly from the ZIP**, without extracting or changing it, and doesn't connect to the internet. If it meets a file or message record it can't read reliably, it stops with an error instead of quietly giving you a smaller CSV, and it only puts the CSV in place once the whole run has succeeded, so a failed run never leaves a half-written file. Read it before running it if you like: it's short.

**1. Install Python 3** if you don't have it ([python.org](https://www.python.org/downloads/)). On Linux and macOS it's usually already there.

**2. Download the script** and put it in the same folder as your package.

**3. See what's in your package:**

```bash
python3 erasure_helper.py summary package.zip
```

Example output (yours will differ):

```
Channel type            Channels    Messages
GUILD_TEXT                   240       51200
DM                            35       20400
GROUP_DM                       6        3100
TOTAL                        281       74700
```

**4. Write the CSV:**

```bash
python3 erasure_helper.py csv package.zip -o messages_to_delete.csv
```

On Windows, use `python` or `py` instead of `python3` if that's what works.

### Useful options

| Option | What it does |
|---|---|
| `--exclude keep.txt` | Leave out the channels listed in `keep.txt` (one channel ID per line), e.g. chats you want to keep |
| `--only these.txt` | Include only the channels listed in `these.txt` |
| `--split 100000` | Split into several files of at most 100,000 messages each, plus the header line (`messages_to_delete_part1.csv`, `_part2`, …), if one file is too big to send |
| `--no-header` | Leave out the `channel_id,message_id` header line |
| `--force` | Overwrite an output file that already exists. Without it, the script won't replace an existing file, and it never writes over the package itself or over the `--only`/`--exclude` lists |
| `--allow-incomplete` | Only if the script stops because some message records can't be read: write the CSV anyway, leaving those records out. It warns you how many, and names any channel where no record could be read (that whole channel is left out). Please also [open an issue](https://github.com/Technae/The-Erasure-Codex/issues) so the script can be fixed |

To find a channel's ID in Discord, turn on **User Settings → Advanced → Developer Mode**, then right-click the channel or DM and choose **Copy Channel ID**.

## Option B: ishnz's bulk_deletion_helper

[bulk_deletion_helper](https://github.com/ishnz/bulk_deletion_helper) by ishnz is the tool linked in No Text To Speech's video, and the one this guide's author used for the requests in the [case study](09-case-study.md). Without it, this guide probably wouldn't exist. It's a set of small Python scripts that read your package locally. They don't connect to the internet or ask for your token.

1. **Extract a copy** of your package (keep the original ZIP untouched).
2. Put `dumpallmessages.py` in the extracted folder, next to the `Messages` folder.
3. Run it:

```bash
python3 dumpallmessages.py
```

It writes `messages.csv` in the same folder, with one `channel_id,message_id` line per message (its header line reads `channelid,messageid`, which Discord has accepted). The repository also has scripts to include or leave out a list of channels; see its README.

Good to know: it expects the current package layout (a `Messages` folder with a `messages.json` in each channel folder), and it has no option to split large files, so see "How big is too big?" below if yours is large.

## Option C: jq and a terminal

If you have [`jq`](https://jqlang.org/) and an **extracted copy** of a recent package (not your original):

```bash
cd extracted-package/Messages
for d in c*/; do
  id="${d#c}"; id="${id%/}"
  jq -r --arg c "$id" '.[] | "\($c),\(.ID)"' "$d/messages.json"
done > ../../messages_to_delete.csv
```

Older packages use `messages/` and `messages.csv` instead, so the script in Option A is easier for those.

## Option D: other tools

Community tools that read data packages exist, such as [undiscord-package-util](https://github.com/dorifor/undiscord-package-util), which the old Discordomicon guide linked to. Check what any tool does before trusting it with your package, and never use one that asks for your Discord token or password. Building the CSV only needs the package.

## What to include

**Everything you want erased.** Don't pre-filter for "messages with personal information" unless you want to. Discord's templates sometimes say the CSV is for messages containing personally identifiable information, but in practice it filters by access, not content (see the [case study](09-case-study.md)), and all of your messages relate to you.

**How big is too big?** Hundreds of thousands of lines are fine for Discord's process, but your email provider may limit attachment size (often around 20–25 MB). A CSV of 760,000 messages is about 30 MB. If yours is too big, either use `--split` and send the files in separate replies in the same thread, or compress it, or upload it to a file host and send a link. Links can expire or need permissions, so check that it opens in a private browser window.

**A note on support attachments:** in 2025 a breach at a third-party customer support provider used by Discord exposed data from support tickets. A CSV of IDs reveals little on its own, but don't attach anything you don't need to, especially ID documents.

[← Get your data package](02-get-your-data.md) · [Contents](../README.md) · [Next: Send the request →](04-send-the-request.md)
