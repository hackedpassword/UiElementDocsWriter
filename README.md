# UiElementDocsWriter

## Description

To address an issue with Unciv's auto document writing for UI's

## What, why?

The [problem being addressed](https://github.com/yairm210/Unciv/issues/9633) is that [the regex in this file](https://github.com/yairm210/Unciv/blob/master/desktop/src/com/unciv/app/desktop/UiElementDocsWriter.kt) is doing too much, and does not produce the correct output. It is responsible for generating the table [seen here](https://yairm210.github.io/Unciv/Modders/Creating-a-UI-skin/#available-ui-elements). And under the hood, here is the [auto-generated markdown](https://github.com/yairm210/Unciv/blob/master/docs/Modders/Creating-a-UI-skin.md).

The 3rd and 4th columns are very tricky to procure. I've taken a different approach to solving the problem:

1. Walk the code tree with python against a local cloned Unciv repo, flatten the code.
2. Lines that sprawled into multi-lines are now tightened to be consistent for parsing.
3. Pipe the flattened single-lines to a perl script for lots of regex parsing.
4. Extract Shapes.
5. Extract colors or tintColors.
6. Table-ize!

Looks like this locally ([whole output here](https://github.com/hackedpassword/UiElementDocsWriter/blob/main/parsed_output.md)):
```
D:\Dev\Python\Dev>py flattener.py | perl uie_parser.pl
| Directory | Name | Default shape | Image |
|---|:---:|:---:|---|
| General/ | ExpanderTab | null | BaseScreen.skinStrings.skinConfig.baseColor )  |
| General/ | KeyCapturingButton | null | null |
| LanguagePickerScreen/ | LanguageTable | null | if (chosenLanguage == language) baseColor else darkBaseColor  |
| General/ | TabbedPager | null | backgroundColor |
| General/ | Tooltip | roundedEdgeRectangle | null |
| General/ | Border | null | color |
| WorldScreen/CityButton/ | InfluenceBar | null | Color.BLACK |
| WorldScreen/CityButton/ | DefenceTable | roundedTopEdgeRectangleSmall | null |
| WorldScreen/CityButton/ | AirUnitTable | roundedEdgeRectangleSmall | null |
...
| AnimatedMenu/ | Button | roundedEdgeRectangleMid | null |
| General/Popup/ | Background | null | Color.GRAY.cpy().apply { a = 0.5f } |
| General/Popup/ | InnerTable | null | BaseScreen.skinStrings.skinConfig.baseColor.darken(0.5f)  |
| object | RoundedEdgeRectangle | roundedEdgeRectangle | null |
| object | RectangleWithOutline | rectangleWithOutline | null |
| object | Select-box | selectBox | null |
...
| TechPickerScreen/ | CurrentTechColor | null | 72, 147, 175 |
| TechPickerScreen/ | ResearchedTechColor | null | 255, 215, 0 |
| TechPickerScreen/ | ResearchableTechColor | null | 28, 170, 0 |
| TechPickerScreen/ | QueuedTechColor | null | 7*2, 46*2, 43*2 |
| TechPickerScreen/ | ResearchedFutureTechColor | null | 127, 50, 0 |
| TechPickerScreen/ | Background | null | skinStrings.skinConfig.clearColor |
| TechPickerScreen/ | BottomTable | null | skinStrings.skinConfig.clearColor |
| General/ | Border | null | Color.WHITE |
| General/ | Border | null | color |
| TechPickerScreen/ | Background | null | queuedTechColor.darken(0.5f) |
```

The `image` column probably needs some discussion. I punted and whatever value `tintColor = ` had is put into Image. To me, the object forms and conditionals look like maybe that's legit, so it's included for now.

If there was no `dir`, some object might have been named, that could be the object's name, so we grabbed that for `name` then and called `dir` "object".

I designed the [flattener](https://github.com/hackedpassword/UiElementDocsWriter/blob/main/flattener.py), gpt-4 wrote most of it. I then designed and wrote the [uie_parser](https://github.com/hackedpassword/UiElementDocsWriter/blob/main/uie_parser.pl), had gpt-4 debug and tighten a few lines to save time. Prototype was done in Excel.

Next step is to convert the two scripts into Kotlin. I have a plan for that.


