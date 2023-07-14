local wk = require("which-key")
local builtin = require('telescope.builtin')
wk.register({
    a={
        name='harpoon',
    },
    u={name='undo',
    t={vim.cmd.UndotreeToggle,"toggle undo tree"},
    s={vim.cmd.UndotreeShow,"Show undotree"}
},
    c={name='code',},
    f={
        name='file',
        f={vim.cmd.Ex,"find file"},
    },
    s={
        name='search',
        f={builtin.find_files,"telescope search"},
        g={builtin.git_files,"git search"},
        s={builtin.live_grep,"grep"},

    }
},{prefix="<leader>"})
