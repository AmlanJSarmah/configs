########################################### Set up the config ##############################################
import os
import subprocess
from libqtile.config import Group, Key, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook

class Colors:
    #DARK: str = "282a36" # Tokyo night
    DARK: str = "1d1f21" # Alacritty default
    WHITE: str = "ffffff"
    # BORDER_ACTIVE: str = "e1acff" #A magenta like color
    BORDER_ACTIVE: str = "6272a4"
    BORDER_INACTIVE: str = "1D2330" 
    WORKSPACE_BLOCK_COLOR: str = "6272a4"

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
terminal = "alacritty"      # My terminal of choice
browser = "firefox" # My browser of choice
palette = Colors()
home = os.path.expanduser('~')


########################################## Keybindings ###########################################################


keys = [
    # Move window focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Suffle windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Change window size
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
   

    # WM related binding
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod],"f",lazy.spawn("rofi -show drun"), desc="Launch Rofi App Launcher"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run -l 10 -fn 'Fira Code Nerd Font-12' -p 'Run' -sb #6272a4"), desc="Launch Dmenu run prompt"),

    # Custom keybindings for screenshot and volume
    Key([mod], "s", lazy.spawn(str(home) + "/.local/bin/screenshot.sh all"),desc="Take a screenshot of entire screen"),
    Key([mod, "shift"], "s", lazy.spawn(str(home) + "/.local/bin/screenshot.sh window"),desc="Take a screenshot of active window"),
    Key([mod, "control"], "s", lazy.spawn(str(home) + "/.local/bin/screenshot.sh select"),desc="Take a screenshot of selected area"),
    #Key([mod, "shift"], "v", lazy.spawn(str(home) + "/.local/bin/changevolume.sh down"),desc="Decrease volume"),
    #Key([mod], "v", lazy.spawn(str(home) + "/.local/bin/changevolume.sh up"),desc="Increases volume"),
]


#############################################3 Screen Layouts #############################################


layout_theme = {
                "border_width": 2,
                "margin": 10,
                "border_focus": palette.BORDER_ACTIVE,
                "border_normal": palette.BORDER_INACTIVE,
                "border_on_single": True,
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    #layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.RatioTile(**layout_theme),
    #layout.Floating(**layout_theme)
]

###################################### Workspaces #####################################################


# groups = [Group(i) for i in "123456789"]
groups = [Group("1", label=""),
          Group("2", label="", layout="max"),
          Group("3", label=""),
          Group("4", label="", layout="max"),
          Group("5", label=""),
          Group("6", label=""),
          Group("7", label="󰎆"),
          Group("8", label="󰙯", layout="max"),
          Group("9", label=""),
          Group("0", label="")]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )


###################################### ScratchPads ##########################################################

groups.append(
    ScratchPad(
        'scratchpad',
        [
            DropDown(
                'term',
                'alacritty',
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.1,
                opacity=0.75,
            ),
            ]
    )
)

keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
])



########################################## Bar and Widgets ####################################################

widget_defaults = dict(
    font='Sauce Code Pro Nerd Font',
    fontsize=15,
    padding=7,
)

extension_defaults = widget_defaults.copy()
separator = widget.TextBox(text=" ",padding=5)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    # Color of the nos in workspace tabs like 1, 2, 3. 4
                    active=palette.WHITE,
                    inactive=palette.WHITE,

                    # Removes border from the workspace tabs
                    borderwidth=0,                    

                    # Removes unwanted default margin
                    margin_x=0,

                    # Color the workspace block 
                    this_current_screen_border=palette.WORKSPACE_BLOCK_COLOR,

                    # Color the entire workspace
                    highlight_method="block",

                    # Hides the unused workspaces
                    hide_unused=False,
                    
                    fontsize=17
                ),
                widget.Spacer(),
                widget.Systray(padding=10),
                separator,
                widget.TextBox(text=" ",  padding=0, mouse_callbacks={"Button1":lazy.spawn(browser + " -new-window github.com/AmlanJSarmah")}),
                separator,
                widget.Battery(format='  {char} {percent:2.0%}', unknown_char="", padding=0),
                separator,
                widget.Wlan(format='  {essid}',disconnected_message="  Disconnected",interface='wlp3s0',padding=0), 
                separator,
                widget.Clock(format='  %H:%M', padding=0),
                separator,
                widget.Clock(format = '  %a %d/%m/%y',padding=0),
                separator,
                widget.QuickExit(default_text=" ", countdown_format=" {}", padding=0),
                separator,
            ],
            25,
            margin=[10, 10, 0, 10],
            background=palette.DARK,
            opacity=1,
        ),
    ),
]


################################################################# Autostart apps ###################################################################


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.run([home + '/.config/qtile/autostart.sh'])
