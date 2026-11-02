# erasure_helper.py

A small, dependency-free Python 3 script for working with a Discord data package when making an erasure request.

- Reads the package **directly from the .zip** (or an extracted folder) and never changes it
- Works with both the current JSON layout and older CSV layouts
- Doesn't connect to the internet, and never needs your token or password

| Command | What it does |
|---|---|
| `python3 erasure_helper.py summary package.zip` | Count your messages by channel type |
| `python3 erasure_helper.py csv package.zip -o messages_to_delete.csv` | Write the `channel_id,message_id` CSV Discord asks for |
| `python3 erasure_helper.py compare old.zip new.zip` | Show how many messages were removed between two packages |

Options for `csv`: `--exclude FILE`, `--only FILE` (channel IDs, one per line), `--split N`, `--no-header`.
Options for `compare`: `--report FILE` (per-channel counts, includes channel names, keep private), `--remaining FILE` (IDs still present, ready to resend).

See [Step 3](../docs/03-build-the-csv.md) and [Step 6](../docs/06-check-the-result.md) for a walkthrough. Licence: MIT.
