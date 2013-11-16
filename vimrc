"test
set shiftwidth=4
set tabstop=4
set expandtab
set softtabstop=4
set smarttab
set smartindent
set autoindent
set lbr
set fo+=mB
set sm
set mousemodel=popup
set number
set incsearch "实时搜索结果
set encoding=utf-8
set fileencodings=ucs-bom,utf-8,utf-16,cp9936,gb18030,big5,euc-jp,euc-kr,latin1
syntax on
set showcmd
set ruler
set mouse=a
filetype plugin on
let g:pydiction_location="~/.vim/vimfiles/pydiction/complete-dict"
let g:pydiction_menu_height=20
colorscheme candycode
autocmd vimenter * if !argc() | NERDTree | endif
map <C-n> :NERDTreeToggle<CR>
vmap "+y :w !pbcopy<CR><CR>
nmap "+p :r !pbpaste<CR><CR>
