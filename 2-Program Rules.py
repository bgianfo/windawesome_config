from Windawesome import Windawesome, ProgramRule, State, OnWindowCreatedOrShownAction, OnWindowCreatedOnWorkspaceAction
from Windawesome.NativeMethods import WS, WS_EX

config.ProgramRules = [
	ProgramRule(
		className = "^cygwin/x X rl$",
		windowCreatedDelay = 300,
		rules = [ProgramRule.Rule(workspace = 1)]
	),
	ProgramRule(
		className = "^TApplication$",
		rules = [ProgramRule.Rule(isFloating = True)]
	),
	ProgramRule(
		className = "^MozillaWindowClass$",
		rules = [ProgramRule.Rule(workspace = 2)]
	),
	ProgramRule(
		className = "^MozillaDialogClass$",
		rules = [ProgramRule.Rule(workspace = 2, isFloating = True)]
	),
	ProgramRule(
		className = "^CabinetWClass$", # Windows Explorer
		updateIcon = True,
		rules = [ProgramRule.Rule(workspace = 1)]
	),
	ProgramRule(
		className = "^ExploreWClass$", # Windows Explorer
		updateIcon = True,
		rules = [ProgramRule.Rule(workspace = 1)]
	),
	ProgramRule(
		displayName = ".*SA Dictionary 2010.*",
		rules = [ProgramRule.Rule(isFloating = True)]
	),
	ProgramRule(
		className = "^rctrl_renwnd32$", # Outlook
		rules = [ProgramRule.Rule(workspace = 5)]
	),
	ProgramRule(
		className = "^{97E27FAA-C0B3-4b8e-A693-ED7881E99FC1}$", # foobar2000
		rules = [ProgramRule.Rule(workspace = 1)]
	),

	# editors

	ProgramRule(
		className = "^Vim$",
		#windowCreatedDelay = 100,
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	ProgramRule(
		displayName = ".*Microsoft Visual Studio.*",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),

	# chat

	ProgramRule(
		className = "^icoTrilly$",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.TemporarilyShowWindowOnCurrentWorkspace,
		onWindowCreatedOnInactiveWorkspaceAction = OnWindowCreatedOnWorkspaceAction.PreserveTopmostWindow,
		rules = [ProgramRule.Rule(workspace = 4, isFloating = True)]
	),
	ProgramRule(
		className = "^ico.*",
		processName = "^trillian$",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		onWindowCreatedOnCurrentWorkspaceAction = OnWindowCreatedOnWorkspaceAction.PreserveTopmostWindow,
		onWindowCreatedOnInactiveWorkspaceAction = OnWindowCreatedOnWorkspaceAction.PreserveTopmostWindow,
		rules = [ProgramRule.Rule(workspace = 4)]
	),

	# terminals

	ProgramRule(
		className = "^Console_2_Main$",
		rules = [ProgramRule.Rule(workspace = 3)]
	),
	ProgramRule(
		className = "^mintty$",
		redrawDesktopOnWindowCreated = True,
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),

	ProgramRule(
		className = "^MsiDialogCloseClass$",
		isManaged = False
	),
	ProgramRule(
		className = "^MsiDialogNoCloseClass$",
		isManaged = False
	),
	ProgramRule(
		className = "^\$\$\$Secure UAP Dummy Window Class For Interim Dialog$"
	),
	ProgramRule(
		className = "^#32770$", # all dialogs
		rules = [ProgramRule.Rule(isFloating = True)] # should be floating
	),
	ProgramRule(
		styleContains = WS.WS_POPUP,
		isManaged = False
	),
	ProgramRule(
		styleNotContains = WS.WS_MAXIMIZEBOX,
		rules = [ProgramRule.Rule(isFloating = True)]
	),
	ProgramRule() # an all-catching rule in the end to manage all other windows
]
