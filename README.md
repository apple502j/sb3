# sb3 - sb3 parses SB3
## Hm, what on earth is sb3?
I should have said that people using the library should know what SB3 is... well, you guessed it. It's a file extension for Scratch 3.0 Projects. sb3 is a parser for SB3 files. (Also, we have SPRITE3 parser.)

## How do I use it?
Import, open, and try. Example:

```py
import sb3
project, assets = sb3.open_sb3("my_game.sb3") # project is a ProjectJSON object, assets is ZipFile.ZipExtFile
print(f"Hmm, I guessed you like the browser with UA {project.meta.user_agent}...")
print(f"What? You use {' extension, '.join(project.extensions)}!?")
```

There is no documentation as of now. But maybe you can check the testcase code and the source code!

## Hmm, can I use it?
All people, cats and other cute animals with **Python 3.6 or above** can use this library. If you are not cute but want to use this, try `sb3.cute()`.
## Who made it?
A person named apple502j, with a secretary kenny2github (who invented GenericData class).

## May I contribute?
Of course under GPL! Feel free to submit issues and PRs. If you have a bug, make sure to submit the SB3 file with the issue.
