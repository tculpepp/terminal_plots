# Exploring options for CLI/Terminal plots

Exploring options for plots that can be used in [obsidian](https://obsidian.md) or similar note taking tools or version controlled in a repo with other relevant information

## The Requirements
- My primary use is plots in my [obsidian](https://obsidian.md) notebook so I need these to accurately display there. (using a code block is acceptable)
- I do most of my explortation and scripting in Python, so we need that compatibility
- Has to still be usable when only in monochrome (color isn't always an option)

## The Hit List

- [x] [mpl_ascii](https://github.com/chriscave/mpl_ascii)
- [ ] [terminalplot](https://github.com/kressi/terminalplot)
- [ ] [asciichartpy](https://pypi.org/project/asciichartpy/)
- [ ] [termplot](https://github.com/justnoise/termplot)
- [ ] [termgraph](https://github.com/sgeisler/termgraph)
- [ ] [plotille](https://github.com/sgeisler/termgraph)
- [ ] [termcharts](https://pypi.org/project/termcharts/)
- [ ] [plotext](https://github.com/piccolomo/plotext)

credit for findign the majority of these tools goes to [Sourav De](https://medium.com/@SrvZ) for this article: [How to Create Stunning Graphs in the Terminal with Python](https://medium.com/@SrvZ/how-to-create-stunning-graphs-in-the-terminal-with-python-2adf9d012131)

## Notes on each:

### [mpl_ascii](https://github.com/chriscave/mpl_ascii)

This one is a matplotlib backend which means that I *should* be able to seamlessly switch between ascii and graphical plots just by changing the plotting backend. That seems pretty useful. Need to try plugging this in to several existing projects with plots to see if it hold true.

Monochrome looks reasonable so far. Bar plots and line graphs are usable. The scatter plot is just hard without color.