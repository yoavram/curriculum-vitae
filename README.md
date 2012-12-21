# Curriculum Vitae

This is a repository for my CV or Resume.

On December 2012 I decided to migrate my CV from Word (.doc) to [Markdown] (.md) which can be converted with [Pandoc] to PDF, HTML and DOCX for a very nice result. Another advantage of [Markdown] is that it can be version controlled and edited with a plain text editor. 

I use [Markx] to edit the CV and do the conversion, but it is done with a command similar to:

    pandoc curriculum-vitae.md -o curriculum-vitae.pdf -s --variable=geometry:a4paper

Subtitute `pdf` with `docx`, `epub`, `html`, etc.

### License

The concept, template, and code is under CC0.

The content itself, the details of my CV, should not be modified, remixed, shared or distributed without my consent.

[Markdown]: http://daringfireball.net/projects/markdown/
[Pandoc]: http://johnmacfarlane.net/pandoc
[Markx]: https://github.com/yoavram/markx