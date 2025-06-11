### FORMATTER PRETTIER MENGGUNAKAN NULL-LS

```lua
return {
  "nvimtools/none-ls.nvim",
  dependencies = { "mason.nvim" },
  lazy = true,
  config = function()
    local null_ls = require("null-ls")
    null_ls.setup({
      sources = {
        null_ls.builtins.formatting.stylua,    -- Format Lua
        null_ls.builtins.formatting.shfmt,     -- Format Shell scripts
        null_ls.builtins.formatting.prettier,  -- Format JavaScript/TypeScript
      },
      on_attach = function(client, bufnr)
        if client.supports_method("textDocument/formatting") then
          vim.api.nvim_create_autocmd("BufWritePre", {
            buffer = bufnr,
            callback = function()
              vim.lsp.buf.format({ async = false })
            end,
          })
        end
      end,
    })
  end,
}
```
### LINTING
```lua
return {config = function()
  local null_ls = require("null-ls")
  null_ls.setup({
    sources = {
      -- Linter
      null_ls.builtins.diagnostics.eslint,   -- ESLint
      null_ls.builtins.diagnostics.pyright,  -- Pyright 
    },
  })

  -- Autocommand: Jalankan linting saat keluar dari Insert Mode (ESC)
  vim.api.nvim_create_autocmd("InsertLeave", {
    callback = function()
      vim.lsp.buf.lint()
    end,
  })
end,}
```
