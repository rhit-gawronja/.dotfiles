return {
  { "ellisonleao/gruvbox.nvim", config = true, opts = {
    dim_inactive = true,
    transparent_mode = true,
  } },

  -- Configure LazyVim to load gruvbox
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "gruvbox",
    },
  },
}
