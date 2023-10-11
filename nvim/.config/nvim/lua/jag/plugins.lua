local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
    vim.fn.system({
        "git",
        "clone",
        "--filter=blob:none",
        "https://github.com/folke/lazy.nvim.git",
        "--branch=stable", -- latest stable release
        lazypath,
    })
end

vim.opt.rtp:prepend(lazypath)
local plugins={
    --looks and feel
    'rebelot/kanagawa.nvim',
    'nvim-tree/nvim-web-devicons',
    'hiphish/rainbow-delimiters.nvim',
        {'nvim-lualine/lualine.nvim',
lazy=false},{
        "folke/which-key.nvim",
        event = "VeryLazy",
        init = function()
            vim.o.timeout = true
            vim.o.timeoutlen = 300
        end,
        opts = {
            -- your configuration comes here
            -- or leave it empty to use the default settings
            -- refer to the configuration section below
        }
    },
    -- speed buffs
    {
        'ThePrimeagen/harpoon',
        dependencies = { {'nvim-lua/plenary.nvim'} }},{
            'nvim-telescope/telescope.nvim',
            -- or                            , branch = '0.1.x',
            dependencies = { {'nvim-lua/plenary.nvim'} }
        }
        ,{'mbbill/undotree',lazy=false},
        -- treesitter
        'nvim-treesitter/nvim-treesitter',
        --tpope
        'tpope/vim-fugitive',
        'tpope/vim-commentary',
        -- completion
        {
            'VonHeikemen/lsp-zero.nvim',
            dependencies = {
                -- LSP Support
                {'neovim/nvim-lspconfig'},
                {'williamboman/mason.nvim'},
                {'williamboman/mason-lspconfig.nvim'},

                -- Autocompletion
                {'hrsh7th/nvim-cmp'},
                {'hrsh7th/cmp-buffer'},
                {'hrsh7th/cmp-path'},
                {'saadparwaiz1/cmp_luasnip'},
                {'hrsh7th/cmp-nvim-lsp'},
                {'hrsh7th/cmp-nvim-lua'},

                -- Snippets
                {'L3MON4D3/LuaSnip'},
                {'rafamadriz/friendly-snippets'},
            }
        },
        {
            'windwp/nvim-autopairs',
            event = "InsertEnter",
            opts = {} -- this is equalent to setup({}) function
        }
        ,
        -- web development
        'jose-elias-alvarez/null-ls.nvim',
        'MunifTanjim/prettier.nvim',
	{'xolox/vim-notes',
dependencies={{'xolox/vim-misc'}}},
}      
    local opts = {}

    require("lazy").setup(plugins, opts)
