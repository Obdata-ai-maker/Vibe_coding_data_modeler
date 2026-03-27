Good thinking—that’s how you keep continuity like a real project.

Here’s a **clean, structured prompt** you can reuse anytime to bring me back into the exact same mentorship mode 👇

---

I am building a data modeling and BI engine from scratch in Python.

Project scope (MVP):

* DataModel manages tables and relationships
* Tables contain only schema (no data)
* Columns are metadata only (name, type)
* Relationships define joins between tables
* Later: QueryEngine (BFS for joins + SQL generation)

Design principles:

* DataModel is the gatekeeper (validation + object creation)
* Table, Column, Relationship are internal classes (not exposed)
* Use dict for tables and columns, list for relationships
* Normalize names (tables + columns) to lowercase
* Fail fast: no invalid objects allowed

Current progress:

* Implementing core classes: Column, Table, DataModel
* Working on DataModel.add_table() with validation and normalization
* No QueryEngine yet

Mentorship style:

* Challenge my design decisions
* Focus on system design before coding
* Push for clean architecture (no shortcuts)
* Be strict and point out flaws

Please continue guiding me from here and review my code like a senior engineer.

---

# 🧠 How to use it

When you restart:

1. Paste that prompt
2. Add your latest code below it
3. Ask: *“review this”* or *“what’s next?”*

---

# 🔥 Pro tip

You can also add:

```text
Current issue:
<what you’re stuck on>
```

👉 That lets me jump directly into debugging or design critique.

---

This keeps:

* same level of depth
* same architecture
* same mentor tone

---

When you're ready, paste your `add_table()` implementation and we continue.
