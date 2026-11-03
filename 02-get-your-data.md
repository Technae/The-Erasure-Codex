# 2. Get your data package

[← How it works](01-how-it-works.md) · [Contents](../README.md) · [Next: Build the CSV →](03-build-the-csv.md)

Your data package is a ZIP file from Discord with a copy of your data. You need it for two reasons:

1. **It lists the IDs of the messages you've sent**, which Discord asks for in the CSV. (Some users report packages missing messages; see below.)
2. **It's your "before" picture.** Comparing it with a later package is the only reliable way to see what was really deleted ([Step 6](06-check-the-result.md)).

## How to request it

**Desktop or browser:** User Settings (the cog, bottom left) → **Data & Privacy** → **Request your data** → **Request Data**. Choose what to include, then **Request My Data**.

**Mobile:** your avatar → the cog → **Data & Privacy** → **Request all of my data**.

Tick **Messages** (and everything else, if you want the full picture). Discord says the package arrives within 30 days. It's often much sooner. The download link is sent to your account's email and stays valid for 30 days.

Things to know:
- **You can only have one request running at a time,** and users report waiting about a month before you can request another. Plan around that: you'll want a second package later to check the result.
- **Deleting or disabling your account before the link arrives cancels the request.**
- **Messages in servers you've left are still included.** The "Servers" folder only lists servers you're in now, but the "Messages" folder covers everything you've sent. Some users have reported packages that seem to be missing messages, so treat it as very good rather than perfect.
- **If you can't get into your account**, Discord's help page says to contact privacy@discord.com.
- **The package isn't everything Discord holds.** Discord's [data package article](https://support.discord.com/hc/en-us/articles/360004957991) says it leaves out support and Trust & Safety correspondence, and that a message you delete "is no longer stored in Discord", so it won't be in the package. But Discord's [retention article](https://support.discord.com/hc/en-us/articles/5431812448791) says public posts may be kept for 180 days to two years after deletion, for example to train safety models. If you want everything, use the [general access request](11-templates.md#access-request-everything-discord-holds-about-you-general-dsar).

## What's inside

| Folder | What it holds |
|---|---|
| `Account/` | Your account details, settings, connections, sessions |
| `Activity/` | Analytics and other event data (subfolders such as reporting, analytics, modeling, tns). Discord says the tns (Trust & Safety) data "is retained for up to 2 years" |
| `Messages/` | One subfolder per channel or DM you've written in, plus an index of channel names |
| `Servers/` | Servers you're currently in |

Inside `Messages/`, each channel has its own folder (named like `c123456789012345678`) containing:
- `channel.json`: the channel ID and type (DM, group DM or server channel), and for server channels, the server
- `messages.json` (or `messages.csv` in older packages): your messages, each with an **ID**, a timestamp, the contents and any attachment links

Folder names and formats have changed over the years. The helper script handles both the JSON and the older CSV layout.

## Keep it as evidence

Treat the ZIP as evidence from day one:

1. **Don't edit it, and don't open the files in a text editor that might save changes.** If you want to look inside, use a viewer, the helper script, or the terminal (`less`, `jq`).
2. **Record its fingerprint.** A SHA-256 hash proves later that the file hasn't changed:
   - Linux: `sha256sum package.zip`
   - macOS: `shasum -a 256 package.zip`
   - Windows (PowerShell): `Get-FileHash package.zip`

   Save the result in a text file with the date, for example `hashes.txt`.
3. **Keep a copy somewhere safe**, and rename it with the date you received it, such as `package-2026-02-07.zip`.

[← How it works](01-how-it-works.md) · [Contents](../README.md) · [Next: Build the CSV →](03-build-the-csv.md)
