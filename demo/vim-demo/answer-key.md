# Answer key — do NOT project this

Three bugs, revealed one at a time by running the script. Each maps to a vim verb.

## Bug 1 — `ci"`, change inside quotes

```
$ python3 report.py
FileNotFoundError: [Errno 2] No such file or directory: 'dat/segments.csv'
```

Fix: cursor anywhere inside `"dat/segments.csv"` → `ci"` → type `data/segments.csv` → `Esc`

## Bug 2 — `dd` + `p`, move a line

```
NameError: name 'late_pct' is not defined
```

The assignment sits *below* the print that uses it.
Fix: on the `late_pct = ...` line → `dd` (cut), `k` (up), `p` (paste above the print)

## Bug 3 — `2dd`, delete two lines

Script finally runs, but spams:

```
DEBUG remove me
DEBUG remove me
```

Fix: cursor on the first `DEBUG` line → `2dd`

## Bonus flexes

- `:%s/DEBUG//gn` — count DEBUG occurrences without changing anything (`n` = dry run)
- `vimtutor` — the 30-minute follow-up for the audience
