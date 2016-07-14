# RemoveKerningExceptions

This is a plugin for the [Glyphs font editor](http://glyphsapp.com/) by Georg Seifert.

*Filter > Remove Kerning Exceptions* removes all kerning exception of selected glyphs in the current master, leaving group kerning intact. Its true power lies in its application as custom parameter. This can be useful in situations where you change the shape of a letter with a *Rename Glyphs* parameter, and its kerning exceptions do not apply anymore.

### Installation

Either install the plugins via *Window > Plugin Manager*, and restart Glyphs, or:

1. Download the complete ZIP file and unpack it, or clone the repository.
2. Double click the .glyphsFilter file. Confirm the dialogs that appear in Glyphs.
3. Restart Glyphs.

### Usage Instructions

#### In Edit View:

1. Choose a font master (Cmd-1, 2, ...).
2. Select one or more glyphs.
3. Choose *Filter > Remove Kerning Exceptions*. There will be status messages documenting all kern pair deletions in the Macro window (*Window > Macro Panel*).
4. To update the view, move the cursor or click in the canvas.

#### At Export Time:

1. Go to *File > Font Info > Instances*, and pick an instance.
2. In your instance, add a new *Filter* custom parameter.
3. Set the *Value* of the parameter to `RemoveKerningExceptions;include:x` and replace `x` with the name of the glyph (or comma-separated names of the glyphs) for which you want to remove kerning exceptions at export time.

### Requirements

The plugin needs Glyphs 2.3.1 or higher, running on OS X 10.9 or later. I can only test it in current OS versions, and I assume it will not work in older versions.

### License

Copyright 2016 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Jan Gerner (@yanone) and Georg Seifert (@schriftgestalt).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
