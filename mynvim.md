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
