import sublime
import sublime_plugin


class K15CommentBlockCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.sel();

		commentBlock = 0
		
		for region in regions:
			regionRange = region.b - region.a
			
			if abs(regionRange) > 0:
				commentBlock = 1
				break

		if commentBlock == 1:
			self.view.run_command("toggle_comment", {"block":0})
		else:
			for region in regions:
				self.view.insert(edit, region.a, "/")