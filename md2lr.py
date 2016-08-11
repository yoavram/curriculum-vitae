title = """title: Curriculum Vitae
---
_model: cv
---
body:
"""

with open('curriculum-vitae.md', 'rt') as fin, open('contents.lr', 'wt') as fout:
	fout.write(title)
	next(fin)
	next(fin)
	next(fin)
	fout.write(fin.read())
