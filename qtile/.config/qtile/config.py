# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import subprocess
import os
from libqtile import hook



# Programs
terminal = "alacritty"
web_browser = "brave"

# Quick Settings
default_font = "JetBrainsMono Nerd Font"
default_font_size = 18
bar_spacing = 12
bar_padding = 20
part_padding = 22
bar_top_height = 28
bar_bottom_height = 28
window_gap_size = 15

# Presets: , , ██, ░▒▓▓▒░, 
bar_left = ""
bar_right = ""

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])

#Colors
catppuccin = {
    "flamingo": "#F3CDCD",
    "mauve": "#DDB6F2",
    "pink": "#f5c2e7",
    "maroon": "#e8a2af",
    "red": "#f28fad",
    "peach": "#f8bd96",
    "yellow": "#fae3b0",
    "green": "#abe9b3",
    "teal": "#b4e8e0",
    "blue": "#96cdfb",
    "sky": "#89dceb",
    "white": "#d9e0ee",
    "gray": "#6e6c7e",
    "black": "#1a1826",
}

mod = "mod4"
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(["control", "mod1"], "t", lazy.spawn(terminal), desc="Launch terminal #1"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal #2"),
    Key([mod], "w", lazy.spawn(web_browser), desc="Launch the web browser."),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Lockscreen
    Key([mod], "m", lazy.spawn("betterlockscreen -l"), desc="Launch the lockscreen."),

    # Rofi Integration
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch an application."),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window"), desc="Switch between windows."),

    # Polybar Stuff
    Key([mod], "b", lazy.spawn("polybar main"), desc="Spawn Polybar."),
    Key([mod, "shift"], "b", lazy.spawn("pkill polybar"), desc="Kill Polybar."),

    # Picom Stuff
    Key([mod, "control"], "p", lazy.spawn("picom --experimental-backends -b"), desc="Start Picom."),
    Key([mod, "shift"], "p", lazy.spawn("pkill picom"), desc="Stop Picom."),

    # Poweroff Menu
    Key([mod], "p", lazy.spawn(os.path.expanduser("~/.dotfiles/qtile/.config/qtile/power_menu.sh")), desc="Launch the power menu."),

    # Flameshot
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Take a screenshot."),

    # XKill
    Key([mod], "x", lazy.spawn("xkill"), desc="Launches XKill."),
    # sound control
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),


]

groups = [Group(i) for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
group_hotkeys = "123456789"

for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {g.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=False),
                desc=f"Switch to & move focused window to group {g.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(
        margin=window_gap_size,
        border_width=2,
        border_normal=catppuccin['black'],
        border_focus=catppuccin['mauve'],
        ),
    layout.Max(),
    # layout.Columns(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
     layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=default_font,
    fontsize=default_font_size,
    padding=2,
    forground=catppuccin["black"],
)
extension_defaults = widget_defaults.copy()

def get_widgets_top(primary=False):
    widgets = [
        widget.Spacer(
            length=bar_padding,
            background=catppuccin['black'],
            ),
        widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["mauve"],
            background=catppuccin['black'],
            ),
        widget.GroupBox(
            highlight_method="line",
            background=catppuccin["mauve"],
            highlight_color=[catppuccin["mauve"], catppuccin["mauve"]],
            inactive=catppuccin["black"],
            ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["mauve"],
            background=catppuccin['black'],
            ),
        widget.Spacer(
            length=bar_spacing,
            background=catppuccin['black'],
            ),
        widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["gray"],
            background=catppuccin['black'],
            ),
        widget.Systray(
            background=catppuccin["gray"],
            foreground=catppuccin['black'],
            ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["gray"],
            background=catppuccin['black'],
            ),
        widget.Spacer(
            length=part_padding,
            background=catppuccin['black']
            ),
        widget.WindowName(
            fontsize=15,
            foreground=catppuccin["white"]
            ),
         widget.Spacer(
            length=part_padding,
            background=catppuccin['black'],
            ),
         widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["sky"],
            background=catppuccin['black'],
            ),
        widget.Volume(
            fmt="墳 {}",
            mute_command="amixer -D pulse set Master toggle",
            foreground=catppuccin["black"],
            background=catppuccin["sky"],
            ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["sky"],
            background=catppuccin['black'],
            ),
         widget.Spacer(
            length=bar_spacing,
            background=catppuccin['black'],
            ),
         widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["teal"],
            background=catppuccin['black'],
            ),
        widget.Battery(foreground=catppuccin["black"],
                       background=catppuccin["teal"],
                       low_background=catppuccin["red"],
                       low_percentage=0.3),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["teal"],
            background=catppuccin['black'],
            ),
         widget.Spacer(
            length=bar_spacing,
            background=catppuccin['black'],
            ),
         widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["peach"],
            background=catppuccin['black'],
            ),

        widget.CPU(
            format=" {load_percent:04}%",
            foreground=catppuccin["black"],
            background=catppuccin["peach"],
            ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["peach"],
            background=catppuccin['black'],
            ),
        widget.Spacer(
            length=bar_spacing,
            background=catppuccin['black'],
            ),
        widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["maroon"],
            background=catppuccin['black'],
            ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=catppuccin["black"],
            background=catppuccin["maroon"],
            ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["maroon"],
            background=catppuccin['black'],
            ),
        widget.Spacer(
            length=bar_padding,
            background=catppuccin['black'],
            ),
            ]
    if primary:
        pass
    return widgets

def get_widgets_bottom(primary=False):
    widgets = [
        widget.Spacer(
            length=bar_padding,
            background=catppuccin['black'],
            ),
         widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["red"],
            background=catppuccin['black'],
            ),
         widget.TaskList(
            background = catppuccin['red'],
            foreground = catppuccin['black'],
            highlight_method = 'block',
            border = catppuccin['gray']
            ),
         widget.TextBox(
             text=bar_right,
             padding=0,
             fontsize=30,
             foreground=catppuccin["red"],
             background=catppuccin['black'],
             ),
        widget.Spacer(
            length=bar_padding + 1000,
            background=catppuccin['black']
            ),
            ]
    if primary:
        pass
    return widgets

screens = [
    Screen(
        top=bar.Bar(
           get_widgets_top(primary=True),
           bar_top_height,
           background=catppuccin['black'],
        ),
        bottom=bar.Bar(
           get_widgets_bottom(primary=True),
           bar_bottom_height,
           background=catppuccin['black'],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
