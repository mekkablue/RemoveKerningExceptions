# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################


from GlyphsApp.plugins import *

class RemoveKerningExceptions(FilterWithoutDialog):
	
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Remove Kerning Exceptions', 
			'de': u'Kerning-Ausnahmen entfernen'
			})
		self.keyboardShortcut = None # With Cmd+Shift

	def filter(self, layer, inEditView, customParameters):
		glyph = layer.glyph()
		glyphID = glyph.id
		glyphName = glyph.name
		masterID = layer.associatedFontMaster().id
		font = layer.font()
		
		# glyph on the left side:
		if glyphID in font.kerning[masterID].keys():
			rightKeys = font.kerning[masterID][glyphID].keys()[:]
			for rightKey in rightKeys:
				if rightKey[0] != "@":
					rightKey = font.glyphForId_(rightKey).name
				if not customParameters:
					print "Removing %s %s" % (glyphName, rightKey)
				font.removeKerningForPair(masterID, glyphName, rightKey)
		
		# glyph on the right side:
		leftKeys = font.kerning[masterID].keys()[:]
		for leftKey in leftKeys:
			if glyphID in font.kerning[masterID][leftKey].keys()[:]:
				if leftKey[0] != "@":
					leftKey = font.glyphForId_(leftKey).name
				if not customParameters:
					print "Removing %s %s" % (leftKey, glyphName)
				font.removeKerningForPair(masterID, leftKey, glyphName)
