General/ | ExpanderTab | null | BaseScreen.skinStrings.skinConfig.baseColor ) 
General/ | KeyCapturingButton | null | null
LanguagePickerScreen/ | LanguageTable | null | if (chosenLanguage == language) baseColor else darkBaseColor 
General/ | TabbedPager | null | backgroundColor
General/ | Tooltip | roundedEdgeRectangle | null
General/ | Border | null | color
WorldScreen/CityButton/ | InfluenceBar | null | Color.BLACK
WorldScreen/CityButton/ | DefenceTable | roundedTopEdgeRectangleSmall | null
WorldScreen/CityButton/ | AirUnitTable | roundedEdgeRectangleSmall | null
WorldScreen/CityButton/ | IconTable | roundedEdgeRectangleMid | null
WorldScreen/ | AirUnitTable | null | null
General/ | HealthBar | null | Color.BLACK
General/ | Tooltip | roundedEdgeRectangle | null
General/ | AnimatedMenu | roundedEdgeRectangle | null
AnimatedMenu/ | Button | roundedEdgeRectangleMid | null
General/Popup/ | Background | null | Color.GRAY.cpy().apply { a = 0.5f }
General/Popup/ | InnerTable | null | BaseScreen.skinStrings.skinConfig.baseColor.darken(0.5f) 
object | RoundedEdgeRectangle | roundedEdgeRectangle | null
object | RectangleWithOutline | rectangleWithOutline | null
object | Select-box | selectBox | null
object | Select-box-pressed | selectBoxPressed | null
object | Checkbox | checkbox | null
object | Checkbox-pressed | checkboxPressed | null
CityScreen/CitizenManagementTable/ | ResetCell | null | colorButton 
CityScreen/CitizenManagementTable/ | AvoidCell | null | if (city.avoidGrowth) colorSelected else colorButton 
CityScreen/CitizenManagementTable/ | FocusCell | null | if (city.cityAIFocus == focus) colorSelected else colorButton 
CityScreen/CityConstructionTable/ | ConstructionsQueueTable | null | Color.BLACK 
CityScreen/CityConstructionTable/ | AvailableConstructionsTable | null | Color.BLACK 
CityScreen/CityConstructionTable/ | QueueEntrySelected | null | Color.GREEN.darken(0.5f) 
CityScreen/CityConstructionTable/ | QueueEntry | null | Color.BLACK 
CityScreen/CityConstructionTable/ | PickConstructionButton | null | Color.BLACK 
CityScreen/CityConstructionTable/ | PickConstructionButtonSelected | null | Color.GREEN.darken(0.5f) 
CityScreen/CityConstructionTable/ | Header | null | BaseScreen.skinStrings.skinConfig.baseColor ) 
CityScreen/ | CityPickerTable | roundedEdgeRectangle | null
CityScreen/CityScreenTileTable/ | InnerTable | null | BaseScreen.skinStrings.skinConfig.baseColor.darken(0.5f) 
CityScreen/CityScreenTileTable/ | Background | null | Color.WHITE
CityScreen/CityStatsTable/ | Background | null | 194, 180, 131
CityScreen/CityStatsTable/ | InnerTable | null | Color.BLACK.cpy().apply { a = 0.8f } 
CityScreen/ConstructionInfoTable/ | SelectedConstructionTable | null | BaseScreen.skinStrings.skinConfig.baseColor.darken(0.5f) 
CityScreen/ConstructionInfoTable/ | Background | null | Color.WHITE 
General/ | Border | null | color
CivilopediaScreen/ | EntryButton | null | 50, 75, 125
MainMenuScreen/ | MenuButton | roundedEdgeRectangle | null
MainMenuScreen/ | Background | null | clearColor
MapEditor/MapEditorToolsDrawer/ | Handle | null | BaseScreen.skin.getColor("color") 
ModManagementOptions/ | ExpanderTab | null | Color(0x203050ff) 
ModManagementScreen/ | BottomTable | null | skinStrings.skinConfig.clearColor
ModManagementScreen/ | TopTable | null | skinStrings.skinConfig.clearColor
MultiplayerScreen/ | BottomTable | null | skinStrings.skinConfig.clearColor
MultiplayerScreen/ | TopTable | null | skinStrings.skinConfig.clearColor
NewGameScreen/ | GameOptionsTable | null | BaseScreen.skinStrings.skinConfig.clearColor
NewGameScreen/ | MapOptionsTable | null | BaseScreen.skinStrings.skinConfig.clearColor
NewGameScreen/NationTable/ | Background | null | Color.DARK_GRAY.cpy().apply { a = 0.75f } 
NewGameScreen/NationTable/ | Title | null | outerColor 
NewGameScreen/NationTable/ | RightInnerTable | null | textBackgroundColor 
NewGameScreen/NationTable/ | BorderTable | null | outerColor 
NewGameScreen/NationTable/ | Background | null | innerColor 
NewGameScreen/ | BottomTable | null | skinStrings.skinConfig.clearColor
NewGameScreen/ | TopTable | null | skinStrings.skinConfig.clearColor
NewGameScreen/ | PlayerPickerTable | null | BaseScreen.skinStrings.skinConfig.clearColor
NewGameScreen/PlayerPickerTable/ | PlayerTable | null | BaseScreen.skinStrings.skinConfig.baseColor.darken(0.8f) 
OverviewScreen/DiplomacyOverviewTab/ | CivTable | null | Color.BLACK 
OverviewScreen/NotificationOverviewTable/ | Notification | roundedEdgeRectangle | null
OverviewScreen/ReligionOverviewTab/ | BeliefDescription | null | BaseScreen.skinStrings.skinConfig.baseColor 
OverviewScreen/TradesOverviewTab/ | OffersTable | null | civ.nation.getOuterColor() 
OverviewScreen/UnitOverviewTab/ | UnitSupplyTable | null | BaseScreen.skinStrings.skinConfig.baseColor.darken(0.6f) 
PolicyScreen/ | PolicyButton | roundedEdgeRectangleSmall | null
PolicyScreen/ | PolicyBranchBackground | null | null
PolicyScreen/ | PolicyBranchHeader | null | null
PolicyScreen/ | PolicyBranchAdoptButton | roundedEdgeRectangleSmall | null
PromotionScreen/ | PromotionButton | roundedEdgeRectangleMid | null
TechPickerScreen/ | TechButtonIconsOutline | roundedEdgeRectangleSmall | Color.BLACK.cpy().apply { a = 0.7f } 
TechPickerScreen/ | CurrentTechColor | null | 72, 147, 175
TechPickerScreen/ | ResearchedTechColor | null | 255, 215, 0
TechPickerScreen/ | ResearchableTechColor | null | 28, 170, 0
TechPickerScreen/ | QueuedTechColor | null | 7*2, 46*2, 43*2
TechPickerScreen/ | ResearchedFutureTechColor | null | 127, 50, 0
TechPickerScreen/ | Background | null | skinStrings.skinConfig.clearColor
TechPickerScreen/ | BottomTable | null | skinStrings.skinConfig.clearColor
General/ | Border | null | Color.WHITE
General/ | Border | null | color
TechPickerScreen/ | Background | null | queuedTechColor.darken(0.5f)
LoadGameScreen/ | BottomTable | null | skinStrings.skinConfig.clearColor
LoadGameScreen/ | TopTable | null | skinStrings.skinConfig.clearColor
VictoryScreen/ | CivGroup | roundedEdgeRectangle | null
WorldScreen/ | Notification | roundedEdgeRectangle | null
WorldScreen/ | Notification | roundedEdgeRectangle | null
PlayerReadyScreen/ | Background | null | curCiv.nation.getOuterColor() 
WorldScreen/ | PickTechButton | roundedEdgeRectangle | 7, 46, 43
WorldScreen/ | TutorialTaskTable | null | skinStrings.skinConfig.baseColor.darken(0.5f)
WorldScreen/ | BattleTable | null | BaseScreen.skinStrings.skinConfig.baseColor.apply { a = 0.8f } 
WorldScreen/ | TileInfoTable | null | BaseScreen.skinStrings.skinConfig.baseColor.darken(0.5f) 
WorldScreenMusicPopup/TrackList/ | Up | null | skin.getColor("color")
WorldScreenMusicPopup/TrackList/ | Down | null | skin.getColor("positive")
WorldScreenMusicPopup/TrackList/ | Over | null | skin.getColor("highlight")
WorldScreen/Minimap/ | Background | null | Color.GRAY 
WorldScreen/Minimap/ | Border | null | Color.WHITE 
WorldScreen/NextTurn/ | ProgressBar | null | defaultRightColor
WorldScreen/NextTurn/ | ProgressColor | null | null
WorldScreen/TopBar/ | StatsTable | null | backColor
WorldScreen/TopBar/ | ResourceTable | null | backColor
WorldScreen/TopBar/ | LeftAttachment | roundedEdgeRectangle | null
WorldScreen/TopBar/ | RightAttachment | roundedEdgeRectangle | null
WorldScreen/ | UnitTable | roundedEdgeRectangleMid | null
WorldScreen/ | UnitTable | roundedEdgeRectangleMid | null
