local mark = require("harpoon.mark")
local ui = require("harpoon.ui")

vim.keymap.set("n", "<leader>aa", mark.add_file, { desc = "add mark" })
vim.keymap.set("n", "<leader>am", ui.toggle_quick_menu, { desc = "mark menu" })
