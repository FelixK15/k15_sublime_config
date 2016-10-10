import sublime
import sublime_plugin


class K15CommentBlockCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region1 = self.view.sel()[0]
		rangeRegion1 = region1.b - region1.a

		if abs(rangeRegion1) > 0:
			self.view.run_command("toggle_comment", {"block":0})
		else:
			self.view.insert(edit, region1.b, "/")

