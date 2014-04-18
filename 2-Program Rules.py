from Windawesome import Windawesome, ProgramRule, State, OnWindowCreatedOrShownAction, OnWindowCreatedOnWorkspaceAction
from Windawesome.NativeMethods import WS, WS_EX

config.ProgramRules = [

	ProgramRule(
		className = "^TApplication$",
		rules = [ProgramRule.Rule(isFloating = True)]
	),

	# Browsers

    # Chrome
	ProgramRule(
		className = "^Chrome_WidgetWin_1$",
		rules = [ProgramRule.Rule(workspace = 2, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
    # Internet Explorer
	ProgramRule(
		className = "^IEFrame$",
		rules = [ProgramRule.Rule(workspace = 2, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	# Firefox
	ProgramRule(
		className = "^MozillaWindowClass$",
		rules = [ProgramRule.Rule(workspace = 2)]
	),
	# Firefox Modal
	ProgramRule(
		className = "^MozillaDialogClass$",
		rules = [ProgramRule.Rule(workspace = 2, isFloating = True)]
	),

	# Windows Explorer
	ProgramRule(
		className = "^CabinetWClass$",
		updateIcon = True,
		rules = [ProgramRule.Rule(workspace = 1, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	ProgramRule(
		className = "^ExploreWClass$",
		updateIcon = True,
		rules = [ProgramRule.Rule(workspace = 1, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),

	# Outlook
	ProgramRule(
		className = "^rctrl_renwnd32$",
		rules = [ProgramRule.Rule(workspace = 5, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),

    # Lync
	ProgramRule(
		className = "^CommunicatorMainWindowClass$",
		rules = [ProgramRule.Rule(workspace = 4, isFloating = True)]
	),
	ProgramRule(
		className = "^IMWindowClass$",
		redrawDesktopOnWindowCreated = True,
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		onWindowCreatedOnCurrentWorkspaceAction = OnWindowCreatedOnWorkspaceAction.PreserveTopmostWindow,
		onWindowCreatedOnInactiveWorkspaceAction = OnWindowCreatedOnWorkspaceAction.PreserveTopmostWindow,
		rules = [ProgramRule.Rule(workspace = 4, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),


	# Spotify Music
	ProgramRule(
		className="^SpotifyMainWindow$",
		rules = [ProgramRule.Rule(workspace = 1)]
	),
	
	# Editors
	ProgramRule(
		className = "^Vim$",
		windowCreatedDelay = 100,
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	ProgramRule(
		displayName = ".*Microsoft Visual Studio.*",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	ProgramRule(
		processName = "^devenv$",
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	ProgramRule(
		displayName = ".*Microsoft SQL Server Management Studio.*",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),

	# Terminals
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
		className = "^cygwin/x X rl$",
		windowCreatedDelay = 300,
		rules = [ProgramRule.Rule(workspace = 3)]
	),
	ProgramRule( # Console, Git Bash, Powershell
		className = "^ConsoleWindowClass$",
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
