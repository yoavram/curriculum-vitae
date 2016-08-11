title = """title: Curriculum Vitae
---
body:
"""

print("Converting curriculum-vitae.md to contents.lr for lektor...")
with open('curriculum-vitae.md', 'rt') as fin, open('contents.lr', 'wt') as fout:
	fout.write(title)
	next(fin)
	next(fin)
	next(fin)
	fout.write(fin.read())
