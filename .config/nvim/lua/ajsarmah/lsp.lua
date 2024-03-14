require('lsp-zero')
require('lspconfig').lua_ls.setup({})
require('lspconfig').clangd.setup({})
require('lspconfig').pyright.setup({})
require('lspconfig').tsserver.setup({})

require('mason').setup({})
require('mason-lspconfig').setup({
  ensure_installed = {'lua_ls', 'pyright', 'clangd', 'tsserver'},
})

local cmp = require('cmp')

cmp.setup({
 mapping = cmp.mapping.preset.insert({
    ['<Tab>'] = cmp.mapping.confirm({ select = true }),
  }),
})
