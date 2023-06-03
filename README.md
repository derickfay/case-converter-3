# case converter 3
 Alfred Case Converter workflow

**Updated March 26, 2022 to use Python 3 for MacOS 12.3 **

  


Now featuring Universal Action triggers and hotkeys for the following five actions:

  


Uppercase

Lowercase

Capitalize - capitalizes **all** words (e.g. Posting A New Topic In Share Your Workflows)

Title Case - capitalizes word except for "the", "in", "of" etc. according to American English title conventions (e.g. Posting a New Topic in Share Your Workflows)

Sentence Case - capitalizes only the first letter of the first word & converts the rest to lower case

  


All of these are set to Copy to Clipboard and Paste by default.

  


There's also a script filter **cc** which lets you view the query converted and select your choice (like the [Code Case](https://www.alfredforum.com/topic/4818-code-case/) workflow).

  


You can also connect a hot key directly to the **cc** script filter directly to view the output options without typing the **cc** command and pasting your text.

  


![ccdemo.thumb.png.613a61bc39aced79368717b23792f127.png](//content.invisioncic.com/r229491/monthly_2018_02/ccdemo.thumb.png.613a61bc39aced79368717b23792f127.png)

  


**Download:**

  


[https://www.dropbox.com/s/8fydkkef1t699et/Case Converter 3.alfredworkflow?dl=0](https://www.dropbox.com/s/8fydkkef1t699et/Case%20Converter%203.alfredworkflow?dl=0)

  


NB This is a new link and will download as a new workflow - you'll need to migrate any hotkeys and delete or disable the older version.

  


**Here's the old Python 2 version in case anyone wants it:**

  


[https://www.dropbox.com/s/3k2lh21g5wnqrkp/Case Converter 2.alfredworkflow?dl=0](https://www.dropbox.com/s/3k2lh21g5wnqrkp/Case%20Converter%202.alfredworkflow?dl=0)

  


**The original version is described below and still available, if anyone prefers it.**

  


**Workflow Version:**

  


This workflow converts the case of the text on the clipboard.

  


<http://dfay.fastmail.fm/alfred/Case%20Converter.alfredworkflow>

  


There are two workflows which display the following five options:

  


Uppercase

Lowercase

Capitalize - capitalizes **all** words (e.g. Posting A New Topic In Share Your Workflows)

Title Case - capitalizes word except for "the", "in", "of" etc. according to American English title conventions (e.g. Posting a New Topic in Share Your Workflows)

Sentence Case - capitalizes only the first letter of the first word & converts the rest to lower case

  


The keyword **case** will transform the text on the clipboard without pasting the result.

The keyword **casep** will transform the text on the clipboard and paste (using Applescript System Events)

  


**Hotkey Version:**

  


Here is a version for use with hotkeys which will operate on the active selection in OS X and paste it with the converted text.  These all have a half second delay prior to pasting, which is necessary for Applescript to be able to paste.

  


<http://dfay.fastmail.fm/alfred/Case%20Hotkeys.alfredworkflow>

  


**Notes and Revision History:**

  


These use the Title Case perl script found at <https://raw.github.com/ap/titlecase/master/titlecase> .

  


If you manage academic citations with BibDesk, Zotero, Papers, Mendeley, etc., Title Case conversion is especially useful for cleaning up downloaded citations.

  


Updated May 3, 2013 with nicer colored icon thanks to mjv ( [http://www.alfredforum.com/user/4384-mjv/](https://www.alfredforum.com/user/4384-mjv/) )

  


Updated February 5, 2014 to handle Sentence Case and to add a second keyword to paste after conversion.

  


Updated May 20, 2014 with hotkeys
