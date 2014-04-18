from System.Drawing import Color, Font
from System.Linq import Enumerable
from Windawesome import ILayout, TileLayout, FullScreenLayout, FloatingLayout, IPlugin, Workspace
from Windawesome import Bar, LayoutWidget, WorkspacesWidget, ApplicationTabsWidget, SystemTrayWidget, CpuMonitorWidget, RamMonitorWidget, LaptopBatteryMonitorWidget, LanguageBarWidget, CurrentlyPlayingWidget, SeparatorWidget
from Windawesome import LoggerPlugin, ShortcutsManager, InputLanguageChangerPlugin
from Windawesome.NativeMethods import MOD
from System import Tuple
from System.Windows.Forms import Keys

def onLayoutLabelClick():
	if windawesome.CurrentWorkspace.Layout.LayoutName() == "Full Screen":
		windawesome.CurrentWorkspace.ChangeLayout(FloatingLayout())
	elif windawesome.CurrentWorkspace.Layout.LayoutName() == "Floating":
		windawesome.CurrentWorkspace.ChangeLayout(TileLayout())
	else:
		windawesome.CurrentWorkspace.ChangeLayout(FullScreenLayout())

config.WindowBorderWidth = 0
config.WindowPaddedBorderWidth = 0

config.CheckForUpdates = True

workspacesWidgetForegroundColors = [Color.LightSeaGreen for i in range(0, 5)]
workspacesWidgetBackgroundColors = [Color.Black for i in range(0, 5)]

config.Bars = Enumerable.ToArray[Bar]([
	Bar(windawesome.monitors[0],
		[
			WorkspacesWidget(
				normalForegroundColor = workspacesWidgetForegroundColors,
				normalBackgroundColor = workspacesWidgetBackgroundColors,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
				highlightedInactiveForegroundColor = Color.LightSeaGreen,
				highlightedInactiveBackgroundColor = Color.Black,
				flashingForegroundColor = Color.Black
			),
			LayoutWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black,
				onClick = onLayoutLabelClick
			)
		],

		[
			#SystemTrayWidget(True),
			CpuMonitorWidget(
				foregroundColor = Color.LightSeaGreen,
				backgroundColor = Color.Black,
			),
			RamMonitorWidget(
				foregroundColor = Color.LightSeaGreen,
				backgroundColor = Color.Black,
			),
			LaptopBatteryMonitorWidget(
				foregroundColor = Color.LightSeaGreen,
				backgroundColor = Color.Black,
			),
		],

		[
			ApplicationTabsWidget(
				normalForegroundColor = Color.LightSeaGreen,
				normalBackgroundColor = Color.Black,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
			)
		],

		backgroundColor = Color.Black,
		font = Font("Consolas", 8)
	)
])

config.Workspaces = Enumerable.ToArray[Workspace]([
	Workspace(windawesome.monitors[0], FloatingLayout(), [config.Bars[0]], name = 'main'),
	Workspace(windawesome.monitors[0], FullScreenLayout(), [config.Bars[0]], name = 'web'),
	Workspace(windawesome.monitors[0], TileLayout(), [config.Bars[0]], name = 'dev'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaAxis = TileLayout.LayoutAxis.TopToBottom, masterAreaWindowsCount = 2, masterAreaFactor = 0.5), [config.Bars[0]], name = 'chat'),
	Workspace(windawesome.monitors[0], FullScreenLayout(), [config.Bars[0]], name = 'mail'),
])

config.StartingWorkspaces = [config.Workspaces[0]]

config.Plugins = [
	ShortcutsManager(),
]
