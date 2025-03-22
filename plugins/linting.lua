return {
    {
        "jose-elias-alvarez/null-ls.nvim",
        config = function()
            require("null-ls").setup {
                sources = {
                    require("null-ls").builtins.diagnostics.eslint_d,
                },
            }
        end,
    },
}

