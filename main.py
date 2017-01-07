import sublime
import sublime_plugin

from .source.cache_directives import cache, get as getDirectivePath

class GoToDirectiveCommand(sublime_plugin.TextCommand):
	def plugin_loaded():
		folders = sublime.active_window().folders()
		cache(folders)

	def run(self, edit):
		name = self.getPointWord()
		file = getDirectivePath(name)

		if file:
			self.openFile(file)

	def getPointWord(self):
		selection = self.view.sel()[0]
		region = self.view.word(selection)

		return self.view.substr(region)

	def openFile(self, file):
		sublime.active_window().open_file(file);'some'

