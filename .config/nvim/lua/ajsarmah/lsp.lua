require('lsp-zero')
require('lspconfig').lua_ls.setup({})
require('lspconfig').clangd.setup({})
require('lspconfig').pyright.setup({})
-- requires recent version of node and npm in stable distros use nvm
require('lspconfig').tsserver.setup({})
require('lspconfig').gopls.setup({})
-- We need to install the lsp for haskell externally using ghcup, if ghcup isn't install COMMENT OUT THE LINE BELOW !
require('lspconfig').hls.setup({})

require('mason').setup({})
require('mason-lspconfig').setup({
  ensure_installed = {'lua_ls', 'pyright', 'clangd', 'tsserver', 'gopls', 'hls'},
})

local cmp = require('cmp')

cmp.setup({
 mapping = cmp.mapping.preset.insert({
    ['<Tab>'] = cmp.mapping.confirm({ select = true }),
  }),
})
