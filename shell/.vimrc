syntax on

" Settings
set number
set relativenumber
set shiftwidth=4
set tabstop=4
set expandtab
set scrolloff=16
set nowrap

" Block cursor in normal, blinking line in insert
let &t_SI = "\<esc>[5 q"
let &t_EI = "\<esc>[1 q"

" Remaps
inoremap jk <Esc>
