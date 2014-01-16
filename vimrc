execute pathogen#infect()
set shiftwidth=4
set tabstop=4
set expandtab
set softtabstop=4
set smarttab
set smartindent
set autoindent
set ignorecase
filetype indent on
set ofu=syntaxcomplete#Complete
highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%81v.\+/
autocmd BufRead *.py inoremap # X<c-h># 
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
"set ruler
set mouse=a
filetype plugin on
let g:pydiction_location="~/.vim/vimfiles/pydiction/complete-dict"
let g:pydiction_menu_height=20
colorscheme candycode
"autocmd vimenter * if !argc() | NERDTree | endif
map <C-n> :NERDTreeToggle<CR>
vmap <C-c> :w !pbcopy<CR><CR>
nmap <C-p> :r !pbpaste<CR><CR>
nmap j gj
nmap k gk

" vim-powerline
set laststatus=2
"set nocompatible
set t_Co=256
"let g:Powerline_symbols = 'fancy'
let g:Powerline_symbols = 'unicode'
let g:Powerline_mode_n = ""
let g:Powerline_mode_i = ""
let g:Powerline_mode_R = ""
let g:Powerline_mode_v = ""
let g:Powerline_mode_V = ""
let g:Powerline_mode_cv = ""
let g:Powerline_mode_s = ""
let g:Powerline_mode_S = ""
let g:Powerline_mode_cs = ""
let g:Powerline_symbols_override={ 'LINE': ''}

"set status line
"hi statusline guibg=DarkGrey ctermfg=8 guifg=White ctermbg=15
"let NERDTreeStatusline = -1

