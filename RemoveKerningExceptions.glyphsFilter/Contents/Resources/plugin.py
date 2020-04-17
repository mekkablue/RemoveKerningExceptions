# encoding: utf-8
from __future__ import division, print_function, unicode_literals

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

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class RemoveKerningExceptions(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Remove Kerning Exceptions', 
			'de': 'Kerning-Ausnahmen entfernen',
			'fr': 'Supprimer les exceptions de crénage',
			'es': 'Borrar excepciones de kerning',
			})
		self.reportString = Glyphs.localize({
			'en': 'Removing kerning exception: %s - %s', 
			'de': 'Kerning-Ausnahme entfernt: %s - %s',
			'fr': 'Exception de crénage supprimée: %s - %s',
			'es': 'Excepción de kerning borrada: %s - %s',
			})
		self.keyboardShortcut = None # With Cmd+Shift

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		glyph = layer.parent
		if glyph:
			glyphID = glyph.id
			glyphName = glyph.name
			masterID = layer.master.id
			font = layer.font()
		
			# glyph on the left side:
			if glyphID in font.kerning[masterID].keys():
				rightKeys = font.kerning[masterID][glyphID].keys()[:]
				for rightKey in rightKeys:
					if rightKey[0] != "@":
						rightKey = font.glyphForId_(rightKey).name
					if not customParameters:
						print(self.reportString % (glyphName, rightKey))
					font.removeKerningForPair(masterID, glyphName, rightKey)
		
			# glyph on the right side:
			leftKeys = font.kerning[masterID].keys()[:]
			for leftKey in leftKeys:
				if glyphID in font.kerning[masterID][leftKey].keys()[:]:
					if leftKey[0] != "@":
						leftKey = font.glyphForId_(leftKey).name
					if not customParameters:
						print(self.reportString % (leftKey, glyphName))
					font.removeKerningForPair(masterID, leftKey, glyphName)
