local wk = require("which-key")
local builtin = require('telescope.builtin')
wk.register({
    a={
    name='harpoon',
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

    }
},{prefix="<leader>"})
