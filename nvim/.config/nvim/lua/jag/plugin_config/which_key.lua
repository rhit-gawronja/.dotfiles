local wk = require("which-key")
wk.register({
    a={
    name='harpoon',
},
c={name='code',},
    f={
        name='file',
        f={vim.cmd.Ex,"find file"},
    },
},{prefix="<leader>"})
