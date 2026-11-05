# erasure_helper.py

A small, dependency-free Python 3 script for working with a Discord data package when making an erasure request.

- Reads the package **directly from the .zip** (or an extracted folder) and never changes it: it refuses to write output over the package or into an extracted package folder
- Stops with a clear error if a file or message record isn't in a format it recognises, rather than reporting a smaller count (`--allow-incomplete` overrides this for unreadable records, and says so)
- Writes output to a temporary file and only puts it in place once the whole run has succeeded, so a failed run never leaves a partial CSV or damages an earlier one
- Works with both the current JSON layout and older CSV layouts
- Doesn't connect to the internet, and never needs your token or password

| Command | What it does |
|---|---|
| `python3 erasure_helper.py summary package.zip` | Count your messages by channel type |
| `python3 erasure_helper.py csv package.zip -o messages_to_delete.csv` | Write the `channel_id,message_id` CSV Discord asks for |
| `python3 erasure_helper.py compare old.zip new.zip` | Show how many messages are no longer in the newer export |

Options for `summary`: `--allow-incomplete`.
Options for `csv`: `--exclude FILE`, `--only FILE` (channel IDs, one per line), `--split N` (messages per file, plus the header), `--no-header`, `--force`, `--allow-incomplete`.
Options for `compare`: `--report FILE` (per-channel counts, includes channel names, keep private), `--remaining FILE` (IDs in both exports, ready to resend), `--force`, `--allow-incomplete`.

The comparison counts `(channel_id, message_id)` pairs. It shows what Discord's export no longer includes, not whether every copy has been erased.

**Tests:** `python3 -m unittest test_erasure_helper -v` (run from this folder) checks the script against small mock packages, including malformed ones. Please run it before submitting changes.

**For maintainers:** `python3 scripts/build_full.py` (run from the repository root) rebuilds [`CODEX-FULL.md`](../CODEX-FULL.md), the whole guide in one file, from the individual pages. Run it after changing any page.

See [Step 3](../docs/03-build-the-csv.md) and [Step 6](../docs/06-check-the-result.md) for a walkthrough. Licence: MIT.
