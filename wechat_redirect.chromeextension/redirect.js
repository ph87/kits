function redirect() {
var url=document.getElementsByTagName('body')[0].attributes['url'];
if (url) {
    document.getElementsByTagName('h3')[0].textContent = 'Redirect';
    window.location.href=url.value;
    }
}
redirect();
