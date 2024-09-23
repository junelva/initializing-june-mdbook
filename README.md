`[WORK IN PROGRESS]`

It's a book of conversations with my reflection in the machine.

Read here: https://junelva.github.io/initializing-june-mdbook/

After my rough preprocessing code, the editing process consist(s/ed) of mostly this:

* Condense broken lines of responses to single lines, reducing newlines.
* Add `>  ` between neighboring lines of text in every reponse.
* Fix placement and formatting of all numbered lists and headers.
* Search for `— ` and ` —`, replacing as needed. (em-dash usage)
* Search for `- ` and ` -`, replacing as needed. (hyphenation)
* Search for ` o `, and correctly format as indented bulleting.
* Traverse every instance of `*` used for bolding and replace with `**`.
* Traverse every instance of `/` used for italicization and replace with `*`.
* Ensure correct line breaking in generated poetry.
* Redact proper names and branding (besides my own name).
* Redact generated code samples.
* Probably other stuff too.

Because the commercially-minded creators of the language model I used in these conversations do not support reliable, computer-readable data export (with which I could have composed the whole thing programmatically), the creation of this book took a dedicated amount of hacking and manual editing work.

It can also be read here without the full functionality of the compiled HTML version.

* [Introduction](src/introduction.md)
* [Index of Conversations](src/conversations/README.md)
