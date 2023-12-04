-- You can add your own plugins here or in other files in this directory!
--  I promise not to create any merge conflicts in this directory :)

-- See the kickstart.nvim README for more information

return {
        {'mbbill/undotree',lazy=false},
        {'ThePrimeagen/harpoon',
        dependencies = { {'nvim-lua/plenary.nvim'} }},
        {'donRaphaco/neotex'},
        { 'windwp/nvim-autopairs',
    event = "InsertEnter",}
}
